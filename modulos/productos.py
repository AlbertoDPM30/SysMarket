import tkinter.ttk as ttk
import tkinter as tk
from modelos import productos_modelo, movimientos_modelo
from login import estado_sesion


def modulo_productos(frame, ROL_USUARIO_ACTUAL):

    # USUARIO_ACTUAL, ROL_USUARIO_ACTUAL, LOGEADO = estado_sesion()
    print(f"Rol actual ::::::: {ROL_USUARIO_ACTUAL}")

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de Productos",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X)
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(1, weight=1)
    form_frame.grid_columnconfigure(2, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)

    tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=10)
    NombreProducto_entry = tk.Entry(form_frame, width=50)
    NombreProducto_entry.grid(row=1, column=0, padx=10)

    tk.Label(form_frame, text="Stock:").grid(row=0, column=1, padx=10)
    Stock_entry = tk.Entry(form_frame, width=50)
    Stock_entry.grid(row=1, column=1, padx=10)

    tk.Label(form_frame, text="Precio Compra $:").grid(
        row=0, column=2, padx=10)
    PrecioCompra_entry = tk.Entry(form_frame, width=50, state="normal")
    PrecioCompra_entry.grid(row=1, column=2, padx=10)

    tk.Label(form_frame, text="Precio Venta $:").grid(row=0, column=3, padx=10)
    PrecioVenta_entry = tk.Entry(form_frame, width=50, state="readonly")
    PrecioVenta_entry.grid(row=1, column=3, padx=10)

    IDProducto_tag = tk.Label(form_frame, text="ID:")
    IDProducto_entry = tk.Entry(form_frame, width=50)

    # Crear tabla
    table_frame = tk.Frame(frame)
    table_frame.pack(fill=tk.BOTH, expand=1)

    # Crear un estilo personalizado
    estilo = ttk.Style()
    estilo.theme_use("alt")
    estilo.configure("Treeview", font=("Verdana", 14), rowheight=30)
    estilo.configure("statusCantidad.Treeview", background="red")
    estilo.configure("Treeview.Heading", font=("Verdana", 14, "bold"))
    estilo.configure("Treeview",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="white")
    estilo.map("Treeview",
               background=[("selected", "#5500bb")])

    cols = ("ID", "Nombre", "Stock", "Precio Compra $",
            "Precio Venta $", "Fecha Ingreso")

    product_table = tk.ttk.Treeview(table_frame, columns=cols, show='headings')

    for i, col in enumerate(cols):
        product_table.heading(col, text=col)
        product_table.column(col, width=100, anchor="center", stretch=True)

    def estilo_cantidad():
        for fila in product_table.get_children():
            valores = product_table.item(fila, "values")
            tags_existentes = product_table.item(fila, "tags")
            if int(valores[2]) == 5:
                if tags_existentes:
                    nueva_tags = "statusCantidad"
                    tags_actualizadas = list(tags_existentes)
                    if nueva_tags not in tags_actualizadas:
                        tags_actualizadas.append(nueva_tags)
                    product_table.item(fila, tags=tags_actualizadas)
                else:
                    product_table.item(fila, tags=("statusCantidad",))

    def cargar_tabla():
        for i, row in enumerate(productos_modelo.mostrar_productos()):
            if i % 2 == 0:
                product_table.insert("", tk.END, values=row, tags=("par",))
            else:
                product_table.insert("", tk.END, values=row, tags=("impar",))

    def refrescar_tabla():
        for item in product_table.get_children():  # Eliminar todas las filas existentes
            product_table.delete(item)
        cargar_tabla()

    cargar_tabla()
    estilo_cantidad()

    # Configurar los colores para las etiquetas
    # Color para filas pares
    product_table.tag_configure("par", background="#B5D4F4")
    product_table.tag_configure("impar", background="#CBDFF3")
    product_table.tag_configure("statusCantidad", background="#FF0022")

    product_table.pack(fill=tk.BOTH, expand=1)

    def limpiar_entradas():
        form_frame.grid_columnconfigure(4, weight=0)
        NombreProducto_entry.delete(0, tk.END)
        Stock_entry.delete(0, tk.END)
        PrecioCompra_entry.delete(0, tk.END)
        PrecioVenta_entry.config(state="normal")
        PrecioVenta_entry.delete(0, tk.END)
        PrecioVenta_entry.config(state="readonly")
        IDProducto_entry.config(state="normal")
        IDProducto_entry.delete(0, tk.END)
        IDProducto_tag.grid_forget()
        IDProducto_entry.grid_forget()
        NombreProducto_entry.focus_set()
        btn_editar.grid_forget()
        btn_eliminar.grid_forget()

    def calcular_incremento(event):
        PrecioVenta_entry.config(state="normal")
        valorCompra = float(PrecioCompra_entry.get())
        if valorCompra == None:
            PrecioVenta_entry.delete(0, tk.END)
            PrecioVenta_entry.insert(0, 0)

        totalPrecioVenta = valorCompra + (valorCompra * 0.3)
        PrecioVenta_entry.delete(0, tk.END)
        PrecioVenta_entry.insert(0, f"{totalPrecioVenta:.2f}")
        PrecioVenta_entry.config(state="readonly")

    def agregar_producto():
        NombreProducto = NombreProducto_entry.get()
        Stock = int(Stock_entry.get())
        PrecioCompra = float(PrecioCompra_entry.get())
        PrecioVenta = float(PrecioVenta_entry.get())
        productos_modelo.crear_producto(
            NombreProducto, Stock, PrecioCompra, PrecioVenta)

        tipoMovimiento = "Egreso"
        descripcion = f"Compra de Mercancia: {NombreProducto}, por cant.: {Stock}"
        totalCompra = (PrecioCompra * Stock)
        totalEgreso = -1 * totalCompra
        cliente = "SysMarket"
        movimientos_modelo.crear_movimiento(
            tipoMovimiento, descripcion, totalEgreso, cliente)
        refrescar_tabla()
        limpiar_entradas()

    def editar_producto():
        IDProducto = IDProducto_entry.get()
        NombreProducto = NombreProducto_entry.get()
        Stock = int(Stock_entry.get())
        PrecioCompra = float(PrecioCompra_entry.get())
        PrecioVenta = float(PrecioVenta_entry.get())

        productos_modelo.editar_producto(
            IDProducto, NombreProducto, Stock, PrecioCompra, PrecioVenta)
        refrescar_tabla()
        limpiar_entradas()

    def eliminar_producto():
        IDProducto = IDProducto_entry.get()
        productos_modelo.eliminar_producto(IDProducto)
        refrescar_tabla()
        limpiar_entradas()

    # Función para mostrar las entradas cuando se selecciona un elemento
    def mostrar_entradas(event):
        seleccionado = product_table.focus()
        if seleccionado:
            valores = product_table.item(seleccionado, "values")
            limpiar_entradas()
            form_frame.grid_columnconfigure(4, weight=1)

            NombreProducto_entry.insert(0, valores[1])
            Stock_entry.insert(0, valores[2])
            PrecioCompra_entry.insert(0, valores[3])
            PrecioVenta_entry.config(state="normal")
            PrecioVenta_entry.insert(0, valores[4])
            PrecioVenta_entry.config(state="readonly")

            if ROL_USUARIO_ACTUAL == "administrador":
                btn_editar.grid(row=2, column=3, columnspan=1, padx=2, pady=10)
                btn_eliminar.grid(
                    row=2, column=4, columnspan=1, padx=2, pady=10)

            IDProducto_tag.grid(row=0, column=4, padx=10)
            IDProducto_entry.grid(row=1, column=4, padx=10)
            IDProducto_entry.insert(0, valores[0])
            IDProducto_entry.config(state="readonly")

    # Vincular la selección de un elemento a la función
    PrecioCompra_entry.bind("<KeyRelease>", calcular_incremento)
    product_table.bind("<<TreeviewSelect>>", mostrar_entradas)

    if ROL_USUARIO_ACTUAL == "administrador":
        add_button = tk.Button(
            form_frame, text="Agregar Producto +", bg="#26b135", command=agregar_producto)
        add_button.grid(row=2, column=0, columnspan=2, padx=4, pady=10)

    btn_limpiar = tk.Button(
        form_frame, text="Limpiar todo |x|", bg="#dadada", command=limpiar_entradas)
    btn_limpiar.grid(row=2, column=2, columnspan=1, padx=4, pady=10)

    btn_editar = tk.Button(
        form_frame, text="Editar Producto !", bg="#fbcf3a", command=editar_producto)

    btn_eliminar = tk.Button(
        form_frame, text="Eliminar Producto X", bg="#de3f1f", fg="#FFFFFF", command=eliminar_producto)
