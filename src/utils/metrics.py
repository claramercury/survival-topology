# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import torch
import networkx as nx
import numpy as np
from typing import List

def calculate_graph_similarity(taxonomy1: List[str], taxonomy2: List[str]) -> float:
    """
    Calculates similarity between two taxonomies using graph isomorphism principles.
    Simplified: uses Jaccard similarity of edges in a path graph.
    """
    if not taxonomy1 or not taxonomy2:
        return 0.0

    g1 = nx.path_graph(len(taxonomy1))
    g2 = nx.path_graph(len(taxonomy2))

    # In this simplified model, we compare the set of unique 'concepts' (top tokens)
    set1 = set(taxonomy1)
    set2 = set(taxonomy2)

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    return intersection / union if union > 0 else 0.0

def measure_efficiency(model: torch.nn.Module, seq_len: int, batch_size: int = 1):
    """Measures time and memory for a single forward pass."""
    import time
    input_ids = torch.randint(0, 1000, (batch_size, seq_len))

    start_time = time.time()
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    model.eval()
    with torch.no_grad():
        _ = model(input_ids)

    duration = time.time() - start_time
    memory = 0 # Dummy for CPU

    return duration, memory
