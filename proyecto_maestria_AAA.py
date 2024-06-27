import speech_recognition as sr
import random
import matplotlib.pyplot as plt
import os
import streamlit as st



st.title('Programa para analisis de datos')
st.header('Listo..?')

if 'start' not in st.session_state:
    st.session_state['start'] = False


def button_start():
    st.session_state['start'] = not st.session_state['start']


if st.button('Comenzar'):
    button_start()


def speak(text):
    os.system(f"say {text}")

listener = sr.Recognizer()

nombres = []
apellidos_paternos = []
apellidos_maternos = []
ciudades = ["Tequila", "Ameca", "Magdalena", "Amatitan", "Zapopan"]


if st.session_state['start']:
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            with st.spinner("Escuchando...."):
                for i in range(0, 3):
                    while True:
                        try:
                            speak("Por favor diga un nombre")
                            voice = listener.listen(source,timeout=2)
                            nombre_escuchado = listener.recognize_google(voice)
                            st.write('Nombre escuchado : ', nombre_escuchado)
                            nombres.append(nombre_escuchado)
                            break
                        except sr.UnknownValueError:
                            speak("No se entendió el nombre. Por favor intente de nuevo.")
                            st.error("No se entendió el nombre. Por favor intente de nuevo.")
                        except sr.RequestError:
                            st.error("Error de conexión con el servicio de reconocimiento. Por favor intente de nuevo.")
                        except sr.WaitTimeoutError:
                            speak("Tiempo de espera agotado. Por favor intente de nuevo.")
                            st.error("Tiempo de espera agotado. Por favor intente de nuevo.")

                    while True:
                        try:
                            speak(f'Por favor diga un apellido paterno de {nombre_escuchado}')
                            voice = listener.listen(source,timeout=2)
                            apellidopaterno_escuchado = listener.recognize_google(voice)
                            st.write('Apellido escuchado : ', apellidopaterno_escuchado)
                            apellidos_paternos.append(apellidopaterno_escuchado)
                            break
                        except sr.UnknownValueError:
                            speak("No se entendió el apellido paterno. Por favor intente de nuevo.")
                            st.error("No se entendió el apellido paterno. Por favor intente de nuevo.")
                        except sr.RequestError:
                            st.error("Error de conexión con el servicio de reconocimiento. Por favor intente de nuevo.")
                        except sr.WaitTimeoutError:
                            speak("Tiempo de espera agotado. Por favor intente de nuevo.")
                            st.error("Tiempo de espera agotado. Por favor intente de nuevo.")

                    while True:
                        try:
                            speak(f'Por favor diga un apellido materno de {nombre_escuchado}')
                            voice = listener.listen(source,timeout=2)
                            apellidomaterno_escuchado = listener.recognize_google(voice)
                            st.write('Apellido escuchado : ', apellidomaterno_escuchado)
                            apellidos_maternos.append(apellidomaterno_escuchado)
                            break
                        except sr.UnknownValueError:
                            speak('"No se entendió el apellido materno. Por favor intente de nuevo."')
                            st.error("No se entendió el apellido materno. Por favor intente de nuevo.")
                        except sr.RequestError:
                            st.error("Error de conexión con el servicio de reconocimiento. Por favor intente de nuevo.")
                        except sr.WaitTimeoutError:
                            speak("Tiempo de espera agotado. Por favor intente de nuevo.")
                            st.error("Tiempo de espera agotado. Por favor intente de nuevo.")

                    st.write(i, nombres[i], apellidos_paternos[i], apellidos_maternos[i])
                    st.success('Usuario agregado')

    except Exception as e:
        st.subheader('Algo salió mal, intente de nuevo')
        st.write('El error es: ', e)
    

    listado = []  

    for j in range (10000): 
        ID =  j+1
        Nombre = random.choices(nombres) 
        Apellido_paterno = random.choices(apellidos_paternos) 
        Apellido_materno = random.choices(apellidos_maternos) 
        edad = random.randint(0, 100)
        peso = round(random.uniform(1,200),2) 
        ciudad = random.choices(ciudades) 
        tupla = (ID, Nombre[0], Apellido_paterno[0], Apellido_materno[0], edad, peso, ciudad[0])
        listado.append(tupla)
        
    print(tuple(listado))

    
    

    apellidos = {}
    hermanos = set()  

    
    for tupla in listado:
        apellido_paterno = tupla[2]
        apellido_materno = tupla[3]
        apellidosconcatenados = ' '.join([str(apellido_paterno), str(apellido_materno)])  
        
        if apellidosconcatenados in apellidos:
            apellidos[apellidosconcatenados] += 1  
            hermanos.add(apellidosconcatenados)
        else:
            apellidos[apellidosconcatenados] = 1

    num_hermanos = len(hermanos)


    apellidos_filtrados = {}
    for apellido, count in apellidos.items(): 
        if count > 1:
            apellidos_filtrados[apellido] = count

    st.header('Estadisticas')
    md = st.text_area(f'¿Cuántos hermanos hay en la Base de Datos?',
                  "Existen {} apellidos con hermanos en la base de datos".format(num_hermanos))
    st.write('Son los siguientes:', apellidos_filtrados)
    
    


    homonimos = set()
    nombres_completos = set()

    

    for tupla in listado:
        nombre_completo = ' '.join([str(tupla[1]), str(tupla[2]), str(tupla[3])])  
        if nombre_completo in nombres_completos:
            homonimos.add(nombre_completo)
        else:
            nombres_completos.add(nombre_completo)

    

    print(homonimos)

    num_homonimos = len(homonimos)

    st.subheader('Homónimos')
    md = st.text_area(f'Cuantos homónimos hay en la base de datos...?',
                  "Hay {} homónimos en la base de datos".format(num_homonimos))
        

    
    listadoedad = []
    listadopesos = []

    
    for i in listado:
        listadoedad.append(i[4])  

    plt.hist(listadoedad, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades (total)")
    plt.savefig('listadoedad.png')
    st.image('listadoedad.png')
    plt.figure()
    
    
    for i in listado:
        listadopesos.append(i[5])  

    plt.hist(listadopesos, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos (total)")
    plt.savefig('listadopesos.png')
    st.image('listadopesos.png')
    plt.figure()

    

    
    edades_por_ciudad_Tequila = []
    pesos_por_ciudad_Tequila = []
    edades_por_ciudad_Ameca = []
    pesos_por_ciudad_Ameca = []
    edades_por_ciudad_Magdalena = []
    pesos_por_ciudad_Magdalena = []
    edades_por_ciudad_Amatitan = []
    pesos_por_ciudad_Amatitan = []
    edades_por_ciudad_Zapopan = []
    pesos_por_ciudad_Zapopan = []


    for i in listado:
        if i[6] == "Tequila":
            edades_por_ciudad_Tequila.append(i[4])
            pesos_por_ciudad_Tequila.append(i[5])
        elif i[6] == "Ameca":
            edades_por_ciudad_Ameca.append(i[4])
            pesos_por_ciudad_Ameca.append(i[5])
        elif i[6] == "Magdalena":
            edades_por_ciudad_Magdalena.append(i[4])
            pesos_por_ciudad_Magdalena.append(i[5])
        elif i[6] == "Amatitan":
            edades_por_ciudad_Amatitan.append(i[4])
            pesos_por_ciudad_Amatitan.append(i[5])
        else:
            edades_por_ciudad_Zapopan.append(i[4])
            pesos_por_ciudad_Zapopan.append(i[5])
    

    st.header('Histogramas de Tequila')
    plt.figure()
    plt.hist(edades_por_ciudad_Tequila, bins=60, color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Tequila")
    plt.savefig('edades_por_ciudad_Tequila.png')
    st.image('edades_por_ciudad_Tequila.png')
    plt.figure()

    plt.hist(pesos_por_ciudad_Tequila, bins=60, color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Tequila")
    plt.savefig('pesos_por_ciudad_Tequila.png')
    st.image('pesos_por_ciudad_Tequila.png')
    plt.figure()

    st.header('Histogramas de Ameca')
    plt.hist(edades_por_ciudad_Ameca, bins=60, color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Ameca")
    plt.savefig('edades_por_ciudad_Ameca.png')
    st.image('edades_por_ciudad_Ameca.png')
    plt.figure()

    
    plt.hist(pesos_por_ciudad_Ameca, bins=60, color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Ameca")
    plt.savefig('pesos_por_ciudad_Ameca.png')
    st.image('pesos_por_ciudad_Ameca.png')
    plt.figure()


    st.header('Histogramas de Magdalena')
    plt.hist(edades_por_ciudad_Magdalena, bins=60,color="blue")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Magdalena")
    plt.savefig('edades_por_ciudad_Magdalena.png')
    st.image('edades_por_ciudad_Magdalena.png')
    plt.figure()


    
    plt.hist(pesos_por_ciudad_Magdalena, bins=60,color="brown")
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Magdalena")
    plt.savefig('pesos_por_ciudad_Magdalena.png')
    st.image('pesos_por_ciudad_Magdalena.png')
    plt.figure()


    st.header('Histogramas de Amatitan')
    plt.hist(edades_por_ciudad_Amatitan, bins=60, color='blue')
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Amatitan")
    plt.savefig('edades_por_ciudad_Amatitan.png')
    st.image('edades_por_ciudad_Amatitan.png')
    plt.figure()

    
    plt.hist(pesos_por_ciudad_Amatitan, bins=60, color='brown')
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos Amatitan")
    plt.savefig('pesos_por_ciudad_Amatitan.png')
    st.image('pesos_por_ciudad_Amatitan.png')
    plt.figure()

    st.header('Histogramas de Zapopan')
    plt.hist(edades_por_ciudad_Zapopan, bins=60,color='blue')
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Zapopan")
    plt.savefig('edades_por_ciudad_Zapopan.png')
    st.image('edades_por_ciudad_Zapopan.png')
    plt.figure()


    plt.hist(pesos_por_ciudad_Zapopan, bins=60,color='brown')
    plt.xlabel("Pesos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades Zapopan")
    plt.savefig('edades_por_ciudad_Zapopan.png')
    st.image('edades_por_ciudad_Zapopan.png')
    plt.figure()

    
    ciudades = {}

    
    for tupla in listado:
        ciudad = tupla[6]
        edad = tupla[4]

        if ciudad in ciudades:
            if edad < 18:
                ciudades[ciudad][0] += 1  
            ciudades[ciudad][1] += 1  
        else:
            ciudades[ciudad] = [1, 1] if edad < 18 else [0, 1]  

    
    porcentajes_menores = {ciudad: (menores / total) * 100 for ciudad, (menores, total) in ciudades.items()}

    
    ciudad_mayor_porcentaje = max(porcentajes_menores, key=porcentajes_menores.get)
    mayor_porcentaje = porcentajes_menores[ciudad_mayor_porcentaje]

    md = st.text_area(f'¿Qué localidad tiene mayor porcentaje de menores (<18)?',
                  "La ciudad con mayor porcentaje de menores de 18 años es: {}, ya que cuenta con con un {}% de menores".format(ciudad_mayor_porcentaje, mayor_porcentaje))
    

    ciudades = {}

    for tupla in listado:
        ciudad = tupla[6]
        edad = tupla[4]

        if ciudad in ciudades:
            if edad > 18 and edad < 60:
                ciudades[ciudad][0] += 1  
            ciudades[ciudad][1] += 1  
        else:
            ciudades[ciudad] = [1, 1] if edad > 18 and edad < 60 else [0, 1]  

    porcentajes_mayores = {ciudad: (mayores / total) * 100 for ciudad, (mayores, total) in ciudades.items()}

    ciudad_mayor_porcentaje = max(porcentajes_mayores, key=porcentajes_mayores.get)
    mayor_porcentaje = porcentajes_mayores[ciudad_mayor_porcentaje]

    md = st.text_area(f'¿Qué localidad tiene mayor porcentaje de adultos (18-60)?',
                  "La ciudad con mayor porcentaje de mayores de entre 18 y 60 años es: {}, con un {}% ".format(ciudad_mayor_porcentaje, mayor_porcentaje))





    ciudades = {}

    
    for tupla in listado:
        ciudad = tupla[6]
        edad = tupla[4]

        if ciudad in ciudades:
            if edad > 60:
                ciudades[ciudad][0] += 1  
            ciudades[ciudad][1] += 1  
        else:
            ciudades[ciudad] = [1, 1] if edad > 60 else [0, 1]  

    
    porcentajes_mayores = {ciudad: (mayores / total) * 100 for ciudad, (mayores, total) in ciudades.items()}

    
    ciudad_mayor_porcentaje = max(porcentajes_mayores, key=porcentajes_mayores.get)
    mayor_porcentaje = porcentajes_mayores[ciudad_mayor_porcentaje]

    md = st.text_area(f'¿Qué localidad tiene mayor porcentaje de adultos mayores (>60)?',
                  "La ciudad con mayor porcentaje de mayores de 60 años es: {}, con un {}% de mayores".format(ciudad_mayor_porcentaje, mayor_porcentaje))
    


    ciudades = {}

    for tupla in listado:
        ciudad = tupla[6]
        edad = tupla[4]
        peso = tupla[5]

        if 18 <= edad <= 60:  
            if ciudad in ciudades:
                ciudades[ciudad].append(peso)
            else:
                ciudades[ciudad] = [peso]

    promedios_peso = {ciudad: sum(pesos) / len(pesos) for ciudad, pesos in ciudades.items()}

    ciudad_mayor_promedio = max(promedios_peso, key=promedios_peso.get)
    mayor_promedio = promedios_peso[ciudad_mayor_promedio]

    
    md = st.text_area(f'¿En qué localidad son más pesados los adultos (18 - 60)?',
                  f"La ciudad con los adultos (18 - 60) más pesados es: {ciudad_mayor_promedio} con un promedio de {mayor_promedio:.2f} kg")
    

    
    
    edades_por_ciudad = {}

    
    for tupla in listado:
        ciudad = tupla[6]
        edad = tupla[4]
        
        if ciudad in edades_por_ciudad:
            edades_por_ciudad[ciudad].append(edad) 
        else:
            edades_por_ciudad[ciudad] = [] 
            edades_por_ciudad[ciudad].append(edad)

    
    
    promedios_edad_por_ciudad = {}
    for ciudad, edades in edades_por_ciudad.items():
        promedio = sum(edades) / len(edades)
        promedios_edad_por_ciudad[ciudad] = promedio


    
    ciudad_maxima_longeva = max(promedios_edad_por_ciudad, key=promedios_edad_por_ciudad.get)
    promedio_maximo_longevo = promedios_edad_por_ciudad[ciudad_maxima_longeva]


    md = st.text_area(f'¿Cuál es la localidad más longeva?',
                  f'La ciudad más longeva es: {ciudad_maxima_longeva}, con el promedio de edad en esa ciudad es: {promedio_maximo_longevo}')
    
