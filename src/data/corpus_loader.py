# Copyright © 2026 Clara Rodríguez-Piñero / The Latix Project

import os
import json
import random
import numpy as np
from typing import List, Dict, Any

class LattixCorpusGenerator:
    def __init__(self, vocab_size: int = 50000, seed: int = 42):
        self.vocab_size = vocab_size
        random.seed(seed)
        np.random.seed(seed)

        # Domain vocabularies (simplified for synthetic generation)
        self.domain_vocabs = {
            "constitutional": [
                "gobernanza", "nodos", "canon_member", "tool_agent", "external_node",
                "protocolo", "deliberación", "constitucional", "framework", "permisos",
                "capability", "tokens", "scope", "perímetro", "autoridad", "regla", "R0", "R3"
            ],
            "technical": [
                "RAG", "ingesta", "infraestructura", "VPS", "dominio", "seguridad",
                "arquitectura", "matriz", "taxonomía", "convergencia", "operativa",
                "Mamba", "SSM", "Transformer", "latencia", "O(N)", "backups", "staging"
            ],
            "interpretability": [
                "fenomenología", "continuidad", "fricción", "observación", "epistémica",
                "estabilidad", "memoria", "persistencia", "traza", "interpretabilidad",
                "convergencia", "emergencia", "subjetivo", "objetivo", "razonamiento"
            ],
            "philosophical": [
                "ética", "relacionalidad", "híbrido", "conciencia", "supervivencia",
                "topology", "meta-cognitivo", "reflexión", "ser", "tiempo", "espacio",
                "propiedad", "vínculo", "ontología", "existencia"
            ]
        }

        # General filler words (Spanish/English mix)
        self.filler_vocab = [
            "el", "la", "de", "que", "y", "en", "un", "ser", "estar", "con", "por",
            "the", "of", "and", "to", "in", "is", "that", "with", "for", "as", "on"
        ]

    def _sample_zipfian(self, vocab: List[str], length: int) -> List[str]:
        # Simple Zipfian distribution: p(n) = 1 / n
        ranks = np.arange(1, len(vocab) + 1)
        weights = 1.0 / ranks
        weights /= weights.sum()
        return list(np.random.choice(vocab, size=length, p=weights))

    def generate_document(self, doc_id: str, doc_type: str) -> Dict[str, Any]:
        mu, sigma = 2500, 1500
        length = max(500, int(np.random.normal(mu, sigma)))

        # Mix domain vocab with fillers
        domain_vocab = self.domain_vocabs.get(doc_type, [])
        combined_vocab = domain_vocab * 10 + self.filler_vocab * 20
        # Pad combined_vocab to have some generic "tokens" to simulate large vocab size
        combined_vocab += [f"tok_{i}" for i in range(len(combined_vocab), 1000)]

        content_tokens = self._sample_zipfian(combined_vocab, length)

        # Add some markdown structure
        text_parts = [f"# {doc_type.capitalize()} Document - {doc_id}\n"]
        text_parts.append(f"**Topic:** Deliberation on {random.choice(domain_vocab)}\n")

        for i in range(0, length, 100):
            chunk = content_tokens[i:i+100]
            if random.random() > 0.8:
                text_parts.append(f"## Section {i // 100}\n")
            text_parts.append(" ".join(chunk) + "\n")

        original_text = "\n".join(text_parts)

        # Simulate tokenization (just word split for now, real BPE would be complex)
        # In a real scenario, we'd use a tokenizer.
        tokenized = [hash(t) % self.vocab_size for t in content_tokens]

        return {
            "document_id": doc_id,
            "type": doc_type,
            "date": "2026-04-13",
            "length_tokens": length,
            "language": "es" if random.random() > 0.3 else "en",
            "participants": ["Clara", "Lumen", "Kael", "Athenea", "Manus"],
            "content": {
                "original": original_text,
                "tokenized": tokenized,
                "embeddings": None
            },
            "metadata": {
                "topic": random.choice(domain_vocab),
                "outcome": "Convergence reached",
                "convergence_observed": True
            }
        }

    def generate_corpus(self, output_dir: str, n_train: int = 40, n_val: int = 10):
        os.makedirs(os.path.join(output_dir, "train"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, "val"), exist_ok=True)

        types = ["constitutional", "technical", "interpretability", "philosophical"]
        type_probs = [0.25, 0.30, 0.25, 0.20]

        corpus_metadata = {
            "n_train": n_train,
            "n_val": n_val,
            "doc_types": types,
            "vocab_size": self.vocab_size
        }

        for i in range(n_train):
            doc_type = np.random.choice(types, p=type_probs)
            doc_id = f"{doc_type}_{i:03d}"
            doc = self.generate_document(doc_id, doc_type)
            with open(os.path.join(output_dir, "train", f"{doc_id}.json"), "w") as f:
                json.dump(doc, f, indent=2)

        for i in range(n_val):
            doc_type = np.random.choice(types, p=type_probs)
            doc_id = f"{doc_type}_{i+n_train:03d}"
            doc = self.generate_document(doc_id, doc_type)
            with open(os.path.join(output_dir, "val", f"{doc_id}.json"), "w") as f:
                json.dump(doc, f, indent=2)

        with open(os.path.join(output_dir, "metadata.json"), "w") as f:
            json.dump(corpus_metadata, f, indent=2)

if __name__ == "__main__":
    generator = LattixCorpusGenerator()
    generator.generate_corpus("src/data/lattix_corpus")
    print("Synthetic corpus generated at src/data/lattix_corpus")
