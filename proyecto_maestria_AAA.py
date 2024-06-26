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
localidades = ["Tequila", "Ameca", "Magdalena", "Amatitan", "Zapopan"]


if st.session_state['start']:
    try:
        with sr.Microphone() as source:
            with st.spinner("Escuchando...."):
                for i in range (0, 2):
                
                    speak("Por favor diga un nombre")
                    voice = listener.listen(source)  
                    rec_name = listener.recognize_google(voice)  
                    st.write('Nombre escuchado : ',rec_name)
                    nombres.append(rec_name)   
                    
                    
                    speak(f'Por favor diga un apellido paterno de {rec_name}')
                    voice = listener.listen(source)
                    rec_apellidopaterno = listener.recognize_google(voice)
                    st.write('Apellido escuchado : ',rec_apellidopaterno)
                    apellidos_paternos.append(rec_apellidopaterno)
                    
                    
                    speak(f'Por favor diga un apellido materno de {rec_name}')
                    voice = listener.listen(source)
                    rec_apellidomaterno = listener.recognize_google(voice)
                    st.write('Apellido escuchado : ',rec_apellidomaterno)
                    apellidos_maternos.append(rec_apellidomaterno)

                    st.write(i ,nombres[i],apellidos_paternos[i],apellidos_maternos[i])
                    st.success('Usuario agregado') 
        
            
            
    except Exception as e:
        st.write(f"Error: {e}")
        st.write('Algo salio mal')

    

    listadoejemplo = []  

    for j in range (10000): 
        ID =  j+1
        Nombre = random.choices(nombres) 
        Apellido_paterno = random.choices(apellidos_paternos) 
        Apellido_materno = random.choices(apellidos_maternos) 
        edad = random.randint(0, 100)
        peso = round(random.uniform(1,200),2) 
        localidad = random.choices(localidades) 
        tupla = (ID, Nombre[0], Apellido_paterno[0], Apellido_materno[0], edad, peso, localidad[0])
        listadoejemplo.append(tupla)
        
    print(tuple(listadoejemplo))

    
    

    apellidos = {}
    hermanos = set()  

    
    for tupla in listadoejemplo:
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
    st.write("Existen {} apellidos con hermanos en la base de datos".format(num_hermanos))
    st.write('Son los siguientes:', apellidos_filtrados)
    
    


    homonimos = set()
    nombres_completos = set()

    

    for tupla in listadoejemplo:
        nombre_completo = ' '.join([str(tupla[1]), str(tupla[2]), str(tupla[3])])  
        if nombre_completo in nombres_completos:
            homonimos.add(nombre_completo)
        else:
            nombres_completos.add(nombre_completo)

    

    print(homonimos)

    num_homonimos = len(homonimos)

    st.subheader('Cuantos homónimos hay en la base de datos')
    st.write("Hay {} homónimos en la base de datos".format(num_homonimos))
        

    
    listadoedad = []
    listadopesos = []

    
    for i in listadoejemplo:
        listadoedad.append(i[4])  

    plt.hist(listadoedad, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Edades (total)")
    plt.savefig('listadoedad.png')
    st.image('listadoedad.png')
    plt.figure()
    
    
    for i in listadoejemplo:
        listadopesos.append(i[5])  

    plt.hist(listadopesos, bins=60)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title("Histograma Pesos (total)")
    plt.savefig('listadopesos.png')
    st.image('listadopesos.png')
    plt.figure()

    

    
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

    

    
    
    print("\n")
    localidades = {}

    
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]

        if localidad in localidades:
            if edad < 18:
                localidades[localidad][0] += 1  
            localidades[localidad][1] += 1  
        else:
            localidades[localidad] = [1, 1] if edad < 18 else [0, 1]  

    
    porcentajes_menores = {localidad: (menores / total) * 100 for localidad, (menores, total) in localidades.items()}

    
    localidad_mayor_porcentaje = max(porcentajes_menores, key=porcentajes_menores.get)
    mayor_porcentaje = porcentajes_menores[localidad_mayor_porcentaje]

    st.header("Localidad con mayor porcentaje de menores de 18 años: {}, con un {}% de menores".format(localidad_mayor_porcentaje, mayor_porcentaje))
    

    
    print("\n")
    localidades = {}

    
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]

        if localidad in localidades:
            if edad > 60:
                localidades[localidad][0] += 1  
            localidades[localidad][1] += 1  
        else:
            localidades[localidad] = [1, 1] if edad > 60 else [0, 1]  

    
    porcentajes_mayores = {localidad: (mayores / total) * 100 for localidad, (mayores, total) in localidades.items()}

    
    localidad_mayor_porcentaje = max(porcentajes_mayores, key=porcentajes_mayores.get)
    mayor_porcentaje = porcentajes_mayores[localidad_mayor_porcentaje]

    st.header("Localidad con mayor porcentaje de mayores de 60 años es: {}, con un {}% de mayores".format(localidad_mayor_porcentaje, mayor_porcentaje))
    

    
    print("\n")
    localidades = {}

    
    for tupla in listadoejemplo:
        localidad = tupla[6]
        peso = tupla[5]

        if localidad in localidades:
            localidades[localidad].append(peso)  
        else:
            localidades[localidad] = [peso]  

    
    promedios_peso = {localidad: sum(pesos) / len(pesos) for localidad, pesos in localidades.items()}

    
    localidad_mayor_promedio = max(promedios_peso, key=promedios_peso.get)
    mayor_promedio = promedios_peso[localidad_mayor_promedio]

    st.header("Localidad con mayor promedio de peso es: {}, con un peso promedio de {}".format(localidad_mayor_promedio, mayor_promedio))
    st.header(f'El promedio de peso en esa localidad es:, {mayor_promedio}')
    

    
    
    edades_por_localidad = {}

    
    for tupla in listadoejemplo:
        localidad = tupla[6]
        edad = tupla[4]
        
        if localidad in edades_por_localidad:
            edades_por_localidad[localidad].append(edad) 
        else:
            edades_por_localidad[localidad] = [] 
            edades_por_localidad[localidad].append(edad)

    
    
    promedios_edad_por_localidad = {}
    for localidad, edades in edades_por_localidad.items():
        promedio = sum(edades) / len(edades)
        promedios_edad_por_localidad[localidad] = promedio


    
    localidad_maxima_longeva = max(promedios_edad_por_localidad, key=promedios_edad_por_localidad.get)
    promedio_maximo_longevo = promedios_edad_por_localidad[localidad_maxima_longeva]

    
    st.header(f'La localidad más longeva es: {localidad_maxima_longeva}')
    st.header(f'El promedio de edad en esa localidad es: {promedio_maximo_longevo}')
    
