import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    X = np.array(list).reshape(3, 3)
    result = {
        'mean': [
            np.mean(X, axis=0).tolist(),
            np.mean(X, axis=1).tolist(),
            np.mean(X).item()
        ],
        'variance': [
            np.var(X, axis=0).tolist(),
            np.var(X, axis=1).tolist(),
            np.var(X).item()
        ],
        'standard deviation': [
            np.std(X, axis=0).tolist(),
            np.std(X, axis=1).tolist(),
            np.std(X).item()
        ],
        'max': [
            np.max(X, axis=0).tolist(),
            np.max(X, axis=1).tolist(),
            np.max(X).item()
        ],
        'min': [
            np.min(X, axis=0).tolist(),
            np.min(X, axis=1).tolist(),
            np.min(X).item()
        ],
        'sum': [
            np.sum(X, axis=0).tolist(),
            np.sum(X, axis=1).tolist(),
            np.sum(X).item()
        ]
    }
    return result