import os
import pytest
from pathlib import Path


@pytest.fixture(autouse=True)
def without_cachew():
    from my.core.cachew import disabled_cachew

    with disabled_cachew():
        yield
