from conexion import Conexion

class Boleta(Conexion):
    def __init__(self, cliente, usuario):
        super().__init__()
        self.cliente = cliente
        self.usuario = usuario

    def guardar(self):
        try:
            sql = "INSERT INTO boleta (cliente, usuario) VALUES (:1, :2)"
            datos = (self.cliente, self.usuario)
            self.cursor.execute(sql, datos)
            self.con.commit()
            print("Boleta guardada correctamente.")
        except Exception as e:
            print("Error deal guardar boleta:", e)
