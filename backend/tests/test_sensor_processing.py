import pytest
from src.sensors.processing import normalize_temperature, validate_weight, detect_swarming


def test_normalize_temperature_normal():
    assert normalize_temperature(25.0) == pytest.approx(0.375, abs=0.01)


def test_normalize_temperature_min():
    assert normalize_temperature(10.0) == pytest.approx(0.0, abs=0.01)


def test_normalize_temperature_max():
    assert normalize_temperature(50.0) == pytest.approx(1.0, abs=0.01)


def test_normalize_temperature_out_of_range():
    with pytest.raises(ValueError):
        normalize_temperature(200.0)


def test_normalize_temperature_below_min():
    with pytest.raises(ValueError):
        normalize_temperature(-5.0)


def test_validate_weight_positive():
    assert validate_weight(35.5) is True


def test_validate_weight_zero():
    assert validate_weight(0.0) is True


def test_validate_weight_negative():
    assert validate_weight(-1.0) is False


def test_validate_weight_too_heavy():
    assert validate_weight(999.0) is False


def test_detect_swarming_positive():
    assert detect_swarming(0.9) is True


def test_detect_swarming_negative():
    assert detect_swarming(0.3) is False


def test_detect_swarming_custom_threshold():
    assert detect_swarming(0.5, threshold=0.4) is True
