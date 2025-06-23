from db_conexion import conexion


def crear_proveedor(NombreProveedor, DireccionProveedor, TelefonoProveedor):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO proveedores (NombreProveedor, DireccionProveedor, TelefonoProveedor) VALUES (%s, %s, %s)", (NombreProveedor, DireccionProveedor, TelefonoProveedor))
    db.commit()
    db.close()


def mostrar_proveedores():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM proveedores ORDER BY IDProveedor DESC")
    result = cursor.fetchall()
    db.close()
    return result


def editar_proveedor(IDProveedor, NombreProveedor, DireccionProveedor, TelefonoProveedor):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE proveedores SET NombreProveedor='{NombreProveedor}', DireccionProveedor='{DireccionProveedor}', TelefonoProveedor='{TelefonoProveedor}' WHERE IDProveedor='{IDProveedor}'")
    db.commit()
    db.close()


def eliminar_proveedor(IDProveedor):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM proveedores WHERE IDProveedor=%s", (IDProveedor,))
    db.commit()
    db.close()
