from db_conexion import conexion


def crear_producto(NombreProducto, Stock, PrecioCompra, PrecioVenta):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO productos (NombreProducto, Stock, PrecioCompra, PrecioVenta) VALUES (%s, %s, %s, %s)", (NombreProducto, Stock, PrecioCompra, PrecioVenta))
    db.commit()
    db.close()


def mostrar_productos():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY IDProducto DESC")
    result = cursor.fetchall()
    db.close()
    return result


def mostrar_producto(IDProducto):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM productos WHERE IDProducto = '{IDProducto}'")
    result = cursor.fetchone()
    db.close()
    return result


def editar_producto(IDProducto, NombreProducto, Stock, PrecioCompra, PrecioVenta):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE productos SET NombreProducto='{NombreProducto}', Stock='{Stock}', PrecioCompra='{PrecioCompra}', PrecioVenta='{PrecioVenta}' WHERE IDProducto='{IDProducto}'")
    db.commit()
    db.close()


def eliminar_producto(IDProducto):
    db = conexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE IDProducto=%s", (IDProducto,))
    db.commit()
    db.close()
