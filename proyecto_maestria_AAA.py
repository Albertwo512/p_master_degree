import speech_recognition as sr
import random
import matplotlib.pyplot as plt
import os
import streamlit as st



st.title('Programa para analisis de datos')
st.header('Listo..?')

start = False

def button_start():
    global start
    start = not start 

if st.button('Comenzar'):
    button_start()
print(start)


def speak(text):
    os.system(f"say {text}")

listener = sr.Recognizer()

nombres = []
apellidos_paternos = []
apellidos_maternos = []
localidades = ["Tequila", "Ameca", "Magdalena", "Amatitan", "Zapopan"]


if start == True:
    try:
        with sr.Microphone() as source:
            with st.spinner("Escuchando...."):
                for i in range (0, 2):
                # nombre
                    speak("Por favor dicte un nombre")
                    voice = listener.listen(source)  # listener objeto de la clase Recognizer de la biblioteca  speech_recognition, se usa para reconocer y escuchar la voz
                    rec_nombre = listener.recognize_google(voice)  # se utiliza para realizar el reconocimiento de voz utilizando el servicio de reconocimiento de voz de Google
                    st.write(f'Nombre escuchado {i}: ',rec_nombre)
                    nombres.append(rec_nombre)   # agregar a una lista de nombres la voz grabada
                    
                    # apellidos paternos
                    speak(f'Por favor dicte un apellido paterno de {rec_nombre}')
                    voice = listener.listen(source)
                    rec_apellidopaterno = listener.recognize_google(voice)
                    st.write(f'Apellido escuchado {i}: ',rec_apellidopaterno)
                    apellidos_paternos.append(rec_apellidopaterno)
                    
                    # apellidos maternos
                    speak(f'Por favor dicte un apellido materno de {rec_nombre}')
                    voice = listener.listen(source)
                    rec_apellidomaterno = listener.recognize_google(voice)
                    st.write(f'Apellido escuchado {i}: ',rec_apellidomaterno)
                    apellidos_maternos.append(rec_apellidomaterno)

                    st.write('Usuario agregado: ',i ,nombres[i],apellidos_paternos[i],apellidos_maternos[i])
                    st.success('Done!') 
        
            
            
    except Exception as e:
        st.write(f"Error: {e}")
        st.write('Algo salio mal')
        st.write(start)

    

    listadoejemplo = []  # declaro listado para guardar las tuplas

    for j in range (10000): # Rango de numero de listado
        ID =  j+1
        Nombre = random.choices(nombres) 
        Apellido_paterno = random.choices(apellidos_paternos) # devuelve una lista con el elemento seleccionado aleatoriamente
        Apellido_materno = random.choices(apellidos_maternos) 
        edad = random.randint(0, 100)
        peso = round(random.uniform(1,200),2) 
        localidad = random.choices(localidades) 
        tupla = (ID, Nombre[0], Apellido_paterno[0], Apellido_materno[0], edad, peso, localidad[0])
        listadoejemplo.append(tupla)
        
    print(tuple(listadoejemplo))

    #-----------------------------ejercicio 2 Estadísticas--------------------------------------------------------------------
    #-------------------------------Hermanos en la BD-----------------------------------------------------------------

    apellidos = {}
    hermanos = set()  # conjunto de elementos únicos para retornar los apellidos que se repiten

    # Recorrer las tuplas y buscar hermanos
    for tupla in listadoejemplo:
        apellido_paterno = tupla[2]
        apellido_materno = tupla[3]
        apellidosconcatenados = ' '.join([str(apellido_paterno), str(apellido_materno)])  # Concatenar apellido paterno y apellido materno
        
        if apellidosconcatenados in apellidos:
            apellidos[apellidosconcatenados] += 1  # agrego al diccionario la cantidad de apariciones de cada apellido para saber la cantidad de hermanos por cada apellidos iguales
            hermanos.add(apellidosconcatenados)
        else:
            apellidos[apellidosconcatenados] = 1

    # Obtener el número de hermanos encontrados
    num_hermanos = len(hermanos)

    # Filtrar los apellidos con un valor mayor que 1 
    apellidos_filtrados = {}
    for apellido, count in apellidos.items(): # itera a través de todos los elementos de un diccionario y desempaqueta los valores en las variables apellidos y count
        if count > 1:  # solo agregará los valores con más de una aparición
            apellidos_filtrados[apellido] = count

    st.header("Existen {} apellidos con hermanos en la base de datos".format(num_hermanos))
    st.write('Son los siguientes:',apellidos_filtrados)

    #-------------------------------FIN Hermanos en la BD-----------------------------------------------------------------
    #-------------------------ejercicios de homónimos------------------------------------------------------------------------

    homonimos = set()
    nombres_completos = set()

    # Recorrer las tuplas y buscar homónimos

    for tupla in listadoejemplo:
        nombre_completo = ' '.join([str(tupla[1]), str(tupla[2]), str(tupla[3])])  # Concatenar nombre, apellido paterno y apellido materno
        if nombre_completo in nombres_completos:
            homonimos.add(nombre_completo)
        else:
            nombres_completos.add(nombre_completo)

    print(homonimos)
    # Obtener el número de homónimos encontrados
    num_homonimos = len(homonimos)
    st.write("Existen {} homónimos en la base de datos".format(num_homonimos))

    #-------------------------ejercicios de histogramas------------------------------------------------------------------------
    listadoedad = []
    listadopesos = []

    # histograma por edades total
    for i in listadoejemplo:
        listadoedad.append(i[4])  # llenar una lista con todas las edades

    plt.hist(listadoedad, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades (total)")
    plt.savefig('listadoedad.png')
    st.image('listadoedad.png')
    plt.figure()
    
    # histograma por pesos total
    for i in listadoejemplo:
        listadopesos.append(i[5])  # llenar una lista con todos los pesos

    plt.hist(listadopesos, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos (total)")
    plt.savefig('listadopesos.png')
    st.image('listadopesos.png')
    plt.figure()

    # histograma edades/localidad

    # Crear un diccionario para almacenar las edades por localidad
    edades_por_localidad_Tequila = []
    edades_por_localidad_Ameca = []
    edades_por_localidad_Magdalena = []
    edades_por_localidad_Amatitan = []
    edades_por_localidad_Zapopan = []
    pesos_por_localidad_Tequila = []
    pesos_por_localidad_Ameca = []
    pesos_por_localidad_Magdalena = []
    pesos_por_localidad_Amatitan = []
    pesos_por_localidad_Zapopan = []

    for i in listadoejemplo:
        if i[6] == "Tequila":
            edades_por_localidad_Tequila.append(i[4])
            pesos_por_localidad_Tequila.append(i[5])
        elif i[6] == "Ameca":
            edades_por_localidad_Ameca.append(i[4])
            pesos_por_localidad_Ameca.append(i[5])
        elif i[6] == "Magdalena":
            edades_por_localidad_Magdalena.append(i[4])
            pesos_por_localidad_Magdalena.append(i[5])
        elif i[6] == "Amatitan":
            edades_por_localidad_Amatitan.append(i[4])
            pesos_por_localidad_Amatitan.append(i[5])
        else:
            edades_por_localidad_Zapopan.append(i[4])
            pesos_por_localidad_Zapopan.append(i[5])
    
    plt.figure()
    plt.hist(edades_por_localidad_Tequila, bins=60, color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Tequila")
    plt.savefig('edades_por_localidad_Tequila.png')
    st.image('edades_por_localidad_Tequila.png')
    plt.figure()

    plt.hist(pesos_por_localidad_Tequila, bins=60, color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Tequila")
    plt.savefig('pesos_por_localidad_Tequila.png')
    st.image('pesos_por_localidad_Tequila.png')
    plt.figure()

    plt.hist(edades_por_localidad_Ameca, bins=60, color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Ameca")
    plt.savefig('edades_por_localidad_Ameca.png')
    st.image('edades_por_localidad_Ameca.png')
    plt.figure()

    plt.hist(pesos_por_localidad_Ameca, bins=60, color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Ameca")
    plt.savefig('pesos_por_localidad_Ameca.png')
    st.image('pesos_por_localidad_Ameca.png')
    plt.figure()

    plt.hist(edades_por_localidad_Magdalena, bins=60,color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Magdalena")
    plt.savefig('edades_por_localidad_Magdalena.png')
    st.image('edades_por_localidad_Magdalena.png')
    plt.figure()

    plt.hist(pesos_por_localidad_Magdalena, bins=60,color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Magdalena")
    plt.savefig('pesos_por_localidad_Magdalena.png')
    st.image('pesos_por_localidad_Magdalena.png')
    plt.figure()

    plt.hist(edades_por_localidad_Amatitan, bins=60, color='blue')
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Amatitan")
    plt.savefig('edades_por_localidad_Amatitan.png')
    st.image('edades_por_localidad_Amatitan.png')
    plt.figure()

    plt.hist(pesos_por_localidad_Amatitan, bins=60, color='brown')
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Amatitan")
    plt.savefig('pesos_por_localidad_Amatitan.png')
    st.image('pesos_por_localidad_Amatitan.png')
    plt.figure()

    plt.hist(edades_por_localidad_Zapopan, bins=60,color='blue')
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Zapopan")
    plt.savefig('edades_por_localidad_Zapopan.png')
    st.image('edades_por_localidad_Zapopan.png')
    plt.figure()

    plt.hist(pesos_por_localidad_Zapopan, bins=60,color='brown')
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Zapopan")
    plt.savefig('edades_por_localidad_Zapopan.png')
    st.image('edades_por_localidad_Zapopan.png')
    plt.figure()

    #-------------------------FIN ejercicios de histogramas------------------------------------------------------------------------

    #-----------------------------ejercicio 3 Análisis--------------------------------------------------------------------
    #-------------------------------¿Qué localidad tiene mayor porcentaje de menores (<18)?-----------------------------------------#
    print("\n")
    localidades = {}

    # Recorrer las tuplas y contar menores de 18 por localidad
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]

        if localidad in localidades:
            if edad < 18:
                localidades[localidad][0] += 1  # Sumar uno a la cantidad de menores
            localidades[localidad][1] += 1  # Sumar uno a la cantidad total
        else:
            localidades[localidad] = [1, 1] if edad < 18 else [0, 1]  # Inicializar la localidad

    # Calcular el porcentaje de menores de 18 por localidad
    porcentajes_menores = {localidad: (menores / total) * 100 for localidad, (menores, total) in localidades.items()}

    # Obtener la localidad con el mayor porcentaje de menores
    localidad_mayor_porcentaje = max(porcentajes_menores, key=porcentajes_menores.get)
    mayor_porcentaje = porcentajes_menores[localidad_mayor_porcentaje]

    st.header("Localidad con mayor porcentaje de menores de 18 años: {}, con un {}% de menores".format(localidad_mayor_porcentaje, mayor_porcentaje))
    #-------------------------------FIN ¿Qué localidad tiene mayor porcentaje de menores (<18)?-----------------------------------------#

    #-------------------------------¿Qué localidad tiene mayor porcentaje de mayores (>60)?-----------------------------------------#
    print("\n")
    localidades = {}

    # Recorrer las tuplas y contar mayores de 60 por localidad
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]

        if localidad in localidades:
            if edad > 60:
                localidades[localidad][0] += 1  # Sumar uno a la cantidad de mayores
            localidades[localidad][1] += 1  # Sumar uno a la cantidad total
        else:
            localidades[localidad] = [1, 1] if edad > 60 else [0, 1]  # Inicializar la localidad

    # Calcular el porcentaje de mayores de 60 por localidad
    porcentajes_mayores = {localidad: (mayores / total) * 100 for localidad, (mayores, total) in localidades.items()}

    # Obtener la localidad con el mayor porcentaje de mayores
    localidad_mayor_porcentaje = max(porcentajes_mayores, key=porcentajes_mayores.get)
    mayor_porcentaje = porcentajes_mayores[localidad_mayor_porcentaje]

    st.header("Localidad con mayor porcentaje de mayores de 60 años es: {}, con un {}% de mayores".format(localidad_mayor_porcentaje, mayor_porcentaje))
    #-------------------------------FIN ¿Qué localidad tiene mayor porcentaje de mayores (>60)?-----------------------------------------#

    #-------------------------------¿Qué localidad tiene mayor promedio de peso?-----------------------------------------#
    print("\n")
    localidades = {}

    # Recorrer las tuplas y calcular el peso por localidad
    for tupla in listadoejemplo:
        localidad = tupla[6]
        peso = tupla[5]

        if localidad in localidades:
            localidades[localidad].append(peso)  # Agregar el peso a la lista de la localidad
        else:
            localidades[localidad] = [peso]  # Inicializar la lista de pesos para la localidad

    # Calcular el promedio de peso por localidad
    promedios_peso = {localidad: sum(pesos) / len(pesos) for localidad, pesos in localidades.items()}

    # Obtener la localidad con el mayor promedio de peso
    localidad_mayor_promedio = max(promedios_peso, key=promedios_peso.get)
    mayor_promedio = promedios_peso[localidad_mayor_promedio]

    st.header("Localidad con mayor promedio de peso es: {}, con un peso promedio de {}".format(localidad_mayor_promedio, mayor_promedio))
    st.header(f'El promedio de peso en esa localidad es:, {mayor_promedio}')
    #-------------------------------FIN ¿Qué localidad tiene mayor promedio de peso?-----------------------------------------#

    #------------------------------- ¿Cuál es la localidad más longeva??-----------------------------------------#
    # Crear un diccionario para almacenar las edades por localidad
    edades_por_localidad = {}

    # Recorrer las tuplas y agregar los pesos a cada localidad en el diccionario
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]
        
        if localidad in edades_por_localidad:
            edades_por_localidad[localidad].append(edad) #si existe la llave ya en el diccionario le agrego el valor
        else:
            edades_por_localidad[localidad] = [] #si no existe la key se crear un espacio vacío y luego se le agrega el valor
            edades_por_localidad[localidad].append(edad)

    #print(edades_por_localidad)
    # Calcular el promedio de edad por localidad
    promedios_edad_por_localidad = {}
    for localidad, edades in edades_por_localidad.items():
        promedio = sum(edades) / len(edades)
        promedios_edad_por_localidad[localidad] = promedio


    # Encontrar la localidad con el mayor promedio de edad
    localidad_maxima_longeva = max(promedios_edad_por_localidad, key=promedios_edad_por_localidad.get)
    promedio_maximo_longevo = promedios_edad_por_localidad[localidad_maxima_longeva]

    # Imprimir el resultado
    st.header(f'La localidad más longeva es: {localidad_maxima_longeva}')
    st.header(f'El promedio de edad en esa localidad es: {promedio_maximo_longevo}')
    #------------------------------- FIN ¿Cuál es la localidad más longeva??-----------------------------------------#
