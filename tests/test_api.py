import pytest
from fastapi.testclient import TestClient
from api.api import app  # Import your FastAPI app

client = TestClient(app)


def test_health_check():
    """Test whether the API works"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_file():
    """Test the API output"""
    # Simulate file content
    file_content = '{"spoor": "ACG", "profielen": ["ACG", "ACT"]}'
    files = {"file": ("test.json", file_content, "application/json")}

    # Make the request
    response = client.post("/process", files=files)

    # Assert response
    assert response.status_code == 200
    assert response.json() == {
        "ACG": "Het DNA profiel past in spoor: DNASpoor(sequentie='ACG') vs DNAProfiel(sequentie='ACG')",
        "ACT": "Het DNA profiel past niet in spoor: DNASpoor(sequentie='ACG') vs DNAProfiel(sequentie='ACT')",
    }
