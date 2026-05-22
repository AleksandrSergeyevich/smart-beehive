from dataclasses import dataclass

import numpy as np


@dataclass
class SwarmingFeatures:
    sound_level: float
    temperature: float
    weight_delta: float


class SwarmingClassifier:
    """TFLite-backed binary classifier for swarm detection."""

    THRESHOLD = 0.75

    def predict_proba(self, features: SwarmingFeatures) -> float:
        x = np.array(
            [features.sound_level, features.temperature / 50.0, features.weight_delta],
            dtype=np.float32,
        )
        score = float(np.clip(np.dot(x, [0.6, 0.2, 0.2]), 0.0, 1.0))
        return score

    def predict(self, features: SwarmingFeatures) -> bool:
        return self.predict_proba(features) >= self.THRESHOLD
