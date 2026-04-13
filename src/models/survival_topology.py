# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import torch.nn as nn
import torch.nn.functional as F

class SurvivalConstraints(nn.Module):
    """
    Implements the 7 dimensions of Survival Topology (Wh- Protocol)
    as formal constraints on the Mamba SSM dynamics.
    """
    def __init__(self, d_model: int):
        super().__init__()
        self.d_model = d_model

        # WHO: Identity Anchor (Immutable-ish prompt vector)
        self.register_buffer("identity_anchor", torch.randn(1, 1, d_model))

        # Mapping dimensions to SSM gates/parameters
        # WHERE: Spatial Context (Entropy sensing)
        self.where_gate = nn.Linear(d_model, d_model)

        # WHY: Utility/Will (Reward signal)
        self.why_potential = nn.Parameter(torch.ones(1))

    def apply_who(self, x: torch.Tensor) -> torch.Tensor:
        """WHO: Attracts input towards identity (Gravity)."""
        # Simple residual connection to identity anchor
        return x + 0.1 * self.identity_anchor

    def apply_where(self, x: torch.Tensor) -> torch.Tensor:
        """WHERE: Filters input based on environment entropy."""
        gate = torch.sigmoid(self.where_gate(x))
        return x * gate

    def calculate_what_pain(self, predicted: torch.Tensor, reality: torch.Tensor) -> torch.Tensor:
        """WHAT: Pain (Error signal)."""
        return F.mse_loss(predicted, reality)

    def apply_which_selectivity(self, dt: torch.Tensor, selectivity_factor: float) -> torch.Tensor:
        """WHICH: Modulates Mamba's selectivity (Imaginary path simulation)."""
        return dt * selectivity_factor

    def apply_how_intensity(self, output: torch.Tensor, intensity: float) -> torch.Tensor:
        """HOW: Computational intensity (Obsession)."""
        return output * intensity

    def apply_when_resonance(self, t: int, freq: float) -> float:
        """WHEN: Phase locking (Timing)."""
        return 0.5 * (1.0 + torch.cos(torch.tensor(t * freq)))

    def apply_why_will(self, loss: torch.Tensor) -> torch.Tensor:
        """WHY: The Prime Mover (Energy cost)."""
        return loss * self.why_potential

class SurvivalMambaWrapper(nn.Module):
    def __init__(self, mamba_model: nn.Module):
        super().__init__()
        self.model = mamba_model
        self.constraints = SurvivalConstraints(mamba_model.d_model)

    def forward(self, input_ids: torch.Tensor, target_ids: torch.Tensor = None, step: int = 0) -> torch.Tensor:
        # WHO & WHERE integration
        x = self.model.embedding(input_ids)
        x = self.constraints.apply_who(x)
        x = self.constraints.apply_where(x)

        # WHEN: Temporal resonance (Modulates the entire sequence activation)
        resonance = self.constraints.apply_when_resonance(step, freq=0.1)
        x = x * resonance

        # Mamba forward
        for layer in self.model.layers:
            # WHICH: Selective state modulation (inside layer logic ideally, but here as a filter)
            # We apply a selectivity factor to the input of each layer
            x = self.constraints.apply_which_selectivity(x, selectivity_factor=1.0)
            x, _ = layer(x)

        x = self.model.norm(x)

        # HOW: Computational intensity
        x = self.constraints.apply_how_intensity(x, intensity=1.1)

        logits = self.model.head(x)

        if target_ids is not None:
            # WHAT: Pain calculation
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), target_ids.view(-1))
            # WHY: Utility weighting
            loss = self.constraints.apply_why_will(loss)
            return logits, loss

        return logits
