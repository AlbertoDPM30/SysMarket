from db_conexion import conexion


def crear_venta(DetallesVenta, TotalVenta, TotalBS, IDCliente):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO ventas (DetallesVenta, TotalVenta, TotalBS, IDCliente) VALUES (%s, %s, %s, %s)", (DetallesVenta, TotalVenta, TotalBS, IDCliente))
    db.commit()
    db.close()


def mostrar_ventas():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT v.IDVenta, v.DetallesVenta, v.TotalVenta, v.TotalBS, c.Nombres, c.Apellidos, c.CI_RIF FROM ventas as v LEFT JOIN clientes as c ON v.IDCliente = c.IDCliente ORDER BY v.IDVenta DESC")
    result = cursor.fetchall()
    db.close()
    return result


def mostrar_recibo(IDVenta):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"SELECT v.IDVenta, v.DetallesVenta, v.TotalVenta, v.TotalBS, c.Nombres, c.Apellidos, c.CI_RIF FROM ventas as v LEFT JOIN clientes as c ON v.IDCliente = c.IDCliente WHERE v.IDVenta = '{IDVenta}'")
    result = cursor.fetchone()
    db.close()
    return result


def editar_venta(IDVenta, DetallesVenta, TotalVenta, TotalBS):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE ventas SET DetallesVenta='{DetallesVenta}', TotalVenta='{TotalVenta}', TotalBS = '{TotalBS}' WHERE IDVenta='{IDVenta}'")
    db.commit()
    db.close()


def eliminar_venta(IDVenta):
    db = conexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM ventas WHERE IDVenta=%s", (IDVenta,))
    db.commit()
    db.close()
