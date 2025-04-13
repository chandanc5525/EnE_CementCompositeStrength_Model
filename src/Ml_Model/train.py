from sklearn.model_selection import GridSearchCV

def train_model(model, X, y, param_grid, cv=5):
    grid = GridSearchCV(model, param_grid, cv=cv, scoring='r2')
    grid.fit(X, y)
    return grid.best_estimator_, grid.best_params_
