from mayavi import mlab
import numpy as np
import numexpr as ne

def create_3d_plot(z_expression):
    """Verilen z ifadesine göre 3D yüzey grafiği oluşturur."""
    x, y = np.mgrid[-5:5:100j, -5:5:100j]  # x ve y için sabit aralık
    z = ne.evaluate(z_expression, local_dict={'x': x, 'y': y})  # ifadeyi değerlendir

    # Grafik çizimi
    mlab.figure(bgcolor=(1, 1, 1))
    mlab.surf(x, y, z, colormap='cool')
    mlab.show()

# Kullanıcı girişi
z_expression = input("z = f(x, y) fonksiyon ifadesini girin (örneğin: 'x**2 + y**3'): ")

# Grafiği oluştur
create_3d_plot(z_expression)
