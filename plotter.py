import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sympy as sp

def create_plot(equation):
    x, y = sp.symbols('x y')
    symbol_dict = {'x': x, 'y': y}

    try:
        expr = sp.sympify(equation, locals=symbol_dict)
        func = sp.lambdify([x, y], expr, 'numpy')

        x_vals = np.linspace(-10, 10, 100)
        y_vals = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = func(X, Y)

        if not isinstance(Z, np.ndarray):
            Z = np.full(X.shape, Z)

        return X, Y, Z
    except Exception as e:
        print(f"Error processing the equation: {e}")
        raise e
