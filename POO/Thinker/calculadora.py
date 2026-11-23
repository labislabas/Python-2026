import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from datetime import datetime, date

# ---------- Funciones ----------

def calcular_edad(texto_fecha_nacimiento):
    try:
        fecha_nacimiento = datetime.strptime(texto_fecha_nacimiento, "%d/%m/%Y").date()
    except ValueError:
        return None

    fecha_hoy = date.today()
    edad = fecha_hoy.year - fecha_nacimiento.year

    if (fecha_hoy.month, fecha_hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad = edad - 1

    if edad < 0 or edad > 120:
        return None
    return edad


def actualizar_edad_en_pantalla(evento=None):
    edad_calculada = calcular_edad(campo_fecha_nacimiento.get().strip())
    if edad_calculada is None:
        etiqueta_edad.config(text="---")
    else:
        etiqueta_edad.config(text=f"{edad_calculada} años")


def limpiar_formulario():
    for campo in (campo_rut, campo_nombres, campo_apellido_paterno, campo_apellido_materno,
                  campo_fecha_nacimiento, campo_peso, campo_altura,
                  campo_telefono_paciente, campo_telefono_emergencia):
        campo.delete(0, END)
    etiqueta_edad.config(text="---")


def registrar_paciente():
    rut = campo_rut.get().strip()
    nombres = campo_nombres.get().strip()
    apellido_paterno = campo_apellido_paterno.get().strip()
    apellido_materno = campo_apellido_materno.get().strip()
    texto_fecha_nacimiento = campo_fecha_nacimiento.get().strip()
    sexo = lista_sexo.get()
    peso = campo_peso.get().strip()

    # para campos obligatorios vacíos
    if rut == "" or nombres == "" or apellido_paterno == "" or texto_fecha_nacimiento == "":
        messagebox.showerror("Error", "Complete: RUT, Nombres, Apellido Paterno y Fecha de nacimiento.")
        return

    # para fecha inválida
    edad_del_paciente = calcular_edad(texto_fecha_nacimiento)
    if edad_del_paciente is None:
        messagebox.showerror("Error", "Fecha inválida. Use el formato dd/mm/aaaa (ejemplo: 25/03/2001).")
        return

    # [ara el peso, si se escribe, debe ser un número
    if peso != "" and not peso.replace(".", "", 1).isdigit():
        messagebox.showerror("Error", "El peso debe ser un número.")
        return

    if peso == "":
        peso_en_texto = "No indicado"
    else:
        peso_en_texto = peso + " kg"

    nombre_completo = nombres + " " + apellido_paterno + " " + apellido_materno

    tabla_pacientes.insert("", "end", values=(rut, nombre_completo, edad_del_paciente, sexo, peso_en_texto))
    messagebox.showinfo("Éxito", "Paciente registrado correctamente.")
    limpiar_formulario()


# ventana principal

ventana_principal = ttk.Window(themename="cosmo")
ventana_principal.title("Sistema de Gestión Médica - Módulo Pacientes")
ventana_principal.geometry("950x650")
ventana_principal.resizable(False, False)

marco_principal = ttk.Frame(ventana_principal, padding=15)
marco_principal.pack(fill=BOTH, expand=True)

ttk.Label(marco_principal, text="Gestión de Pacientes", font=("Helvetica", 16, "bold")).pack(anchor=W, pady=5)

# formulario

marco_formulario = ttk.Labelframe(marco_principal, text="Datos del Paciente", padding=15)
marco_formulario.pack(fill=X, pady=5)

# rut y nombres
ttk.Label(marco_formulario, text="RUT:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
campo_rut = ttk.Entry(marco_formulario, width=15)
campo_rut.grid(row=0, column=1, padx=5, pady=5, sticky=W)

ttk.Label(marco_formulario, text="Nombres:").grid(row=0, column=2, sticky=W, padx=5, pady=5)
campo_nombres = ttk.Entry(marco_formulario, width=22)
campo_nombres.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# apellidos
ttk.Label(marco_formulario, text="Apellido Paterno:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
campo_apellido_paterno = ttk.Entry(marco_formulario, width=15)
campo_apellido_paterno.grid(row=1, column=1, padx=5, pady=5, sticky=W)

ttk.Label(marco_formulario, text="Apellido Materno:").grid(row=1, column=2, sticky=W, padx=5, pady=5)
campo_apellido_materno = ttk.Entry(marco_formulario, width=22)
campo_apellido_materno.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# fecha de nacimiento y edad calculada
ttk.Label(marco_formulario, text="Fecha nac. (dd/mm/aaaa):").grid(row=2, column=0, sticky=W, padx=5, pady=5)
campo_fecha_nacimiento = ttk.Entry(marco_formulario, width=15)
campo_fecha_nacimiento.grid(row=2, column=1, padx=5, pady=5, sticky=W)
campo_fecha_nacimiento.bind("<KeyRelease>", actualizar_edad_en_pantalla)  # calcula la edad al escribir

ttk.Label(marco_formulario, text="Edad:").grid(row=2, column=2, sticky=W, padx=5, pady=5)
etiqueta_edad = ttk.Label(marco_formulario, text="---", font=("Helvetica", 11, "bold"))
etiqueta_edad.grid(row=2, column=3, padx=5, pady=5, sticky=W)

# sexo y peso
ttk.Label(marco_formulario, text="Sexo:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
lista_sexo = ttk.Combobox(marco_formulario, values=["Masculino", "Femenino"], width=12, state="readonly")
lista_sexo.grid(row=3, column=1, padx=5, pady=5, sticky=W)
lista_sexo.current(0)

ttk.Label(marco_formulario, text="Peso (kg):").grid(row=3, column=2, sticky=W, padx=5, pady=5)
campo_peso = ttk.Entry(marco_formulario, width=8)
campo_peso.grid(row=3, column=3, padx=5, pady=5, sticky=W)

# altura y contacto del paciente
ttk.Label(marco_formulario, text="Altura (m):").grid(row=4, column=0, sticky=W, padx=5, pady=5)
campo_altura = ttk.Entry(marco_formulario, width=8)
campo_altura.grid(row=4, column=1, padx=5, pady=5, sticky=W)

ttk.Label(marco_formulario, text="Contacto Paciente:").grid(row=4, column=2, sticky=W, padx=5, pady=5)
campo_telefono_paciente = ttk.Entry(marco_formulario, width=15)
campo_telefono_paciente.grid(row=4, column=3, padx=5, pady=5, sticky=W)

# contacto de emergencia y botón
ttk.Label(marco_formulario, text="Contacto Emergencia:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
campo_telefono_emergencia = ttk.Entry(marco_formulario, width=15)
campo_telefono_emergencia.grid(row=5, column=1, padx=5, pady=5, sticky=W)

boton_registrar = ttk.Button(marco_formulario, text="Registrar Paciente", bootstyle=SUCCESS,
                             command=registrar_paciente)
boton_registrar.grid(row=5, column=3, sticky=E, pady=10)

# Tabla

marco_tabla = ttk.Frame(marco_principal)
marco_tabla.pack(fill=BOTH, expand=True, pady=10)

ttk.Label(marco_tabla, text="Lista de Pacientes Registrados", font=("Helvetica", 12, "bold")).pack(anchor=W, pady=5)

columnas_tabla = ("rut", "nombre", "edad", "sexo", "peso")
tabla_pacientes = ttk.Treeview(marco_tabla, columns=columnas_tabla, bootstyle="primary", show="headings", height=8)

tabla_pacientes.heading("rut", text="RUT")
tabla_pacientes.heading("nombre", text="Nombre Completo")
tabla_pacientes.heading("edad", text="Edad")
tabla_pacientes.heading("sexo", text="Sexo")
tabla_pacientes.heading("peso", text="Peso")

tabla_pacientes.column("rut", width=110)
tabla_pacientes.column("nombre", width=220)
tabla_pacientes.column("edad", width=60)
tabla_pacientes.column("sexo", width=90)
tabla_pacientes.column("peso", width=80)

tabla_pacientes.pack(fill=BOTH, expand=True)

ventana_principal.mainloop()