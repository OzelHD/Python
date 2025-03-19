import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
from fractions import Fraction

def inverse_matrix(matrix):
    try:
        np_matrix = np.array(matrix, dtype=float)
        inv_matrix = np.linalg.inv(np_matrix)
        
        # Convert to fractions for display
        frac_matrix = [[Fraction(inv_matrix[i, j]).limit_denominator() for j in range(len(inv_matrix))] for i in range(len(inv_matrix))]
        return frac_matrix
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "The given matrix is singular and cannot be inverted.")
        return None

def get_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = simpledialog.askfloat("Input", f"Enter value for matrix[{i+1}][{j+1}]:")
            row.append(value)
        matrix.append(row)
    return matrix

def main():
    root = tk.Tk()
    root.withdraw() 
    
    n = simpledialog.askinteger("Matrix Size", "Enter the size of the nxn matrix:")
    if n is None or n <= 0:
        messagebox.showerror("Error", "Invalid matrix size.")
        return
    
    matrix = get_matrix(n)
    inv_matrix = inverse_matrix(matrix)
    
    if inv_matrix is not None:
        result_str = "\n".join(["\t".join(map(str, row)) for row in inv_matrix])
        messagebox.showinfo("Result", f"Inverse:\n{result_str}")

if __name__ == "__main__":
    main()
