import numpy as np
import pandas as pd
from fastapi.testclient import TestClient
from sklearn.metrics import accuracy_score


# a simple test that uses two fixtures (defined in conftest module)
def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given (the body of our post request to the endpoint)
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }
    expected_no_predictions = 131
    payload = {
      "pclass": 1,
      "name": "Sadawi, Mr, Noureddin",
      "sex": "male",
      "age": 44,
      "sibsp": 0,
      "parch": 0,
      "ticket": "111369",
      "fare": 30,
      "cabin": "C148",
      "embarked": "C",
      "boat": "5",
      "body": 7
    }

    # When
    # notice we post to the predict endpoint
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )
    print(response)

    # Then
    assert response.status_code == 200
    prediction_data = response.json()

    predictions = prediction_data.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.int64)
    assert prediction_data.get("errors") is None
    assert len(predictions) == expected_no_predictions
    # _predictions = list(predictions)
    y_true = test_data["survived"]
    accuracy = accuracy_score(predictions, y_true)
    assert accuracy > 0.7