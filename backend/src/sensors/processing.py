"""Sensor data processing utilities."""


def normalize_temperature(value: float) -> float:
    """Normalize temperature to [0, 1] range (min=10, max=50)."""
    min_t, max_t = 10.0, 50.0
    if value < min_t or value > max_t:
        raise ValueError(f"Temperature {value} out of valid range [{min_t}, {max_t}]")
    return (value - min_t) / (max_t - min_t)


def validate_weight(value: float) -> bool:
    """Return True if weight reading is physically plausible."""
    return 0.0 <= value <= 200.0


def detect_swarming(sound_level: float, threshold: float = 0.8) -> bool:
    """Simple threshold-based swarming detection."""
    return sound_level >= threshold
