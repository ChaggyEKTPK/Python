
#Funcion de añadir
def add_setting(configuracion, tupla):

    clave = tupla[0].lower()
    valor = tupla[1].lower()
    
    if clave in configuracion:
        return f"Setting '{clave}' already exists! Cannot add a new setting with this name."
    
    configuracion[clave] = valor
    return f"Setting '{clave}' added with value '{valor}' successfully!"

#Funcion de actualizar
def update_setting(configuracion, tupla):

    clave = tupla[0].lower()
    valor = tupla[1].lower()

    if clave not in configuracion:
        return f"Setting '{clave}' does not exist! Cannot update a non-existing setting."
    
    configuracion[clave] = valor
    return f"Setting '{clave}' updated to '{valor}' successfully!"

#funcion de borrar
def delete_setting(configuracion, key):

    claveLow = key.lower()

    if claveLow not in configuracion:
        return f"Setting not found!"
    
    del configuracion[claveLow]
    return f"Setting '{claveLow}' deleted successfully!"

#funcion de ver
def view_settings(configuracion):

    resultado = ''

    if not configuracion:
        return 'No settings available.'
    
    for clave, valor in configuracion.items():
        resultado += f"{clave.capitalize()}: {valor}\n"
    
    return "Current User Settings:\n" + resultado

test_settings = {
    "theme": "dark",
    "language": "spanish",
    "notifications": "enabled"
}