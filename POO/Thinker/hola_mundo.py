import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo('Click', 'Hola Mundo')

ventana = tk.Tk()
ventana.title('Hola mundo')
ventana.geometry('250x200')

tk.Label(ventana, text='Hola Mundo', font=('Arial', 23)).pack(pady=45)
tk.Button(ventana, text='click', command=saludar).pack()

ventana.mainloop()