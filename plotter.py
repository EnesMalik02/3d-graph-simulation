import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D grafik için gereklidir
import numpy as np
import sympy as sp

def create_plot(equation):
    # Tüm alfabeyi kapsayan semboller
    symbols = sp.symbols('a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:z')
    symbol_dict = {str(symbol): symbol for symbol in symbols}

    try:
        expr = sp.sympify(equation, locals=symbol_dict)
        used_symbols = sorted(expr.free_symbols, key=lambda sym: str(sym))
        func = sp.lambdify(used_symbols, expr, 'numpy')

        # Gerekli X ve Y değerlerini oluştur
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)

        # Eğer kullanılan değişkenler sadece x veya y içeriyorsa
        eval_dict = {str(symbol): 0 for symbol in symbols}
        eval_dict.update({'x': X, 'y': Y})

        # Denklemdeki değişkenleri uygun bir şekilde yerine koyarak Z değerini hesapla
        Z = func(*[eval_dict[str(sym)] if str(sym) in eval_dict else 0 for sym in used_symbols])

        # Figür ve 3D eksenler oluştur
        fig = plt.figure(figsize=(5, 4))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='viridis')

        # Eksen isimlerini ve sınırlarını ayarla
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_xlim([x.min(), x.max()])
        ax.set_ylim([y.min(), y.max()])
        ax.set_zlim([Z.min(), Z.max()])

        plt.colorbar(surf, shrink=0.5, aspect=5)

        return fig

    except Exception as e:
        print(f"Error processing the equation: {e}")
        raise e