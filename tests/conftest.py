import pytest
from fastapi.testclient import TestClient

from banking_client_services.app import app


@pytest.fixture
def client():
    return TestClient(app)



