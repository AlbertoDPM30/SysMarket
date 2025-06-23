from db_conexion import conexion


def crear_movimiento(TipoMovimiento, DescripcionMovimiento, CantidadMovimiento, Cliente):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO movimientos (TipoMovimiento, DescripcionMovimiento, CantidadMovimiento, Cliente) VALUES (%s, %s, %s, %s)", (TipoMovimiento, DescripcionMovimiento, CantidadMovimiento, Cliente))
    db.commit()
    db.close()


def mostrar_movimientos():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM movimientos WHERE status = 1 ORDER BY IDMovimiento DESC")
    result = cursor.fetchall()
    db.close()
    return result


def mostrar_movimiento(IDMovimiento):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM movimientos WHERE status = 1 AND IDMovimiento = '{IDMovimiento}'")
    result = cursor.fetchone()
    db.close()
    return result


def sumar_movimientos():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUM(CantidadMovimiento) FROM movimientos WHERE status = 1")
    result = cursor.fetchall()
    db.close()
    return result


def mostrar_todos_movimientos():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM movimientos ORDER BY IDMovimiento DESC")
    result = cursor.fetchall()
    db.close()
    return result


def sumar_todos_movimientos():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUM(CantidadMovimiento) FROM movimientos")
    result = cursor.fetchall()
    db.close()
    return result


def cierre_movimientos(IDMovimiento):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE movimientos SET status = 0 WHERE IDMovimiento='{IDMovimiento}'")
    db.commit()
    db.close()
