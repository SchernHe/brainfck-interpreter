from pathlib import Path
import pytest

ROOT_PATH = Path(__file__)


@pytest.fixture
def test_data() -> Path:
    """Provide the path to the test data."""
    test_data_path = ROOT_PATH.parent / "test_data"
    return test_data_path
