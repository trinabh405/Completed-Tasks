import tkinter as tk
from tkinter import messagebox
import numpy as np

def get_matrix_from_entry(entry):
    try:
        rows = entry.get("1.0", tk.END).strip().split('\n')
        matrix = [list(map(float, r.strip().split())) for r in rows]
        return np.array(matrix)
    except:
        messagebox.showerror("Error", "Invalid matrix input")
        return None

def add():
    m1 = get_matrix_from_entry(a)
    m2 = get_matrix_from_entry(b)
    if m1 is not None and m2 is not None:
        try:
            res.config(text=str(m1 + m2))
        except:
            messagebox.showerror("Error", "Matrix sizes do not match")

def sub():
    m1 = get_matrix_from_entry(a)
    m2 = get_matrix_from_entry(b)
    if m1 is not None and m2 is not None:
        try:
            res.config(text=str(m1 - m2))
        except:
            messagebox.showerror("Error", "Matrix sizes do not match")

def mul():
    m1 = get_matrix_from_entry(a)
    m2 = get_matrix_from_entry(b)
    if m1 is not None and m2 is not None:
        try:
            res.config(text=str(m1 @ m2))
        except:
            messagebox.showerror("Error", "Invalid matrix dimensions for multiplication")

def trans():
    m1 = get_matrix_from_entry(a)
    if m1 is not None:
        res.config(text=str(m1.T))

def det():
    m1 = get_matrix_from_entry(a)
    if m1 is not None:
        if m1.shape[0] == m1.shape[1]:
            res.config(text=str(np.linalg.det(m1)))
        else:
            messagebox.showerror("Error", "Determinant requires a square matrix")

# interface setiup
root = tk.Tk()
root.title("Matrix Tool")

tk.Label(root, text="Matrix A").grid(row=0, column=0)
tk.Label(root, text="Matrix B").grid(row=0, column=1)

a = tk.Text(root, height=6, width=25)
a.grid(row=1, column=0, padx=5, pady=5)
b = tk.Text(root, height=6, width=25)
b.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=sub).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=mul).grid(row=3, column=0)
tk.Button(root, text="Transpose A", command=trans).grid(row=3, column=1)
tk.Button(root, text="Determinant of A", command=det).grid(row=4, column=0)

tk.Label(root, text="Result:").grid(row=5, column=0, sticky="w")
res = tk.Label(root, text="", justify="left", wraplength=400)
res.grid(row=6, column=0, columnspan=2)

root.mainloop()
