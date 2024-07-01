import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotter import create_plot
import matplotlib.pyplot as plt

def clear_graph(canvas, ax):
    ax.cla()  # Mevcut eksenleri temizle
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    canvas.draw()  # Canvas'ı yeniden çiz

def save_graph(entry, canvas):
    filetypes = [("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("PDF files", "*.pdf"), ("All files", "*.*")]
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)
    if filename:
        try:
            fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
            X, Y, Z = create_plot(entry.get())
            ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', shade=True)
            fig.savefig(filename)
            messagebox.showinfo("Success", "Graph saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the graph: {e}")

def show_graph(entry, canvas, ax):
    try:
        ax.cla()
        X, Y, Z = create_plot(entry.get())
        ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', shade=True)
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
    
    style = ttk.Style()
    style.theme_use('clam')  # Modern tema kullanımı
    
    label = ttk.Label(root, text="Enter your equation:")
    label.pack(pady=(20, 5))
    
    equation_entry = ttk.Entry(root, width=40)
    equation_entry.pack()
    
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    show_button = ttk.Button(root, text="Show Graph", command=lambda: show_graph(equation_entry, canvas, ax))
    show_button.pack(pady=5)
    
    clear_button = ttk.Button(root, text="Clear Graph", command=lambda: clear_graph(canvas, ax))
    clear_button.pack(pady=5)
    
    save_button = ttk.Button(root, text="Save Graph", command=lambda: save_graph(equation_entry, canvas))
    save_button.pack(pady=(5, 20))
    
    root.mainloop()

if __name__ == "__main__":
    start_interface()
