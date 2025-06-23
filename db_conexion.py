import logging
import pymysql

logging.basicConfig(
    filename="db_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def conexion():
    try:
        logging.info("Intentando conectar a la base de datos usando PyMySQL.")
        conexion = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='mercado',
            port=3306
        )
        logging.info("Conexión exitosa a la base de datos.")
        return conexion
    except pymysql.MySQLError as err:
        logging.error(f"Error de conexión a MySQL con PyMySQL: {err}")
        return None
