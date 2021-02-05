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
