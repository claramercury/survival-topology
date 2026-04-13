# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
from src.models.mamba_ssm import MambaLM
from src.models.survival_topology import SurvivalMambaWrapper

def test_survival_wrapper():
    vocab_size = 100
    d_model = 32
    mamba = MambaLM(vocab_size=vocab_size, d_model=d_model)
    wrapped = SurvivalMambaWrapper(mamba)

    input_ids = torch.randint(0, vocab_size, (2, 10))
    target_ids = torch.randint(0, vocab_size, (2, 10))

    logits, loss = wrapped(input_ids, target_ids)

    assert logits.shape == (2, 10, vocab_size)
    assert loss > 0
    print("Survival Topology wrapper tests passed!")

if __name__ == "__main__":
    test_survival_wrapper()
