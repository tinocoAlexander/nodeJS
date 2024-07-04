import requests

BASE_URL = 'http://localhost:5000'

def registrar_profesor(id_profesor, nombre, correo, direccion):
    url = f'{BASE_URL}/profesor/registrar'
    datos_profesor = {
        "id": id_profesor,
        "nombre": nombre,
        "correo": correo,
        "direccion": direccion
    }
    try:
        response = requests.post(url, json=datos_profesor)
        if response.status_code == 200:
            return True, "Profesor agregado exitosamente."
        else:
            return False, f"Error: {response.status_code}, {response.text}"
    except requests.exceptions.RequestException as e:
        return False, f"Error en la conexión: {str(e)}"

def obtener_profesor_por_id(id_profesor):
    url = f'{BASE_URL}/profesor/{id_profesor}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.content:
                return response.json()
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {str(e)}")
        return None
    except requests.exceptions.JSONDecodeError:
        print("Error al decodificar la respuesta JSON.")
        return None

def consultar_profesor():
    id_profesor = int(input("ID del profesor: "))
    profesor = obtener_profesor_por_id(id_profesor)
    if profesor:
        print(f"El profesor con ID {id_profesor} es:\n{profesor}")
    else:
        print('El profesor con ese ID no existe.')

def actualizar_profesor(id_profesor, nombre=None, correo=None, direccion=None):
    url = f'{BASE_URL}/profesor/modificar'
    datos_actualizados = {"id": id_profesor}
    if nombre:
        datos_actualizados['nombre'] = nombre
    if correo:
        datos_actualizados['correo'] = correo
    if direccion:
        datos_actualizados['direccion'] = direccion
    
    try:
        response = requests.put(url, json=datos_actualizados)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {str(e)}")
        return None

def modificar_profesor():
    id_profesor = int(input("ID del profesor a modificar: "))
    profesor = obtener_profesor_por_id(id_profesor)
    if profesor:
        print("Profesor encontrado, por favor ingresa los nuevos datos (deja en blanco para no modificar):")
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        direccion = input("Nueva dirección: ")
        
        resultado = actualizar_profesor(id_profesor, nombre=nombre or None, correo=correo or None, direccion=direccion or None)
        if resultado:
            print("Profesor modificado exitosamente:", resultado)
        else:
            print('Error al actualizar el profesor.')
    else:
        print('El profesor con ese ID no existe.')

def eliminar_profesor_por_id():
    id_profesor = int(input("ID del profesor a eliminar: "))
    url = f'{BASE_URL}/profesor/eliminar/{id_profesor}'
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print("Profesor eliminado exitosamente.")
        else:
            print(f'Error al eliminar el profesor: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {str(e)}")

def eliminar_profesor():
    eliminar_profesor_por_id()

def listar_profesores():
    url = f'{BASE_URL}/profesores'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            profesores = response.json()
            for profesor in profesores:
                print(profesor)
        else:
            print(f'Error al obtener los profesores: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {str(e)}")

def main():
    while True:
        print("Bienvenido a nuestro programa de control escolar.\nMenú de opciones:\n1. Agregar\n2. Consultar\n3. Modificar\n4. Eliminar\n5. Reportar\n6. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            id_profesor = int(input("ID: "))
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            registrar_profesor(id_profesor, nombre, correo, direccion)
        elif opcion == 2:
            consultar_profesor()
        elif opcion == 3:
            modificar_profesor()
        elif opcion == 4:
            eliminar_profesor()
        elif opcion == 5:
            listar_profesores()
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
