import pytest
import tasks


def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")
