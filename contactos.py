# Agenda de Contactos

contactos = []

def agregar_contacto():
    """Agregar un nuevo contacto a la agenda"""
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    
    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    contactos.append(contacto)
    print(f"✓ Contacto '{nombre}' agregado exitosamente")

def listar_contactos():
    """Listar todos los contactos"""
    if not contactos:
        print("No hay contactos en la agenda")
        return
    
    print("\n=== LISTA DE CONTACTOS ===")
    for i, contacto in enumerate(contactos, 1):
        print(f"\n{i}. {contacto['nombre']}")
        print(f"   Teléfono: {contacto['telefono']}")
        print(f"   Email: {contacto['email']}")

def buscar_contacto():
    """Buscar un contacto por nombre"""
    nombre_buscar = input("Ingrese el nombre a buscar: ").lower()
    encontrados = []
    
    for contacto in contactos:
        if nombre_buscar in contacto['nombre'].lower():
            encontrados.append(contacto)
    
    if not encontrados:
        print("No se encontraron contactos con ese nombre")
        return
    
    print(f"\n=== CONTACTOS ENCONTRADOS ({len(encontrados)}) ===")
    for i, contacto in enumerate(encontrados, 1):
        print(f"\n{i}. {contacto['nombre']}")
        print(f"   Teléfono: {contacto['telefono']}")
        print(f"   Email: {contacto['email']}")

def menu():
    """Mostrar el menú principal"""
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            listar_contactos()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
