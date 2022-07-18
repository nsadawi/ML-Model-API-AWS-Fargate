import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from titanic_model import __version__ as model_version
from titanic_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


# health endpoint
@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    # we define a response schema
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )
    # return schema as a dict (fastapi will do conversion to json for response)
    return health.dict()


# predict endpoint
# the expected inputs make use of a schema
@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleTitanicDataInputs) -> Any:
    """
    Make titanic survival predictions with the classification model
    """
    # load inputs into a DF
    # jsonable_encoder handles loading pydantic data into json in the format
    # expected by pandas
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    # get the results as a dict
    # replace nan with None so pydantic can work with them correctly
    results = make_prediction(input_data=input_df.replace({np.nan: None}))
    # check the dict for errors
    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")
    # if no errors, return results in the format specified in the response
    # model (pydantic and fastapi working together)
    return results
