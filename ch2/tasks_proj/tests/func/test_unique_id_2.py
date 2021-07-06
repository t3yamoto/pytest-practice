import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    # setup
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # run test here

    # teardown
    tasks.stop_tasks_db()


@pytest.mark.skip(reason="misunderstood the API")
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task("one")))
    ids.append(tasks.add(Task("two")))
    ids.append(tasks.add(Task("three")))

    uid = tasks.unique_id()

    assert uid not in ids
