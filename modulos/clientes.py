import tkinter.ttk as ttk
import tkinter as tk
from modelos import clientes_modelo


def modulo_clientes(frame, ROL_USUARIO_ACTUAL):

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de clientes",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X)
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(1, weight=1)
    form_frame.grid_columnconfigure(2, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)
    form_frame.grid_columnconfigure(4, weight=1)

    tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=10)
    Nombres_entry = tk.Entry(form_frame, width=50)
    Nombres_entry.grid(row=1, column=0, padx=10)

    tk.Label(form_frame, text="Apellidos:").grid(row=0, column=1, padx=10)
    Apellidos_entry = tk.Entry(form_frame, width=50)
    Apellidos_entry.grid(row=1, column=1, padx=10)

    tk.Label(form_frame, text="Tipo:").grid(row=0, column=2)
    Tipo_select = ttk.Combobox(
        form_frame, values=["V", "E", "J", "N", "P"], width=5)
    Tipo_select.grid(row=1, column=2, padx=10)
    Tipo_select.set("V")

    tk.Label(form_frame, text="CI / RIF:").grid(
        row=0, column=3, padx=10)
    CI_RIF_entry = tk.Entry(form_frame, width=50)
    CI_RIF_entry.grid(row=1, column=3, padx=10)

    IDCliente_tag = tk.Label(form_frame, text="ID:")
    IDCliente_entry = tk.Entry(form_frame, width=50)

    # Crear tabla
    table_frame = tk.Frame(frame)
    table_frame.pack(fill=tk.BOTH, expand=1)

    # Crear un estilo personalizado
    estilo = ttk.Style()
    estilo.theme_use("alt")
    estilo.configure("Treeview", font=("Verdana", 14), rowheight=30)
    estilo.configure("Treeview.Heading", font=("Verdana", 14, "bold"))
    estilo.configure("Treeview",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="white")
    estilo.map("Treeview",
               background=[("selected", "#5500bb")])

    cols = ("ID", "Nombres", "Apellidos", "CI / RIF")

    clientes_table = tk.ttk.Treeview(
        table_frame, columns=cols, show='headings')

    for i, col in enumerate(cols):
        clientes_table.heading(col, text=col)
        clientes_table.column(col, width=100, anchor="center", stretch=True)

    def cargar_tabla():
        for i, row in enumerate(clientes_modelo.mostrar_clientes()):
            if i % 2 == 0:
                clientes_table.insert("", tk.END, values=row, tags=("par",))
            else:
                clientes_table.insert("", tk.END, values=row, tags=("impar",))

    def refrescar_tabla():
        for item in clientes_table.get_children():  # Eliminar todas las filas existentes
            clientes_table.delete(item)
        cargar_tabla()

    cargar_tabla()

    # Configurar los colores para las etiquetas
    # Color para filas pares
    clientes_table.tag_configure("par", background="#B5D4F4")
    clientes_table.tag_configure("impar", background="#CBDFF3")

    clientes_table.pack(fill=tk.BOTH, expand=1)

    def limpiar_entradas():
        form_frame.grid_columnconfigure(4, weight=0)
        Nombres_entry.delete(0, tk.END)
        Apellidos_entry.delete(0, tk.END)
        CI_RIF_entry.delete(0, tk.END)
        IDCliente_entry.delete(0, tk.END)
        IDCliente_tag.grid_forget()
        IDCliente_entry.grid_forget()
        IDCliente_entry.config(state="normal")
        Nombres_entry.focus_set()
        btn_editar.grid_forget()
        btn_eliminar.grid_forget()
        add_button.grid(row=2, column=0, columnspan=1, padx=2, pady=10)

    def agregar_cliente():
        Nombres = Nombres_entry.get()
        Apellidos = Apellidos_entry.get()
        Tipo = Tipo_select.get()
        Documento = CI_RIF_entry.get()

        ci_rif = f"{Tipo}{Documento}"

        clientes_modelo.crear_cliente(
            Nombres, Apellidos, ci_rif)

        add_button.grid(row=2, column=0, columnspan=1, padx=2, pady=10)
        refrescar_tabla()
        limpiar_entradas()

    def editar_cliente():
        IDCliente = IDCliente_entry.get()
        Nombres = Nombres_entry.get()
        Apellidos = Apellidos_entry.get()
        Tipo = Tipo_select.get()
        Documento = CI_RIF_entry.get()

        ci_rif = f"{Tipo}{Documento}"

        clientes_modelo.editar_cliente(
            IDCliente, Nombres, Apellidos, ci_rif)
        add_button.grid(row=2, column=0, columnspan=1, padx=2, pady=10)
        refrescar_tabla()
        limpiar_entradas()

    def eliminar_cliente():
        IDCliente = IDCliente_entry.get()
        clientes_modelo.eliminar_cliente(IDCliente)
        refrescar_tabla()
        limpiar_entradas()

    # Función para mostrar las entradas cuando se selecciona un elemento
    def mostrar_entradas(event):
        seleccionado = clientes_table.focus()
        if seleccionado:
            valores = clientes_table.item(seleccionado, "values")
            limpiar_entradas()
            form_frame.grid_columnconfigure(4, weight=1)

            Nombres_entry.insert(0, valores[1])
            Apellidos_entry.insert(0, valores[2])
            CI_RIF_entry.insert(0, valores[3])

            add_button.grid_forget()
            btn_editar.grid(row=2, column=3, columnspan=1, padx=2, pady=10)
            btn_eliminar.grid(row=2, column=4, columnspan=1, padx=2, pady=10)

            IDCliente_tag.grid(row=0, column=4, padx=10)
            IDCliente_entry.grid(row=1, column=4, padx=10)
            IDCliente_entry.insert(0, valores[0])
            IDCliente_entry.config(state="readonly")

    # Vincular la selección de un elemento a la función
    clientes_table.bind("<<TreeviewSelect>>", mostrar_entradas)

    add_button = tk.Button(
        form_frame, text="Agregar Cliente +", bg="#26b135", command=agregar_cliente)
    add_button.grid(row=2, column=0, columnspan=2, padx=4, pady=10)

    btn_limpiar = tk.Button(
        form_frame, text="Limpiar todo |x|", bg="#dadada", command=limpiar_entradas)
    btn_limpiar.grid(row=2, column=2, columnspan=1, padx=4, pady=10)

    btn_editar = tk.Button(
        form_frame, text="Editar Cliente !", bg="#fbcf3a", command=editar_cliente)

    btn_eliminar = tk.Button(
        form_frame, text="Eliminar Cliente X", bg="#de3f1f", fg="#FFFFFF", command=eliminar_cliente)
