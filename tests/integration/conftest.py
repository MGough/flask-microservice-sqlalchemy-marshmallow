import time

import docker
import pytest
import requests

APPLICATION_PORT = 8000


@pytest.fixture(scope="session")
def docker_client():
    return docker.from_env()


@pytest.fixture(scope="session")
def application_image(docker_client):
    image, logs = docker_client.images.build(path="./", pull=True)
    for log in logs:
        print(log)
    return image


@pytest.fixture
def application_container(docker_client, application_image):
    container = docker_client.containers.run(
        application_image,
        detach=True,
        auto_remove=True,
        ports={f"{APPLICATION_PORT}/tcp": None},
        environment={"ENV_FOR_DYNACONF": "integration"},
    )
    # Update container attributes to ensure exposed port is available
    container.reload()

    assigned_port = container.ports[f"{APPLICATION_PORT}/tcp"][0]["HostPort"]
    _wait_for_application(assigned_port)

    yield container, assigned_port
    print(container.logs())
    try:
        container.stop()
    except docker.errors.APIError as ex:
        print(f"Error when killing container: {ex}")


def _wait_for_application(port):
    """
    This waits for the HTTP server within the container to start responding
    to ensure that we're not running integration tests too soon
    It hits the /health endpoint until a response is received or until a
    period of time has elapsed.
    :param port: The of the service on the host machine
    """
    for i in range(10):
        try:
            requests.get(f"http://localhost:{port}/health")
            print("Connected to newly created container")
            break
        except requests.RequestException as ex:
            print(f"error connecting to newly created container: {ex}")
            time.sleep(i / 100)
