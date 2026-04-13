# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from typing import Optional, Tuple

class MambaLayer(nn.Module):
    """
    A pure PyTorch implementation of the Selective State Space Model (SSM) layer,
    following the Mamba architecture principles.
    Complexity: O(N) in sequence length.
    """
    def __init__(self, d_model: int, d_state: int = 16, d_conv: int = 4, expand: int = 2):
        super().__init__()
        self.d_model = d_model
        self.d_state = d_state
        self.d_inner = expand * d_model
        self.d_conv = d_conv

        # Projection layers
        self.in_proj = nn.Linear(d_model, self.d_inner * 2, bias=False)
        self.out_proj = nn.Linear(self.d_inner, d_model, bias=False)

        # 1D Convolution
        self.conv1d = nn.Conv1d(
            in_channels=self.d_inner,
            out_channels=self.d_inner,
            kernel_size=d_conv,
            groups=self.d_inner,
            padding=d_conv - 1
        )

        # Selective SSM parameters
        self.x_proj = nn.Linear(self.d_inner, d_state * 2 + self.d_inner, bias=False)
        self.dt_proj = nn.Linear(self.d_inner, self.d_inner, bias=True)

        # Fixed parameters (simplified for this prototype)
        self.A_log = nn.Parameter(torch.log(torch.arange(1, d_state + 1).float().repeat(self.d_inner, 1)))
        self.D = nn.Parameter(torch.ones(self.d_inner))

    def forward(self, x: torch.Tensor, state: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        x: (batch, seq_len, d_model)
        Returns: (output, next_state)
        """
        batch, seq_len, _ = x.shape

        # 1. In projection
        xz = self.in_proj(x) # (batch, seq_len, 2 * d_inner)
        x, z = xz.chunk(2, dim=-1) # (batch, seq_len, d_inner)

        # 2. Convolution (sequential processing for O(N))
        x = x.transpose(1, 2) # (batch, d_inner, seq_len)
        x = self.conv1d(x)[:, :, :seq_len]
        x = x.transpose(1, 2) # (batch, seq_len, d_inner)
        x = F.silu(x)

        # 3. Selective SSM
        # x_proj outputs dt, B, C
        dt_B_C = self.x_proj(x) # (batch, seq_len, d_inner + 2 * d_state)
        dt, B, C = torch.split(dt_B_C, [self.d_inner, self.d_state, self.d_state], dim=-1)

        dt = F.softplus(self.dt_proj(dt)) # (batch, seq_len, d_inner)
        A = -torch.exp(self.A_log) # (d_inner, d_state)

        # Selective scan (Simplified loop for O(N) proof of concept)
        # In real Mamba, this is a parallel scan, but for multi-agent O(N) is the key.
        y = []
        h = torch.zeros(batch, self.d_inner, self.d_state, device=x.device) if state is None else state

        for t in range(seq_len):
            # discretization
            # dA = exp(dt * A)
            # dB = dt * B
            dt_t = dt[:, t, :].unsqueeze(-1) # (batch, d_inner, 1)
            B_t = B[:, t, :].unsqueeze(1) # (batch, 1, d_state)
            C_t = C[:, t, :].unsqueeze(-1) # (batch, d_state, 1)

            dA = torch.exp(dt_t * A) # (batch, d_inner, d_state)
            dB = dt_t * B_t # (batch, d_inner, d_state)

            # State update: h = dA * h + dB * x
            x_t = x[:, t, :].unsqueeze(-1) # (batch, d_inner, 1)
            h = dA * h + dB * x_t # (batch, d_inner, d_state)

            # Output: y = C * h
            y_t = torch.bmm(h, C_t).squeeze(-1) # (batch, d_inner)
            y.append(y_t)

        y = torch.stack(y, dim=1) # (batch, seq_len, d_inner)

        # 4. Out projection
        y = y * F.silu(z)
        output = self.out_proj(y)

        return output, h

class MambaLM(nn.Module):
    def __init__(self, vocab_size: int, d_model: int = 256, n_layers: int = 4, d_state: int = 16):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.layers = nn.ModuleList([
            MambaLayer(d_model=d_model, d_state=d_state) for _ in range(n_layers)
        ])
        self.norm = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        x = self.embedding(input_ids)
        for layer in self.layers:
            x, _ = layer(x)
        x = self.norm(x)
        return self.head(x)

if __name__ == "__main__":
    # Simple test
    model = MambaLM(vocab_size=1000)
    test_input = torch.randint(0, 1000, (2, 64))
    output = model(test_input)
    print(f"Output shape: {output.shape}") # Expected: (2, 64, 1000)
