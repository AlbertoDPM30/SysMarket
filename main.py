import sys
import os
import tkinter as tk
from modulos import productos, movimientos, proveedores, ventas, clientes, cierres_financieros

from tkinter import font
import db_conexion as conexion


def resource_path(relative_path):
    """ Obtén la ruta absoluta del recurso empaquetado. """
    if hasattr(sys, '_MEIPASS'):
        # _MEIPASS es la ruta temporal donde PyInstaller desempaqueta recursos
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def show_module(frame, module_func, rol):
    for widget in frame.winfo_children():
        widget.destroy()
    module_func(frame, rol)


def status_db():
    try:
        if conexion.conexion():
            return True

    except:
        return False


def menu_principal(usuario_actual, rol_usuario_actual, logeado):
    # from login import estado_sesion
    # usuario_actual, rol_usuario_actual, logeado = estado_sesion()
    print(f"::::log:::: {logeado}")
    print(f"::::usuario:::: {usuario_actual}")
    print(f"::::rol:::: {rol_usuario_actual}")

    window = tk.Tk()
    window.title("SysMarket")
    window.geometry("1024x720")
    window.state('zoomed')

    fuente_personalizada = font.Font(family="Helvetica", size=14)
    window.option_add("*Font", fuente_personalizada)

    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=1)
    main_frame.grid_columnconfigure(0, weight=1)

    titulo = tk.Label(main_frame, text="Bienvenido/a SysMarket",
                      font=("Verdana", 22, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    if status_db() == True:
        tk.Label(main_frame, text="Conexión establecida", font=(
            "Helvetica", 11, "normal"), fg="green").grid(row=1, column=0, pady=50)
        # Colocar la imagen dentro del marco
        imagen_tk = tk.PhotoImage(file=resource_path("public/back.png"))
        etiqueta_imagen = tk.Label(main_frame, image=imagen_tk)
        # Evitar que la imagen sea recolectada por el recolector de basura
        etiqueta_imagen.image = imagen_tk
        etiqueta_imagen.grid(row=2, column=0, padx=0, pady=2)
    else:
        tk.Label(main_frame, text="Existe un problema con la conexion, verifique lo siguiente:", font=(
            "Helvetica", 11, "bold"), fg="red").grid(row=1, column=0, pady=50)
        tk.Label(main_frame, text="-> Servicio MySQL desconectado o Puerto diferente a 3306", font=(
            "Helvetica", 10, "normal"), fg="black").grid(row=2, column=0, pady=5)
        tk.Label(main_frame, text="-> Nombre de la base de datos, debe llamarse \"mercado\"", font=(
            "Helvetica", 10, "normal"), fg="black").grid(row=3, column=0, pady=5)
        tk.Label(main_frame, text="-> Credenciales del servidor MySQL, no predeterminados", font=(
            "Helvetica", 10, "normal"), fg="black").grid(row=4, column=0, pady=5)

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.TOP)

    if rol_usuario_actual == "administrador":
        btn_clientes = tk.Button(button_frame, text="Clientes", command=lambda: show_module(
            main_frame, clientes.modulo_clientes, rol_usuario_actual),
            font=("Verdana", 16, "bold"),
            bg="#4A74CE",
            fg="#FFFFFF",
            activebackground="#2055CA",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=2,
            padx=20,
            pady=10)
        btn_clientes.pack(side=tk.LEFT, padx=5, pady=5)

        btn_proveedores = tk.Button(button_frame, text="Proveedores", command=lambda: show_module(
            main_frame, proveedores.modulo_proveedores, rol_usuario_actual),
            font=("Verdana", 16, "bold"),
            bg="#4A74CE",
            fg="#FFFFFF",
            activebackground="#2055CA",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=2,
            padx=20,
            pady=10)
        btn_proveedores.pack(side=tk.LEFT, padx=5, pady=5)

        btn_movimientos = tk.Button(button_frame, text="Movimientos", command=lambda: show_module(
            main_frame, movimientos.modulo_movimientos, rol_usuario_actual),
            font=("Verdana", 16, "bold"),
            bg="#4A74CE",
            fg="#FFFFFF",
            activebackground="#2055CA",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=2,
            padx=20,
            pady=10)
        btn_movimientos.pack(side=tk.LEFT, padx=5, pady=5)

        btn_cierres_financieros = tk.Button(button_frame, text="Cierres Financieros", command=lambda: show_module(
            main_frame, cierres_financieros.modulo_cierres_financieros, rol_usuario_actual),
            font=("Verdana", 16, "bold"),
            bg="#4A74CE",
            fg="#FFFFFF",
            activebackground="#2055CA",
            activeforeground="#FFFFFF",
            relief="raised",
            bd=2,
            padx=20,
            pady=10)
        btn_cierres_financieros.pack(side=tk.LEFT, padx=5, pady=5)

    btn_productos = tk.Button(button_frame, text="Productos", command=lambda: show_module(
        main_frame, productos.modulo_productos, rol_usuario_actual),
        font=("Verdana", 16, "bold"),
        bg="#4A74CE",
        fg="#FFFFFF",
        activebackground="#2055CA",
        activeforeground="#FFFFFF",
        relief="raised",
        bd=2,
        padx=20,
        pady=10)
    btn_productos.pack(side=tk.LEFT, padx=5, pady=5)

    btn_ventas = tk.Button(button_frame, text="Procesar Venta", command=lambda: show_module(
        main_frame, ventas.modulo_ventas, rol_usuario_actual),
        font=("Verdana", 16, "bold"),
        bg="#4A74CE",
        fg="#FFFFFF",
        activebackground="#2055CA",
        activeforeground="#FFFFFF",
        relief="raised",
        bd=2,
        padx=20,
        pady=10)
    btn_ventas.pack(side=tk.LEFT, padx=5, pady=5)

    window.mainloop()


# if __name__ == "__main__":
#     menu_principal()
