# Inicialización de variables
reporte_participantes = "Listado de Participantes\n"  # Cadena para almacenar la lista de participantes
reporte_edades = "Listado de Edades\n"  # Cadena para almacenar las edades de los participantes
suma_edades = 0  # Acumulador para calcular el promedio de edades
contador = 0  # Contador para numeración de participantes
bandera = True  # Variable de control para el ciclo while

# Uso de diccionarios para almacenar datos de los participantes
registro_participantes = {} # Almacena los participantes, identificiandolos con una id

# Bucle para ingreso de datos
while bandera:
    participante = {} # Definimos el diccionario a emplear para ir almacenando los datos del participante

    print("\nIngrese la información del participante:")
    nombres = input("Nombres del participante: ").title()  # Se solicita el nombre del participante
    lenguaje = input("Lenguaje de programación favorito: ").title()  # Se solicita el lenguaje favorito
    edad = input("Edad del participante: ")  # Se solicita la edad del participante
    edad = int(edad)  # Conversión de la edad a entero
    nivel = input("Nivel de experiencia (Principiante, Intermedio, Avanzado): ").title()  # Se solicita el nivel de experiencia

    # Uso de listas para almacenar la información de cada participante
    contador = contador + 1  # Se incrementa el contador para numerar a los participantes

    '''
        NOTE: Establecemos una id constituida por el contador (numero del participante), primera y última inicial del nombre.

            Ejemplo:
                nombre -> sebastian | sn
                contador -> 1

                La id generada es: id_1sn
    '''
    id_user = "id_"+str(contador)+nombres[0]+nombres[len(nombres)-1]                                                                          
    participante.setdefault("nombre", nombres)  # Se almacena la información en el diccionario con un identificador, en este caso 'nombre' 
    participante.setdefault("edad", edad)  # Se almacena la información en el diccionario con un identificador, en este caso 'edad' 
    participante.setdefault("lenguaje", lenguaje)  # Se almacena la información en el diccionario con un identificador, en este caso 'lenguaje' 
    participante.setdefault("nivel", nivel)  # Se almacena la información en el diccionario con un identificador, en este caso 'nivel' 
    
    # Una vez tenemos la información del participante la implementamos en el diccionario principal 'registro_participantes' con su identificador establecido en la variable id_user
    registro_participantes.setdefault(id_user, participante)

    # Preguntar al usuario si desea continuar ingresando participantes
    continuar = input("¿Desea ingresar otro participante? (si/no): ")
    if continuar.lower() != "si":  # Si la respuesta no es "si", se termina el ciclo
        bandera = False

#TODO: Impresión del reporte final
for keys in registro_participantes:
    for data in registro_participantes[keys]:
        if data == "nombre":
            reporte_participantes += f"{registro_participantes[keys][data]} "
        elif data == "lenguaje":
            reporte_participantes += f"-{registro_participantes[keys][data]}- "
        elif data == "edad":
            reporte_participantes += f"edad {registro_participantes[keys][data]}, "
        elif data == "nivel":
            reporte_participantes += f"nivel {registro_participantes[keys][data]}"

    reporte_participantes += "\n" # Agregamos un salto de línea para el siguiente participante
    
print(reporte_participantes)

#TODO:  Impresión del reporte de edades
for keys in registro_participantes:
    for data in registro_participantes[keys]:
        if data!="edad":
            continue
        
        # Hacemos una conversión de tipos de datos: int a str
        reporte_edades += str(registro_participantes[keys][data])
    reporte_edades += "\n"

print(reporte_edades)

#TODO: Impresion del promedio de edades
if contador > 0:
    # Recorremos el registro de participantes y accedemos al indice 'edad' para obtener su valor e ir sumandolo en la variable 'suma_edades'
    for keys in registro_participantes:
        suma_edades += registro_participantes[keys]["edad"]
    # Cálculo de promedios de edad
    promedio_edades = suma_edades / contador   #Se calcula el promedio de edades
else:
    promedio_edades = 0

print(f"Promedio de edades: {promedio_edades:.1f}")  # Se imprime el promedio de edades
