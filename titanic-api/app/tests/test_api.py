import math

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

# a simple test that uses two fixtures (defined in conftest module)
def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given (the body of our post request to the endpoint)
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    # notice we post to the predict endpoint
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert math.isclose(prediction_data["predictions"][0], 113422, rel_tol=100)
