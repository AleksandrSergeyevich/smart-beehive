import pytest
from src.ml.swarming_classifier import SwarmingClassifier, SwarmingFeatures


clf = SwarmingClassifier()


def test_swarm_detected_high_sound():
    f = SwarmingFeatures(sound_level=0.9, temperature=35.0, weight_delta=0.5)
    assert clf.predict(f) is True


def test_no_swarm_low_sound():
    f = SwarmingFeatures(sound_level=0.1, temperature=25.0, weight_delta=0.0)
    assert clf.predict(f) is False


def test_proba_range():
    f = SwarmingFeatures(sound_level=0.5, temperature=30.0, weight_delta=0.1)
    p = clf.predict_proba(f)
    assert 0.0 <= p <= 1.0


def test_threshold_boundary():
    f = SwarmingFeatures(sound_level=1.0, temperature=0.0, weight_delta=0.0)
    assert clf.predict_proba(f) == pytest.approx(0.6, abs=0.05)
