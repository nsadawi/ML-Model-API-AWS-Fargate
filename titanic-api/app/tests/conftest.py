import logging
from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from sklearn.model_selection import train_test_split
from titanic_model.config.core import config
from titanic_model.processing.data_manager import _load_raw_dataset

from app.main import app

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    data = _load_raw_dataset(file_name=config.app_config.raw_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data,  # predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )

    return X_test


# standard pattern for setting up fastapi test client so we can make api calls
@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
