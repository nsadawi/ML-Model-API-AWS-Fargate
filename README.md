## Video to Complete Course on 2nd Dec 2022 is here: https://youtu.be/5wSL86Yi37s


## Run With tox (Recommended):
- Install tox using: `pip install tox`
- Make sure you are in the classification_model directory (where the tox.ini file is) then run the command: `tox` (this runs the tests and typechecks, trains the model under the hood). The first time you run this it creates a virtual env and installs
dependencies, so takes a few minutes.

## Run Without tox:
- Add ML-Model-Packaging *and* classification_model paths to your system PYTHONPATH
- `pip install -r requirements/test_requirements`
- Train the model: `python classification_model/train_pipeline.py`
- Run the tests `pytest tests`
