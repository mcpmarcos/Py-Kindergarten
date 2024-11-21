from http import HTTPStatus

# Organizar(arrange)
# Agir(act)
# Affirmar(assert)
# Teardown

# =========================================================#

# Organizar(arrange)
def test_readRoot_returningOk(client):
    # Agir(act)
    response = client.get("/")
    # Affirmar(assert)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}
    # Teardown


def test_create_user(client):
    response = client.post("/user/",
                json={"name": "Billy Joe", "email": "john.doe@example.com", "password": "password"}
                )
    # Voltou o status corrreto?
    assert response.status_code == HTTPStatus.OK
    # Validar UserPublic
    assert response.json() == {
        "name": "Billy Joe", "email": "john.doe@example.com", "id": 1
    }