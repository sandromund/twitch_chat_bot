"""
Pytest
"""

import pytest
from pydantic import ValidationError

from source.main import ConfigFilePath


def test_config_file_path_invalid():
    """Test ConfigFilePath model with an invalid path."""
    invalid_path = "invalid/path/to/config.yaml"
    with pytest.raises(ValidationError):
        ConfigFilePath(path=invalid_path)
