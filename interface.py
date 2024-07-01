import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib import pyplot as plt
from plotter import create_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def save_graph(entry, canvas):
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filename:
        try:
            fig = create_plot(entry.get())
            fig.savefig(filename)
            messagebox.showinfo("Success", "Graph saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the graph: {e}")

# interface.py içerisindeki show_graph fonksiyonu güncelleme
def show_graph(entry, canvas):
    try:
        fig = create_plot(entry.get())  # create_plot artık 3D grafik oluşturacak
        canvas.figure = fig
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Could not display the graph: {e}")

def start_interface():
    root = tk.Tk()
    root.title("3D Function Plotter")
    root.geometry("400x700")  # Adjust size to accommodate plot and controls

    label = tk.Label(root, text="Enter your equation:")
    label.pack(pady=(20, 5))

    equation_entry = tk.Entry(root, width=40)
    equation_entry.pack()

    # Set up the matplotlib figure and canvas
    fig, ax = plt.subplots(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)  # Create a canvas widget
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    show_button = tk.Button(root, text="Show Graph", command=lambda: show_graph(equation_entry, canvas), bg="#FF6347")
    show_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Graph", command=lambda: save_graph(equation_entry, canvas), bg="#6495ED")
    save_button.pack(pady=(5, 20))

    root.mainloop()
