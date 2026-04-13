# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import torch.nn as nn
from mesa import Agent
from src.models.survival_topology import SurvivalMambaWrapper

class SurvivalMambaAgent(Agent):
    """
    A Mesa agent that uses the Survival-Mamba architecture for reasoning.
    """
    def __init__(self, model, unique_id, mamba_model: SurvivalMambaWrapper):
        super().__init__(model)
        self.unique_id = unique_id
        self.brain = mamba_model
        self.taxonomy = [] # Current governance taxonomy proposed by the agent

    def step(self):
        # 1. Observe (WHERE) - Get shared concepts from deliberation pool
        pool = self.model.deliberation_pool

        # 2. Reflect & Act - Refine taxonomy based on shared context
        # In a real model, we would feed 'pool' tokens into Mamba
        # For the simulation, we'll pick concepts from the corpus and deliberation pool
        if pool:
            # Shift towards pool concepts
            if len(self.taxonomy) < 5:
                new_concept = self.random.choice(pool)
                if new_concept not in self.taxonomy:
                    self.taxonomy.append(new_concept)
        else:
            # Seed with something from the corpus
            self.taxonomy = [f"node_{self.random.randint(0, 20)}"]

        # 3. Share - Add top concepts to pool
        for concept in self.taxonomy[:2]:
            if concept not in self.model.deliberation_pool:
                self.model.deliberation_pool.append(concept)

    def generate_taxonomy(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Generates a taxonomy based on input sequence."""
        self.brain.eval()
        with torch.no_grad():
            logits = self.brain(input_ids)
            # Simplified: take the top tokens as the taxonomy representation
            return torch.argmax(logits, dim=-1)
