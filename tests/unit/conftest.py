import pytest

from business.application_factory import create_app


@pytest.fixture
def client():
    with create_app().test_client() as client:
        yield client
