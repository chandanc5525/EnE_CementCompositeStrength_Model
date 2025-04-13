import pytest
from src.Ml_Model.model import get_xgb_model

def test_model_creation():
    model = get_xgb_model({'n_estimators': 100})
    assert model is not None