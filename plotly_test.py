import plotly.graph_objects as go
import numpy as np

# Veri noktalarını oluştur
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.sin(x ** 2 + y ** 2)

# Grafik çizimi
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Plotly 3D Yüzey Grafiği', autosize=False, width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))
fig.show()
