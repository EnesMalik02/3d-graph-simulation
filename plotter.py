import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_plot(equation):
    x, y = sp.symbols('x y')  # Semboller tanımlandı
    try:
        expr = sp.sympify(equation, locals={'x': x, 'y': y})  # Kullanıcı girdisi doğrulanıyor
        func = sp.lambdify([x, y], expr, 'numpy')  # Fonksiyona dönüştürülüyor
    except sp.SympifyError as e:
        raise ValueError(f"Invalid expression: {equation}") from e  # Hata yönetimi

    x_vals = np.linspace(-10, 10, 100)
    y_vals = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func(X, Y)
    return X, Y, Z
