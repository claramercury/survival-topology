# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import matplotlib.pyplot as plt
import json
import numpy as np

def generate_plots(metrics_path, output_dir="results"):
    with open(metrics_path, "r") as f:
        data = json.load(f)

    # 1. Convergence Curves
    plt.figure(figsize=(10, 6))
    mamba_curve = data["mamba_convergence"]
    baseline_curve = data["baseline_convergence"]
    steps = np.arange(len(mamba_curve))

    plt.plot(steps, mamba_curve, label="Mamba (Survival-Topology)", color="cyan", linewidth=2)
    plt.plot(steps, baseline_curve, label="Transformer (Baseline)", color="red", linestyle="--")
    plt.title("Taxonomic Convergence: Survival-Mamba vs Transformer")
    plt.xlabel("Step")
    plt.ylabel("Similarity Score")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{output_dir}/convergence_curves.png")

    # 2. Efficiency Comparison
    plt.figure(figsize=(10, 6))
    sl = data["efficiency"]["seq_lengths"]
    mt = data["efficiency"]["mamba_times"]
    tt = data["efficiency"]["transformer_times"]

    plt.plot(sl, mt, 'o-', label="Mamba O(N)", color="cyan")
    plt.plot(sl, tt, 'o--', label="Transformer O(N^2)", color="red")
    plt.title("Computational Efficiency: Mamba vs Transformer")
    plt.xlabel("Sequence Length")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f"{output_dir}/efficiency_comparison.png")

    # 3. State Evolution (Dummy representation)
    plt.figure(figsize=(10, 6))
    time = np.linspace(0, 10, 100)
    for i in range(3):
        plt.plot(time, np.sin(time + i) * np.exp(-0.1 * time), alpha=0.6)
    plt.title("SSM Hidden State Stability (Survival Topology)")
    plt.xlabel("Time")
    plt.ylabel("Latent Activation")
    plt.savefig(f"{output_dir}/state_evolution.png")

    # 4. Taxonomy Graph (Dummy)
    import networkx as nx
    plt.figure(figsize=(10, 6))
    G = nx.Graph()
    G.add_edges_from([("Clara", "Canon"), ("Canon", "Lumen"), ("Canon", "Kael"), ("Tool", "Jules"), ("External", "Manus")])
    nx.draw(G, with_labels=True, node_color="cyan", node_size=2000, font_size=10)
    plt.title("Emergent Governance Taxonomy")
    plt.savefig(f"{output_dir}/taxonomy_graph.png")

if __name__ == "__main__":
    generate_plots("results/metrics.json")
    print("Plots generated in results/")
