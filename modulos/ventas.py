import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
from modelos import ventas_modelo, productos_modelo, movimientos_modelo, clientes_modelo
from modulos import recibos
import main


def modulo_ventas(frame, ROL_USUARIO_ACTUAL):

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de Ventas",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Crear tabla
    table_frame = tk.Frame(frame)
    table_frame.pack(fill=tk.BOTH, expand=1)

    # Crear un estilo personalizado
    estilo = ttk.Style()
    estilo.theme_use("alt")
    estilo.configure("Treeview", font=("Verdana", 10), rowheight=25)
    estilo.configure("Treeview.Heading", font=("Verdana", 12, "bold"))
    estilo.configure("Treeview",
                     foreground="black",
                     rowheight=20,
                     fieldbackground="white")
    estilo.map("Treeview",
               background=[("selected", "#5500bb")])

    cols = ("ID", "Nombre", "Stock", "Precio Unit. $")

    product_table = tk.ttk.Treeview(table_frame, columns=cols, show='headings')

    product_table.heading(cols[0], text=cols[0])
    product_table.column(cols[0], width=35, anchor="e", stretch=True)

    product_table.heading(cols[1], text=cols[1])
    product_table.column(cols[1], width=400, anchor="w", stretch=True)

    product_table.heading(cols[2], text=cols[2])
    product_table.column(cols[2], width=75, anchor="e", stretch=True)

    product_table.heading(cols[3], text=cols[3])
    product_table.column(cols[3], width=150, anchor="e", stretch=True)

    # Crear tabla productos seleccionados
    cols = ("ID", "Nombre", "Cantidad",
            "Precio Unit. $", "precio $", "Precio BS")

    ventas_table = tk.ttk.Treeview(
        table_frame, columns=cols, show='headings')

    ventas_table.heading(cols[0], text=cols[0])
    ventas_table.column(cols[0], width=35, anchor="e", stretch=True)

    ventas_table.heading(cols[1], text=cols[1])
    ventas_table.column(cols[1], width=300, anchor="w", stretch=True)

    ventas_table.heading(cols[2], text=cols[2])
    ventas_table.column(cols[2], width=100, anchor="e", stretch=True)

    ventas_table.heading(cols[3], text=cols[3])
    ventas_table.column(cols[3], width=150, anchor="e", stretch=True)

    ventas_table.heading(cols[4], text=cols[4])
    ventas_table.column(cols[4], width=150, anchor="e", stretch=True)

    ventas_table.heading(cols[5], text=cols[5])
    ventas_table.column(cols[5], width=150, anchor="e", stretch=True)

    # Visualizar total a pagar
    total_frame = tk.Frame(frame)
    total_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(total_frame, text="Tasa BS:").pack(side=tk.LEFT, padx=5)
    TasaBS_entry = tk.Entry(total_frame, width=25)
    TasaBS_entry.pack(side=tk.LEFT, padx=10)

    PrecioTotal_entry = tk.Entry(total_frame, width=25)
    PrecioTotal_entry.pack(side=tk.RIGHT, padx=10)
    tk.Label(total_frame, text="Total $:").pack(side=tk.RIGHT, padx=5)

    PrecioTotalBS_entry = tk.Entry(total_frame, width=25)
    PrecioTotalBS_entry.pack(side=tk.RIGHT, padx=50)
    tk.Label(total_frame, text="Total BS:").pack(side=tk.RIGHT, padx=5)

    lista_productos_entry = tk.Entry(total_frame)

    # Añadir elementos de interfaz para las acciones
    cliente_frame = tk.Frame(frame)
    cliente_frame.pack(fill=tk.X, pady=10)
    cliente_frame.grid_columnconfigure(0, weight=1)
    cliente_frame.grid_columnconfigure(1, weight=1)
    cliente_frame.grid_columnconfigure(2, weight=1)
    cliente_frame.grid_columnconfigure(3, weight=1)
    cliente_frame.grid_columnconfigure(4, weight=1)
    cliente_frame.grid_columnconfigure(5, weight=1)

    tk.Label(cliente_frame, text="ID:").grid(
        row=0, column=0, padx=10)
    IDCliente_entry = tk.Entry(cliente_frame, width=10, state="readonly")
    IDCliente_entry.grid(row=1, column=0, padx=15)

    tk.Label(cliente_frame, text="Tipo CI / RIF:").grid(row=0, column=1)
    TipoDocumento_select = ttk.Combobox(
        cliente_frame, values=["V", "E", "J", "N", "P"], width=5)
    TipoDocumento_select.grid(row=1, column=1, padx=10)
    TipoDocumento_select.set("V")

    tk.Label(cliente_frame, text="CI / RIF:").grid(row=0, column=2, padx=10)
    DocumentoCliente_entry = tk.Entry(cliente_frame, width=25)
    DocumentoCliente_entry.grid(row=1, column=2, padx=10)

    tk.Label(cliente_frame, text="Nombres:").grid(row=0, column=3, padx=10)
    NombreCliente_entry = tk.Entry(cliente_frame, width=50, state="readonly")
    NombreCliente_entry.grid(row=1, column=3, padx=10)

    tk.Label(cliente_frame, text="Apellidos:").grid(row=0, column=4, padx=10)
    ApellidoCliente_entry = tk.Entry(cliente_frame, width=50, state="readonly")
    ApellidoCliente_entry.grid(row=1, column=4, padx=10)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X, pady=10)
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(1, weight=1)
    form_frame.grid_columnconfigure(2, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)
    form_frame.grid_columnconfigure(4, weight=1)

    tk.Label(form_frame, text="ID:").grid(
        row=0, column=0, padx=10)
    IDProducto_entry = tk.Entry(form_frame, width=25)
    IDProducto_entry.grid(row=1, column=0, padx=10)

    tk.Label(form_frame, text="Nombre:").grid(row=0, column=1, padx=10)
    NombreProducto_entry = tk.Entry(form_frame, width=75)
    NombreProducto_entry.grid(row=1, column=1, padx=10)

    tk.Label(form_frame, text="Cantidad:").grid(row=0, column=2, padx=10)
    Cantidad_entry = tk.Entry(form_frame, width=15)
    Cantidad_entry.grid(row=1, column=2, padx=10)

    tk.Label(form_frame, text="Precio Unit. $:").grid(
        row=0, column=3, padx=10)
    PrecioUnitario_entry = tk.Entry(form_frame, width=25)
    PrecioUnitario_entry.grid(row=1, column=3, padx=10)

    tk.Label(form_frame, text="Precio $:").grid(row=0, column=4, padx=10)
    Precio_entry = tk.Entry(form_frame, width=25)
    Precio_entry.grid(row=1, column=4, padx=10)

    # Funciones del modulo

    def cargar_tabla():
        for i, row in enumerate(productos_modelo.mostrar_productos()):
            tags = ("par",) if i % 2 == 0 else ("impar",)
            if row[2] < 5:  # Si el stock es menor a 5
                tags = ("rojo",)  # Añadir tag "rojo"
            product_table.insert("", tk.END, values=(
                row[0], row[1], row[2], row[4]), tags=tags)

    def refrescar_tabla():
        for item in product_table.get_children():  # Eliminar todas las filas existentes
            product_table.delete(item)
        cargar_tabla()

    cargar_tabla()

    # Configurar los colores para las etiquetas
    # Color para filas pares
    product_table.tag_configure("par", background="#B5D4F4")
    product_table.tag_configure("impar", background="#CBDFF3")
    # Color rojo para stock bajo
    product_table.tag_configure("rojo", background="#E96061")

    # product_table.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
    product_table.pack(fill=tk.BOTH, side=tk.LEFT, padx=15, pady=10, expand=1)
    ventas_table.pack(fill=tk.BOTH, side=tk.RIGHT, padx=15, pady=10, expand=1)

    lista_productos = {}

    def limpiar_entradas():
        IDProducto_entry.delete(0, tk.END)
        NombreProducto_entry.delete(0, tk.END)
        Cantidad_entry.delete(0, tk.END)
        PrecioUnitario_entry.delete(0, tk.END)
        Precio_entry.delete(0, tk.END)
        IDProducto_entry.config(state="normal")
        IDProducto_entry.focus_set()
        PrecioTotal_entry.delete(0, tk.END)
        PrecioTotalBS_entry.delete(0, tk.END)

    def cargar_producto():
        IDProducto = IDProducto_entry.get()
        NombreProducto = NombreProducto_entry.get()
        Cantidad = int(Cantidad_entry.get())
        PrecioUnitario = float(PrecioUnitario_entry.get())
        Precio = float(Precio_entry.get())
        PrecioBS = Precio * float(TasaBS_entry.get())

        seleccion = product_table.focus()
        producto_seleccionado = product_table.item(seleccion, "values")

        if Cantidad > int(producto_seleccionado[2]):
            return messagebox.showwarning("¡Alerta!", "Cantidad supera el Stock")

        ventas_table.insert("", tk.END, values=(
            IDProducto, NombreProducto, Cantidad, PrecioUnitario, Precio, PrecioBS), tag=("par",))

        lista_id = len(lista_productos) + 1

        lista_productos[lista_id] = {
            "IDProducto": IDProducto,
            "Nombre": NombreProducto,
            "Cantidad": Cantidad,
            "Precio Unit. $": PrecioUnitario,
            "Precio": Precio,
            "PrecioBS": PrecioBS
        }

        ventas_table.tag_configure("par", background="#B9F3C7")
        refrescar_tabla()
        limpiar_entradas()
        actualizar_total()

    def actualizar_total():
        total = sum(producto["Precio"]
                    for producto in lista_productos.values())
        PrecioTotal_entry.delete(0, tk.END)
        PrecioTotal_entry.insert(0, f"{total:.2f}")

        totalBS = sum(producto["PrecioBS"]
                      for producto in lista_productos.values())
        PrecioTotalBS_entry.delete(0, tk.END)
        PrecioTotalBS_entry.insert(0, f"{totalBS:.2f}")

    def limpiar_tabla():
        for item in ventas_table.get_children():
            ventas_table.delete(item)
        PrecioTotal_entry.delete(0, tk.END)

    def refrescar_pantalla(pantalla, modulo, rol):
        for widget in pantalla.winfo_children():
            widget.destroy()
        modulo(pantalla, rol)

    def buscar_cliente():
        ci = DocumentoCliente_entry.get()
        tipoDocumento = TipoDocumento_select.get()
        if not ci or not tipoDocumento:
            messagebox.showwarning(
                "Advertencia", "Por favor ingresa una CI o RIF.")
            return

        ci_completo = f"{tipoDocumento}{ci}"

        busquedaCliente = clientes_modelo.mostrar_cliente(ci_completo)

        if busquedaCliente:

            IDCliente_entry.config(state="normal")
            NombreCliente_entry.config(state="normal")
            ApellidoCliente_entry.config(state="normal")

            IDCliente_entry.delete(0, tk.END)
            NombreCliente_entry.delete(0, tk.END)
            ApellidoCliente_entry.delete(0, tk.END)

            IDCliente_entry.insert(0, busquedaCliente[0])
            NombreCliente_entry.insert(0, busquedaCliente[1])
            ApellidoCliente_entry.insert(0, busquedaCliente[2])

            IDCliente_entry.config(state="readonly")
            NombreCliente_entry.config(state="readonly")
            ApellidoCliente_entry.config(state="readonly")

            AgregarCliente_button.grid_forget()
        else:
            messagebox.showinfo(
                "Información", "Cliente no encontrado. Puedes crear un nuevo cliente.")

            IDCliente_entry.config(state="normal")
            NombreCliente_entry.config(state="normal")
            ApellidoCliente_entry.config(state="normal")

            IDCliente_entry.delete(0, tk.END)
            NombreCliente_entry.delete(0, tk.END)
            ApellidoCliente_entry.delete(0, tk.END)

            AgregarCliente_button.grid(row=1, column=6, padx=4)

    def nuevo_cliente():
        nombre_cliente = NombreCliente_entry.get()
        apellido_cliente = ApellidoCliente_entry.get()

        if not nombre_cliente or not apellido_cliente:
            messagebox.showwarning(
                "Advertencia", "Por favor ingresa todos los datos del nuevo cliente.")
            return

        ci = DocumentoCliente_entry.get()
        tipoDocumento = TipoDocumento_select.get()
        ci_completo = f"{tipoDocumento}{ci}"

        clientes_modelo.crear_cliente(
            nombre_cliente, apellido_cliente, ci_completo)

        busquedaCliente = clientes_modelo.mostrar_cliente(ci_completo)

        if busquedaCliente:
            IDCliente_entry.config(state="normal")
            IDCliente_entry.delete(0, tk.END)
            IDCliente_entry.insert(0, busquedaCliente[0])
            IDCliente_entry.config(state="disabled")

            NombreCliente_entry.config(state="disabled")
            ApellidoCliente_entry.config(state="disabled")
            AgregarCliente_button.grid_forget()

    def agregar_venta():
        lista_productos_entry.insert(0, lista_productos)
        DetallesVenta = lista_productos_entry.get()
        TotalVenta = float(PrecioTotal_entry.get())
        TotalBS = float(PrecioTotalBS_entry.get())

        IDCliente = int(IDCliente_entry.get())
        Nombres_cliente = NombreCliente_entry.get()
        Apellidos_cliente = ApellidoCliente_entry.get()
        Documento_cliente = DocumentoCliente_entry.get()
        TipoDoc = TipoDocumento_select.get()

        Documento = f"{TipoDoc} {Documento_cliente}"

        Cliente = f"{Documento}, {Nombres_cliente} {Apellidos_cliente}"

        ventas_modelo.crear_venta(
            DetallesVenta, TotalVenta, TotalBS, IDCliente)

        for producto_a_vender in ventas_table.get_children():
            valores = ventas_table.item(producto_a_vender, "values")
            valores_id = valores[0]
            valores_cantidad = int(valores[2])

            producto_obtenido = productos_modelo.mostrar_producto(
                valores_id)

            IDProducto = producto_obtenido[0]
            NombreProducto = producto_obtenido[1]
            Stock = int(producto_obtenido[2])
            PrecioCompra = producto_obtenido[3]
            PrecioVenta = producto_obtenido[4]

            nuevo_stock = (Stock - valores_cantidad)

            productos_modelo.editar_producto(
                IDProducto,
                NombreProducto,
                nuevo_stock,
                PrecioCompra,
                PrecioVenta
            )

        datos_venta = ventas_modelo.mostrar_ventas()[0][0]

        tipoMovimiento = "Ingreso"
        descripcion = f"Venta de Productos. No. Recibo: {datos_venta}, por cant.: {TotalVenta}"
        movimientos_modelo.crear_movimiento(
            tipoMovimiento, descripcion, TotalVenta, Cliente)

        refrescar_tabla()
        limpiar_entradas()
        actualizar_total()
        limpiar_tabla()
        lista_productos.clear()
        ventana_recibo = tk.Tk()
        recibos.modulo_recibo(ventana_recibo, datos_venta)
        refrescar_pantalla(frame, modulo_ventas, ROL_USUARIO_ACTUAL)

    def eliminar_producto_selecion():
        seleccionado = ventas_table.focus()

        if seleccionado:
            # Obtener los valores del producto seleccionado
            valores = ventas_table.item(seleccionado, "values")
            # El ID del producto está en la primera columna
            id_producto = valores[0]

            # Eliminar el producto del diccionario
            if id_producto in [producto["IDProducto"] for producto in lista_productos.values()]:
                # Usamos list() para poder borrar mientras iteramos
                for key, producto in list(lista_productos.items()):
                    if producto["IDProducto"] == id_producto:
                        del lista_productos[key]

            # Eliminar el producto de la tabla
            ventas_table.delete(seleccionado)

            # Actualizar el total
            actualizar_total()

    def valor_precio(event):
        try:
            # Obtener valores de las entradas
            cantidad = int(Cantidad_entry.get()
                           ) if Cantidad_entry.get().isdigit() else 0
            precio = float(PrecioUnitario_entry.get()
                           ) if PrecioUnitario_entry.get() else 0.0

            # Calcular el total
            total = cantidad * precio

            # Actualizar la entrada de total
            Precio_entry.delete(0, tk.END)
            Precio_entry.insert(0, f"{total:.2f}")
        except ValueError:
            # Manejar casos de error (como caracteres no válidos)
            Precio_entry.delete(0, tk.END)
            Precio_entry.insert(0, "0.00")

    # Función para mostrar las entradas cuando se selecciona un elemento
    def mostrar_entradas(event):
        seleccionado_producto = product_table.focus()
        if seleccionado_producto:
            valores = product_table.item(seleccionado_producto, "values")

            if valores[2] == "0":
                return messagebox.showwarning("¡Alerta!", "Stock insuficiente.")

            limpiar_entradas()

            IDProducto_entry.insert(0, valores[0])
            NombreProducto_entry.insert(0, valores[1])
            Cantidad_entry.insert(0, 1)
            PrecioUnitario_entry.insert(0, valores[3])
            Precio_entry.insert(0, valores[3])

    def validar_tasa_existente(event):
        if TasaBS_entry.get() != "":
            add_button.grid(row=1, column=0, padx=4, pady=10)
        else:
            add_button.grid_forget()

    def mostrar_entradas_ventas(event):
        seleccionado = ventas_table.focus()
        if seleccionado:
            btn_eliminar.grid(row=1, column=2, columnspan=1, padx=4, pady=10)

    Cantidad_entry.bind("<KeyRelease>", valor_precio)
    TasaBS_entry.bind("<KeyRelease>", validar_tasa_existente)

    # Vincular la selección de un elemento a la función
    buttons_frame = tk.Frame(frame)
    buttons_frame.pack(fill=tk.X)
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)
    buttons_frame.grid_columnconfigure(3, weight=1)

    product_table.bind("<<TreeviewSelect>>", mostrar_entradas)
    ventas_table.bind("<<TreeviewSelect>>", mostrar_entradas_ventas)

    add_button = tk.Button(
        buttons_frame, text="Agregar Producto +", bg="#26b135", command=cargar_producto)
    # add_button.grid(row=1, column=0, padx=4, pady=10)

    btn_limpiar = tk.Button(
        buttons_frame, text="Limpiar todo |X|", bg="#dadada", command=limpiar_entradas)
    btn_limpiar.grid(row=1, column=1, padx=4, pady=10)

    btn_eliminar = tk.Button(
        buttons_frame, text="Eliminar Producto X", bg="#de3f1f", fg="#FFFFFF", command=eliminar_producto_selecion)

    sell_button = tk.Button(
        buttons_frame, text="Generar Recibo |=|",  bg="#28c3d9", command=agregar_venta)
    sell_button.grid(row=1, column=3, padx=4, pady=10)

    # Botones de acciones de cliente
    buscarCliente_button = tk.Button(
        cliente_frame, text="Buscar", bg="#64D595", width=15, command=buscar_cliente)
    buscarCliente_button.grid(row=1, column=5, padx=4)

    AgregarCliente_button = tk.Button(
        cliente_frame, text="Agregar", bg="#28c3d9", width=15, command=nuevo_cliente)
