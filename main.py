from inventario import Inventario
from habitacion import Habitacion
from cliente import Cliente
from recepcionista import Recepcionista
from boleta import Boleta

def main():
    print("=== Sistema de Hotel (Acumulativa 3) ===")

    inventario = Inventario("Jabón", "Limpieza", 100, 250)
    inventario.guardar()

    habitacion = Habitacion(101, 2, "Disponible")
    habitacion.guardar()

    cliente = Cliente("Juan Pérez", "912345678", "Chilena", "101")
    cliente.guardar()

    recep = Recepcionista("Ana López", "987654321", "Recepción principal")
    recep.guardar()

    boleta = Boleta("Juan Pérez", "Ana López")
    boleta.guardar()

if __name__ == "__main__":
    main()
