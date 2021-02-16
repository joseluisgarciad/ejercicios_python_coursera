# En esta pregunta, hay cuatro variables definidas, pero solo debes retornar una
# (es decir, en la línea 8 poner algo como return algo, con algo una opción
# entre var1, var2, var3, var4). En esta pregunta debes retornar la multiplicación
# de los dos parámetros (valores dentro de paréntesis después del nombre de la función)
# que se pasan a la función. ¿Cuál de las cuatro variables será?
def multiplicacion(a, b):
    var1 = a + b
    var2 = a + var1
    var3 = a * b
    var4 = a / b
    return var3
    # Después de esta línea pon algo como return nombre_variable, donde nombre_variable es la variable correcta según lo que pide. Ojo: debe escribirse con la misma indentación (cantidad de espacios al principio de la línea) que las líneas 2 a 5.


multiplicacion(2, 3)


# =====================

# Para poder resolver este problema y los siguientes, debes escribir el código que falta
# en el espacio que lo señala. Asume que ya existen variables con los nombres masa y peso,
# que ya contienen los valores requeridos (no debes pedírselos al usuario),
# haz los cálculos que necesites, y luego deja el resultado en una variable llamada imc.


def imc(masa, estatura):
    indice = masa / (estatura ** 2)
    return indice


imc(23, 178)


# ============

# Para obtener ciertas estadísticas de un recorrido, se pide realizar un programa que dada una distancia,
# entregue la velocidad en kilómetros por hora y en metros por segundo. Para esto, existen dos variables
# tiempo y distancia que vienen en segundos y kilómetros respectivamente.
# Tu programa debe guardar en la variable resultado un string, por ejemplo, para el siguiente caso:

# tiempo = 1
# distancia = 0.01

# La variable resultado debería tener lo siguiente:
# "La velocidad es 36.0 km/h o 10.0 m/s"

# Para poder resolver este problema , debes escribir el código que falta en el espacio que lo señala.
# Asume que ya existen variables con los nombres tiempo y distancia, que ya contienen los valores requeridos
# (no debes pedírselos al usuario), haz los cálculos que necesites, y luego deja el resultado
# en una variable llamada resultado.

def velocidad(distancia, tiempo):
    resultado = ""
    resultado = ("La velocidad es " + str((distancia / tiempo) * 3600) + " km/h o " + str(
        distancia * 1000 / tiempo) + " m/s")
    return resultado


velocidad(0.01, 1)


# ====================

# En este ejercicio se utilizaran variables de tipo booleanas.
# En computación un operador muy conocido es el operador lógico XOR (exclusive OR),
# el que dadas dos expresiones a y b booleanas, entrega verdadero únicamente si una de ellas es verdadera,
# y falso en cualquier otro caso.

# Por ejemplo si se tiene : resultado = True XOR False en resultado estará almacenado el valor True,
# en cambio si se tiene : resultado = True XOR True    o     resultado = False XOR False
# en resultado estará almacenado el valor False.

# a	    b	    a XOR b
# True	True	False
# True	False	True
# False	True	True
# False	False	False

# Para poder resolver este problema , debes escribir el código que falta en el espacio que lo señala.
# Asume que ya existen variables con los nombres a y b, que ya contienen los valores requeridos
# (no debes pedírselos al usuario), haz los cálculos que necesites,
# y luego deja el resultado en una variable llamada xor.

def xor(a, b):
    res = False
    if bool(a) == bool(b):
        return False
    else:
        return a or b

    return res


# ==================

# La variable cargo contiene el nombre del cargo (por ejemplo, "Externo").
# Recuerda entregar tu resultado modificando únicamente la variable dinero


def sueldo(cargo):
    dinero = 0
    if cargo == "Ejecutivo":
        dinero = 90
    elif cargo == "Jefe":
        dinero = 100
    elif cargo == "Externo":
        dinero = 50
    else:
        dinero = 0

    return dinero


sueldo("Jefe")


# ===================

# Escribe un código que calcule el cuadrado de un número si este es impar,
# o el cubo de un número si este es par. Por ejemplo,
# para 4 tu programa debe entregar 64, y para 3 debe entregar 9.


import math


def exponenciacion(numero):
    resultado = numero
    if numero % 2 == 0:
        resultado = pow(numero, 3)
    else:
        resultado = pow(numero, 2)

    return resultado


exponenciacion(3)


# ===================

# Escriba un programa que verifique si un número es primo o no.
# Por ejemplo, para los número 3, 5, y 13, la variable primo debe ser True, y para 1, 10, y 33, False.


def es_primo(numero):
    primo = True
    if numero <= 1:
        return False
    for n in range(2, numero):
        if numero % n == 0:
            primo = False

    return primo


es_primo(3)


# ===================


# Calculo de Maximo común divisor.
# escriba una función de nombre mcd que reciba dos números n1 y n2 como argumentos,
# y retorne el máximo común divisor. Por ejemplo para los argumentos 10 y 15 debe retornar 5.

def mcd(n1, n2):
    resto = 0
    while (n2 > 0):
        resto = n2
        n2 = n1 % n2
        n1 = resto
    return n1


mcd(10, 15)


# ===================

# Escribe una función exponente, que dado un número n, retorne el exponente de dicha potencia de 2 más grande.
# Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶  = 64.


def exponente(n):
    for i in range(1, n):
        if 2 ** (i) == n:
            return (i)
        if 2 ** (i) > n:
            return (i - 1)


exponente(65)


# ===================

# Considere que existen los números primos y los números pandigitales.
# Los números pandigitales son aquellos que contienen todos los dígitos del 0 al 9 al menos una vez,
# como el 1023478695. Escribe una función panprimo que determine si un número n es pandigital
# y si al mismo tiempo, sus últimos 3 dígitos conforman un número primo, retornando True o False según corresponda.
# Ejemplo : 2424643 False, 1234567890 False, 10123485769 True, 10123485759 False


def panprimo(n):
    encontrado = False
    i = 0
    cadena = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    while (i < len(cadena)):
        if str(cadena[i]) in str(n):
            encontrado = True
        else:
            return False  # sale en el momento en que no encuentra un numero en el patrosn
        i += 1

        # se comprueba si los tres ultimos digitos son primos
    anumero = str(n)
    pre = str(anumero[-3:])
    pre = int(pre)
    if pre == 1:
        return True
    if pre < 1:
        return False
    else:
        for i in range(2, pre):
            if pre % i == 0:
                return False
        return True


panprimo(15907)

# ====================
#
# Escribe una función que reciba dos strings (de largo > 2) como parámetros,
# y retorne un string de largo 4 que consista de las dos primeras letras del primer string
# y las últimas dos letras del segundo.
#
# Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".


def mezclador(string_a, string_b):
    texto = string_a[0: 2] + string_b[-2:]
    return texto


mezclador("familia", "abrigarse")

#=================

# Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista
# del primero, pero con el segundo string intercalado entre cada letra del primero.

# Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"


def intercalar(string_a, string_b):
    i = 0
    palabra = ""
    while i < len(string_a):
        palabra += string_a[i] + string_b
        i += 1

    return palabra


intercalar("paz", "so")

# ====================

# Escriba una función que reciba un string consistente de unos y ceros y retorne
# la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
#
# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1
# (ya que hay 6 unos y 5 ceros)


def ocurrencias(string):
    i = 0
    unos = 0
    ceros = 0

    while i < len(string):
        if string[i] == "1":
            unos += 1
        elif string[i] == "0":
            ceros += 1

        i += 1
    return unos - ceros


ocurrencias("11000110101")

# ===================

# .
# Pregunta 4
#
# Escriba una función que reciba un string s y un número n como parámetros y
# retorne el mismo string s pero sin el elemento en el índice n.
# Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
#
# Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.

def remover_enesimo(s, n):
    i = 0
    palabra = ""
    while i < len(s):
        if i != n:
            palabra += s[i]
        i += 1

    return palabra


remover_enesimo("Hasta luego", 3)

# ================

#
# Escriba una función que reciba un string como parámetro y retorne el string,
# pero con cada elemento que estuviese en mayúsculas reemplazado por "$".
# Asuma que el string consistirá solamente de letras.
#
# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".


def reemplazo(string):
    i = 0
    palabra = ""

    while i < len(string):
        if (string[i]).isupper():
            palabra += "$"
        else:
            palabra += string[i]

        i += 1
    return palabra


reemplazo("Viva la Vida")


#===================================

#Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista,
# y debe retornar retornar el promedio de ellos, junto con su desviación estándar.

#Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados de las diferencias
# de cada elemento respecto al promedio, divididos por la cantidad de elementos.
#Hint 2: Recuerda que puedes retonar dos valores x e y utilizando la notación

##################
# Forma con llamada a libreria Math
##################

from math import sqrt


def promedio_std(lista:list):
    x = y = v = i = 0

    # Promedio de la lista
    x = round(sum(lista) / len(lista), 3)

    for i in lista:
        v += (i - x) ** 2

    # desviación estandar
    y = round(sqrt(v / len(lista)), 3)

    return (x, y)


print(promedio_std([2, 3, 5, 6, 34]))

###########################
### Forma SIN llamar a la libreria MATH
###########################

def promedio_std(lista):
    x = y = suma = 0

    media = sum(lista) / len(lista)

    total = 0.0

    for i in lista:
        suma = suma + i
        total = total + (i - media) ** 2

    y = (total / len(lista)) ** 0.5
    x = suma / len(lista)

    return (x, y)


print(promedio_std([2, 3, 5, 6, 34]))


# ====================

#Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser:
# azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite.
# Escriba una función color_frecuente que reciba como argumento a una lista de strings
# llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.

#Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde',
# 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
# Debe retornar: "verde", 8

# ==========================
# Posibilidad 1
# ==========================

def prioridad(color):
    valor = 0
    if color == "azul":
        valor = 1
    elif color == "rojo":
        valor = 2
    elif color == "verde":
        valor = 3
    elif color == "amarillo":
        valor = 4

    return valor


def color_frecuente(lista: list):
    i: str = ""
    x: int = 0
    occ: int = 0
    color_ant: str = ""
    colores = []

    lista.sort()
    color_ant = lista[0]
    for i in lista:
        if i != color_ant:  # or i == len(lista)-1:
            colores.append([prioridad(color_ant), color_ant, occ])
            occ = 0

        color_ant = i
        occ = occ + 1
        x += 1
        if len(lista) == x:
            colores.append([prioridad(color_ant), color_ant, occ])

    # colores.sort(key=lambda porprioridad: porprioridad[0])

    be = sorted(colores, key=lambda x: (x[2], -x[0]), reverse=True)

    print(be)
    return be[0][1], be[0][2]


lista = ["azul", "rojo", "verde", "verde", "verde", "rojo", "verde", "verde", "azul", "amarillo", "azul", "azul", "verde", "verde", "verde", "amarillo", "amarillo"]

print(color_frecuente(lista))

# ==========================
# Posibilidad 1
# ==========================


def color_frecuente_2(lista):
    color = ""
    maximo = 0

    for c in ['azul', 'rojo', 'verde', 'amarillo']:
        if lista.count(c) > maximo:
            maximo = lista.count(c)
            color = c

    return color, maximo


lista = ["azul", "rojo", "verde", "verde", "verde", "rojo", "verde", "verde", "azul", "amarillo", "azul", "azul", "verde", "verde", "verde", "amarillo", "amarillo"]

print(color_frecuente_2(lista))

# ==============================

# Un uso muy común de las listas es el de representar tableros con ellas. Para eso se utilizan listas de listas,
# de este modo, se puede entender una lista de listas como una matriz. Así, para acceder a un elemento i,j
# de la matriz, se debe acceder a: matriz[i][j].

# Para ese ejercicio se dispone de un tablero de buscaminas especial, donde lo único que hay es bombas en las
# distintas posiciones. Este tablero es de la forma:
# 	X		X
# X
# 	X	X
# X			X

# Donde las X representan las bombas. Ese tablero, en representación matricial de Python, donde se utilizan strings
# con un espacio: " " y "X" para representar espacios libres y bombas respectivamente, viene dado por:

# 1  tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

# El objetivo de este ejercicio, es que programes una función buscaminas que reciba como argumento a una matriz tablero
# y dos coordenadas i, j, y que entregue la cantidad de bombas que rodean a esa posición.

# Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene dada por i=0 y j=0,
# tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0).

# Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4,
# pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).

# Hint: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir posiciones más grandes
# que ese tamaño o menores que 0, tu programa arrojará error.


def buscaminas(matriz, i, j):
    x: int = j
    y: int = i
    dx: int = x - 1
    dy: int = y - 1

    hx: int = x + 2
    if hx > len(matriz):
        hx = len(matriz)
    hy: int = y + 2
    if hy > len(list(zip(*matriz))[0]):
        hy = len(list(zip(*matriz))[0])
    bb: int = -1
    aa: int = -1
    bombas: int = 0

    #    if i == 0 and bb < 0:  bb = 0
    #    if j == 0 and aa < 0:  aa = 0

    for aa in range(dy, hy):  # Y
        for bb in range(dx, hx):  # X
            if aa >= 0 and bb >= 0:
                # if aa <= hx:  # verifica que no se sobre pasa el limite horizontal
                print(aa, "-", bb, "-", matriz[aa][bb])
                if matriz[aa][bb] == "X":
                    if str(aa) + str(bb) != str(y) + str(x):  # verifica que no se cuente la posición pasada por
                        bombas += 1  # parametro como bomba

    print("------")


    b = 0
    for a in range(len(matriz)):
        print("[", matriz[a][b])
        for b in range(len(list(zip(*matriz))[0])):  # coge el primer elemento de cada sublista
            print(matriz[a][b])

    # if matriz[a][b] == "X":
    #  print(matriz[a][b])
    # else:
    # print("0")

    print(matriz)

    return bombas


tablero = [['A', 'X', 'B', 'X'], ['X', 'C', 'D', 'E'], ['F', 'X', 'X', 'G'], ['X', 'H', 'I', 'X']]

print("hay :", buscaminas(tablero, 1, 2), " minas en el tablero")


# ================================================
friends = []
friends = linea[3:-1].split(",")  # pasa el contenido de un string separado por comas a una lista

# ===============================================