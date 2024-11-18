from http import HTTPStatus

from fastapi.testclient import TestClient

from banking_client_services.app import app

client = TestClient(app)


# Organizar(arrange)
def test_readRoot_returningOk(): ...


# Agir(act)
response = client.get("/")


# Affirmar(assert)
assert response.status_code == HTTPStatus.OK
assert response.json() == {"message": "Hello World"}

# Teardown
