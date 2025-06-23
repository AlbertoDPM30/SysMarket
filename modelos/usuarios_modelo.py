from db_conexion import conexion


def crear_usuario(usuario, password, rol):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO usuarios (usuario, password, rol) VALUES (%s, %s, %s)", (usuario, password, rol))
    db.commit()
    db.close()


def mostrar_usuarios():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios ORDER BY id DESC")
    result = cursor.fetchall()
    db.close()
    return result


def login_usuario(usuario, password):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND password = '{password}'")
    result = cursor.fetchone()
    db.close()
    return result


def mostrar_usuario(id):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE id = '{id}'")
    result = cursor.fetchone()
    db.close()
    return result


def editar_usuario(id, usuario, password, rol):
    db = conexion()
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE usuarios SET usuario='{usuario}', password='{password}', rol='{rol}' WHERE id='{id}'")
    db.commit()
    db.close()


def eliminar_usuario(id):
    db = conexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    db.commit()
    db.close()
