import pytest
from gradesystem.marks import calculate_average, InvalidMarksError

def test_average():
    assert calculate_average([80, 90, 100]) == 90

def test_invalid_marks():
    with pytest.raises(InvalidMarksError):
        calculate_average([100, 110])
