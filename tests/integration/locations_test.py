import requests


def test_added_location_can_be_retrieved(application_container):
    _, port = application_container
    item_to_store = {"name": "whatever"}

    # Store object
    response = requests.post(f"http://localhost:{port}/location", json=item_to_store)
    assert response.status_code == 200

    stored_item_id = response.json()["id"]
    # Attempt to retrieve stored location
    response = requests.get(f"http://localhost:{port}/location/{stored_item_id}")

    item_to_store["id"] = stored_item_id
    assert response.status_code == 200
    assert response.json() == item_to_store
