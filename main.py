#Zad matematyczne
# import math
# x = math.log(3, 27) + pow(8/26 + math.sin(50), 1/3)
# print(x)

#Zad zliczanie
# lista = [44, 30, 35, 40, 200]
# b = (min(lista))
# a = lista.count(min(lista))
# print('Najmniejsza liczba: ', b, '\n Ilość wystąpień najmniejszej liczby: ',a)

#Zad Calkowite,Zmiennoprzecinkowe
# lista = [1, 2, 19.4, 4, 5, 12.35, 7, 8, 2.5, 10.24]
# ile_calkowitych = 0
# ile_zmiennoprzecinkowych = 0
# for x in lista:
#     if(isinstance(x, int)):
#         ile_calkowitych += 1
#     elif(isinstance(x, float)):
#         ile_zmiennoprzecinkowych +=1
# print('Tyle calkowitych: ', ile_calkowitych, '\n Tyle zmiennoprzecinkowych:', ile_zmiennoprzecinkowych)

#liczenie wzorow
# a = pow(5/9, 2) + pow( + math.log(23 + math.sin(45)), 1/4)
# print(a)

#zliczanie + suma

# lista = [1, 2, 3, 4, 5, 6, 'siema', 'nko', 2.5]
# def suma_liczb(dodawanie):
#     suma = 0
#     for x in dodawanie:
#         if(isinstance(x, str) == False):
#             suma += x
#             print(x)
#     print('Suma:', suma)
#
# suma_liczb(lista)

# ZAD 1 (Napisz funkcje, która jako argument przyjmuje słownik gdzie klucz i wartość będą
# dowolnego typu. Funkcja ma za zadanie utworzyć i zwrócić listę, do której trafią te elementy
# ze słownika które będą miały jako klucz i wartość liczbę całkowitą.)
#
# import math
# slownik = {120 : 2, 240 : 4 ,'elo': 'elko'
# def calkowite(siema):
# lista = []
#      for x in siema:
#         if(type(x) == int):
#         if(type(siema[x]) == int):
# lista.append(x)
#
# lista.append(siema[x])
# return lista



# lista1 = calkowite(slownik)
# print(lista1)
#
#
#
# ZAD 3.(Napisz skrypt, w którym utworzysz listę z liczbami całkowitymi, a następnie sprawdzisz
# czy co drugi element jest parzysty. Wyświetl ilość takich elementów.)
#
# lista = [10, 6, 2, 4, 16, 8]
# for x in range(0, len(lista), 2):
# if (lista[x] % 2 == 0):
# print(lista[x])
#
#
#
#
#
# ZAD 4.(Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby całkowite a i b.
# Zadaniem jest utworzenie ciągu liczb od a do b z krokiem równym 2 i podniesieniem każdego
# elementu do kwadratu. W skrypcie dokonaj sprawdzenia błędów związanych z wczytywaną
# wartością, do tego celu użyj składni try-except.)
#
# a = input()
# b = input()
# try:
# for x in range(int(a), int(b), 2):
# x **= 2
# print(x)
# except:
# print('Błąd. Wypisz liczby całkowite.')