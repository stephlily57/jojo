"""
NAYA LLM INTEGRATION — NVIDIA GPU ACCELERATOR

Rôle :
- Détecter la disponibilité GPU
- Signaler une capacité d'accélération
"""

from typing import Dict


class NvidiaGPUEngine:

    def detect(self) -> Dict[str, bool]:
        """
        Détection simple GPU Nvidia.
        """
        try:
            import torch
            return {
                "gpu_available": torch.cuda.is_available()
            }
        except ImportError:
            return {
                "gpu_available": False
            }
