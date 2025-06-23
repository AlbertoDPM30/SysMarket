from db_conexion import conexion


def crear_cierre_financiero(MovimientosCerrados, TotalCierre):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO cierres_financieros (MovimientosCerrados, TotalCierre) VALUES (%s, %s)", (MovimientosCerrados, TotalCierre))
    db.commit()
    db.close()


def mostrar_cierres_financieros():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM cierres_financieros ORDER BY IDCierre DESC")
    result = cursor.fetchall()
    db.close()
    return result


def sumar_cierres_finacieros():
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUM(TotalCierre) FROM cierres_financieros")
    result = cursor.fetchall()
    db.close()
    return result
