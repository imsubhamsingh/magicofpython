"""
Tests the validator functions
Command line: python -m pytest tests/unit/test_validators.py
"""

import pytest
from inventory.app.utils.validators import validate_integer


class TestIntergerValidator:
    def test_valid(self):
        validate_integer('arg', 10, 0, 20, 'custom min msg', 'custom max msg')
