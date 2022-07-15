from typing import Any, List, Optional

from pydantic import BaseModel
from titanic_model.processing.validation import TitanicDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]

    # in this pydantic config class we're able to provide an example
    # example with dummy values
    # we can try this example out in our documentation
    # fastapi pics up inputs and response models of diff endpoints
    # based on that and little config we get documentation out of the box
    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
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
                        "body": 7,
                    },
                    {
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
                        "body": 7,
                    },
                    {
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
                        "body": 7,
                    },
                ]
            }
        }
