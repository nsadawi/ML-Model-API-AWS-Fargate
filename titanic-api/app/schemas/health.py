from pydantic import BaseModel


# class inhertis from BaseModel and uses type hints so we can get
# automatic validation
class Health(BaseModel):
    name: str
    api_version: str
    model_version: str
