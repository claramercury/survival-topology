# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import pytest
from src.models.mamba_ssm import MambaLayer, MambaLM

def test_mamba_layer_shape():
    batch, seq_len, d_model = 2, 10, 32
    layer = MambaLayer(d_model=d_model, d_state=8)
    x = torch.randn(batch, seq_len, d_model)
    output, state = layer(x)
    assert output.shape == (batch, seq_len, d_model)
    assert state.shape == (batch, layer.d_inner, 8)

def test_mamba_lm_output():
    vocab_size = 100
    model = MambaLM(vocab_size=vocab_size, d_model=32, n_layers=2)
    x = torch.randint(0, vocab_size, (1, 20))
    output = model(x)
    assert output.shape == (1, 20, vocab_size)

if __name__ == "__main__":
    test_mamba_layer_shape()
    test_mamba_lm_output()
    print("Mamba implementation tests passed!")
