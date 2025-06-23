import tkinter as tk
from tkinter import messagebox
from modelos import usuarios_modelo


USUARIO_ACTUAL = None
ROL_USUARIO_ACTUAL = None
LOGEADO = False


def estado_sesion():
    return USUARIO_ACTUAL, ROL_USUARIO_ACTUAL, LOGEADO


def iniciar_sesion():

    global USUARIO_ACTUAL, ROL_USUARIO_ACTUAL, LOGEADO

    usuario = usuario_entry.get()
    password = password_entry.get()

    login = usuarios_modelo.login_usuario(usuario, password)

    if login:
        USUARIO_ACTUAL = login[1]
        ROL_USUARIO_ACTUAL = login[3]
        LOGEADO = True
        ventana.destroy()
        from main import menu_principal
        menu_principal(USUARIO_ACTUAL, ROL_USUARIO_ACTUAL, LOGEADO)
    else:
        USUARIO_ACTUAL = None
        ROL_USUARIO_ACTUAL = None
        LOGEADO = False
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


if __name__ == "__main__":

    ventana = tk.Tk()
    ventana.title("iniciar Sesión")

    # Etiqueta y campo para el nombre de usuario
    tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
    usuario_entry = tk.Entry(ventana)
    usuario_entry.grid(row=0, column=1, padx=10, pady=10)

    # Etiqueta y campo para la contraseña
    tk.Label(ventana, text="Contraseña:").grid(
        row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(ventana, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Botón para iniciar sesión
    boton_login = tk.Button(ventana, text="Iniciar sesión",
                            command=iniciar_sesion)
    boton_login.grid(row=2, column=0, columnspan=2, pady=10)

    ventana.mainloop()
