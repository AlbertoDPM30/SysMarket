from db_conexion import conexion


def crear_cliente(Nombres, Apellidos, CI_RIF):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO clientes (Nombres, Apellidos, CI_RIF) VALUES (%s, %s, %s)", (Nombres, Apellidos, CI_RIF))
    db.commit()
    db.close()


def mostrar_clientes():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY IDCliente DESC")
    result = cursor.fetchall()
    db.close()
    return result


def mostrar_cliente(CI_RIF):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM clientes WHERE CI_RIF = '{CI_RIF}'")
    result = cursor.fetchone()
    db.close()
    return result


def editar_cliente(IDCliente, Nombres, Apellidos, CI_RIF):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE clientes SET Nombres='{Nombres}', Apellidos='{Apellidos}', CI_RIF='{CI_RIF}' WHERE IDCliente='{IDCliente}'")
    db.commit()
    db.close()


def eliminar_cliente(IDCliente):
    db = conexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM clientes WHERE IDCliente=%s", (IDCliente,))
    db.commit()
    db.close()
