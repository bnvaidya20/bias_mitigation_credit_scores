
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV


def optimize_hyperparameters(dataset, model, param_grid, fit_params=None, cv=10):
    """
    Optimizes hyperparameters for a given machine learning model using GridSearchCV.

    Parameters:
    - dataset: The dataset to use for training, which should include features, labels, and instance_weights.
    - model: The machine learning model to be used (e.g., LogisticRegression, RandomForestClassifier).
    - param_grid: A dictionary defining the hyperparameters to be optimized.
    - fit_params: Optional dictionary of fit parameters (e.g., sample weights) to be passed during model training.
    - cv: The number of cross-validation folds (default is 5).

    Returns:
    - The best model found by GridSearchCV.
    - The best hyperparameters.
    """
    
    # Create a pipeline with standard scaling and the given model
    pipeline = make_pipeline(StandardScaler(), model)
    
    # Perform GridSearchCV
    grid_search = GridSearchCV(pipeline, param_grid, cv=cv, n_jobs=-1, verbose=1)
    
    # Fit the model with GridSearchCV
    grid_search.fit(dataset.features, dataset.labels.ravel(), **(fit_params or {}))
    
    # Return the best model and the best parameters
    return grid_search.best_estimator_, grid_search.best_params_

