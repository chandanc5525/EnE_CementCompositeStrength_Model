from xgboost import XGBRegressor

def get_xgb_model(params):
    return XGBRegressor(**params)