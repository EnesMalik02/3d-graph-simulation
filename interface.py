import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotter import create_plot
import matplotlib.pyplot as plt

def save_graph(entry, canvas):
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filename:
        try:
            fig, ax = create_plot(entry.get())
            fig.savefig(filename)
            messagebox.showinfo("Success", "Graph saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the graph: {e}")

def show_graph(entry, canvas, ax):
    try:
        # Mevcut eksenleri temizle
        ax.cla()

        # Yeni grafik verilerini al ve oluştur
        X, Y, Z = create_plot(entry.get())
        ax.plot_surface(X, Y, Z, cmap='viridis')

        # Eksenleri ve çizimi güncelle
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Could not display the graph: {e}")

def start_interface():
    root = tk.Tk()
    root.title("3D Function Plotter")
    root.geometry("700x700")

    label = tk.Label(root, text="Enter your equation:")
    label.pack(pady=(20, 5))

    equation_entry = tk.Entry(root, width=40)
    equation_entry.pack()

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    show_button = tk.Button(root, text="Show Graph", command=lambda: show_graph(equation_entry, canvas, ax), bg="#FF6347")
    show_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Graph", command=lambda: save_graph(equation_entry, canvas), bg="#6495ED")
    save_button.pack(pady=(5, 20))

    root.mainloop()

if __name__ == "__main__":
    start_interface()