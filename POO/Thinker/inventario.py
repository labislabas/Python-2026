import ttkbootstrap as ttk

app = ttk.Window(themename ="cosmo")
tabla = ttk.Treeview(app, columns = ("prod", "stock"), show="headings")
tabla.heading("prod", text="Producto")
tabla.heading("stock", text="Stock")
tabla.insert("", "end", values=("Teclado mecánico",15))
tabla.pack(pady=16, padx=20)
ttk.Button(app, text="Agregar", bootstyle="success").pack(pady=8)
app.mainloop()
