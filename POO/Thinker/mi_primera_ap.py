import ttkbootstrap as ttk
from ttkbootstrap.constants import*

ventana = ttk.Window(themename = "vapor")
ventana.title("Mi primera ap")
ventana.geometry("400x300")

etiqueta = ttk.Label(ventana, text="¡Hola! presiona el botòn", font=("Helvetica",14))
etiqueta.pack(pady=20)

boton = ttk.Button(ventana, text = "Aceptar" , bootstyle=SUCCESS)
boton.pack(pady=10)

boton_salir = ttk.Button(ventana, text = "Cancelar" , bootstyle = (DANGER, OUTLINE) )
boton_salir.pack(pady=10)

ventana.mainloop()

