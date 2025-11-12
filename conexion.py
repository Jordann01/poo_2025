import oracledb

def conectar():
    try:
        conexion = oracledb.connect(
            user="root",          # 👈 cambia si tu usuario Oracle es distinto
            password="inacap",      # 👈 cambia tu contraseña de Oracle
            dsn="localhost:1521/XE" # 👈 usa el nombre del servicio de tu Oracle
        )
        print("!Conexión establecida con Oracle!")
        return conexion
    except Exception as e:
        print("Error de conexión!:", e)
        return None
