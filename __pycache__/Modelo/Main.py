from Cliente import Cliente
from Adminsitrador import Administrador


Cliente1 = Cliente("Juan", "Perez", "juan@gmail.com", "1234", "37904222", 30)
Administrador1 = Administrador("Ana", "Admin", "ana@fitpal.com", "admin123", True)

print("Datos del Cliente:")
print(Cliente1.mostrarDatos())

print("\nDatos del Administrador:")
print(Administrador1.mostrarDatos()) 