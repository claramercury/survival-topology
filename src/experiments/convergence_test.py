# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import os
import json
import torch
import torch.optim as optim
from mesa import Model
from src.models.agent import SurvivalMambaAgent
from src.models.mamba_ssm import MambaLM
from src.models.survival_topology import SurvivalMambaWrapper
from tqdm import tqdm

class GovernanceExperimentModel(Model):
    """
    Orchestrates the 3-agent experiment on governance taxonomy.
    """
    def __init__(self, n_agents=3, vocab_size=50000, d_model=256):
        super().__init__()
        self.vocab_size = vocab_size
        self.deliberation_pool = []

        # Share the same corpus (restricted)
        self.corpus = self.load_corpus()

        for i in range(n_agents):
            mamba = MambaLM(vocab_size=vocab_size, d_model=d_model)
            wrapped = SurvivalMambaWrapper(mamba)
            SurvivalMambaAgent(self, i, wrapped)

    def load_corpus(self):
        corpus_path = "src/data/lattix_corpus/train"
        files = [os.path.join(corpus_path, f) for f in os.listdir(corpus_path) if f.endswith(".json")]
        docs = []
        for f in files:
            with open(f, "r") as f_in:
                docs.append(json.load(f_in))
        return docs

    def train_agents(self, epochs=5):
        print(f"Training {len(self.agents)} agents on restricted corpus...")
        for agent in self.agents:
            optimizer = optim.Adam(agent.brain.parameters(), lr=1e-4)
            agent.brain.train()
            for epoch in range(epochs):
                total_loss = 0
                for doc in self.corpus:
                    tokens = torch.LongTensor(doc["content"]["tokenized"]).unsqueeze(0)
                    # Simple next-token prediction
                    input_ids = tokens[:, :-1]
                    target_ids = tokens[:, 1:]

                    if input_ids.size(1) == 0: continue

                    # Truncate to reasonable length for CPU
                    input_ids = input_ids[:, :512]
                    target_ids = target_ids[:, :512]

                    optimizer.zero_grad()
                    _, loss = agent.brain(input_ids, target_ids)
                    loss.backward()
                    optimizer.step()
                    total_loss += loss.item()
                # print(f"Agent {agent.unique_id} - Epoch {epoch} - Loss: {total_loss/len(self.corpus):.4f}")

    def run_simulation(self, steps=100):
        print(f"Running multi-agent simulation for {steps} steps...")
        # In a real experiment, agents would interact.
        # Here we simulate the emergence of taxonomic convergence.
        # Each step, agents refine their 'internal' taxonomy based on shared task.
        for i in tqdm(range(steps)):
            self.step()

    def step(self):
        # In Mesa 3.0+, we can iterate over agents directly if we don't use a specific scheduler
        for agent in self.agents:
            agent.step()

if __name__ == "__main__":
    # Quick test of the experiment model
    # Use real vocab size from metadata to avoid IndexError
    model = GovernanceExperimentModel(n_agents=2, vocab_size=50000, d_model=64)
    model.train_agents(epochs=1)
    model.run_simulation(steps=5)
    print("Orchestration test complete.")
