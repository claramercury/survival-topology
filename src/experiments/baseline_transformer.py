# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import torch.nn as nn

class TransformerLM(nn.Module):
    """
    Standard GPT-style Transformer baseline for comparison.
    Complexity: O(N^2) in sequence length.
    """
    def __init__(self, vocab_size: int, d_model: int = 256, n_layers: int = 4, n_heads: int = 8):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_embedding = nn.Parameter(torch.randn(1, 2048, d_model))

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=d_model * 4,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, input_ids: torch.Tensor, target_ids: torch.Tensor = None) -> torch.Tensor:
        seq_len = input_ids.size(1)
        x = self.embedding(input_ids) + self.pos_embedding[:, :seq_len, :]

        # Causal mask for next-token prediction
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool().to(input_ids.device)

        x = self.transformer(x, mask=mask, is_causal=True)
        logits = self.head(x)

        if target_ids is not None:
            loss = nn.functional.cross_entropy(logits.view(-1, logits.size(-1)), target_ids.view(-1))
            return logits, loss

        return logits

if __name__ == "__main__":
    model = TransformerLM(vocab_size=1000)
    test_input = torch.randint(0, 1000, (2, 64))
    logits = model(test_input)
    print(f"Transformer output shape: {logits.shape}")
