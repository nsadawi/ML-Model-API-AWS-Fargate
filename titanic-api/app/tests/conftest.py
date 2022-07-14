from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from model.config.core import config
from model.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    # use the load_dataset function from our package
    # as well as the test data file
    # any consuming application of the package gets out of the box a series of
    # test data and utilities so it can use that test data 
    return load_dataset(file_name=config.app_config.test_data_file)


# standard pattern for setting up fastapi test client so we can make api calls
@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
