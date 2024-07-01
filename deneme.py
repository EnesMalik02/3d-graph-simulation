import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Veri noktalarını oluştur
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Grafik çizimi için figür ve eksenleri hazırla
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Yüzey grafiğini çiz
ax.plot_surface(x, y, z, cmap='viridis')

# Eksenlerin grafik boyutunu en iyi şekilde doldurmasını sağla
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)  # Kenar boşluklarını ayarla

# Etiketler ve başlık
ax.set_xlabel('X koordinatı')
ax.set_ylabel('Y koordinatı')
ax.set_zlabel('Z koordinatı')
ax.set_title('3D Yüzey Grafiği: z = x^2 + y^2')

# Grafik penceresini dolduracak şekilde ayarla
plt.tight_layout(pad=0)

# Göster
plt.show()
