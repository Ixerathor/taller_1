# -*- coding: utf-8 -*-

l = [2, 7, 1, 5, 1, 6, 6, 2, 8, 6]

print ("Esta es la lista: ", l)

promedio = sum(l) / len(l)
print ("El promedio es: ", promedio)

# moda
repeticiones = 0
for i in l:
    apariciones = l.count(i)
    if apariciones > repeticiones:
        repeticiones = apariciones

modas = []
for i in l:
    apariciones = l.count(i)
    if apariciones == repeticiones and i not in modas:
        modas.append(i)

print ("La moda es: ", modas)

# mediana
l.sort()
print (l)

if len(l) % 2 == 0:
    n = len(l)
    mediana = (l[int(n / 2 - 1)] + l[int(n / 2)]) / 2
else:
    mediana = l[int(len(l) / 2)]

print ("La mediana es: ", mediana)

#varianza

def print_l(l):
    for grade in l:
        print(grade)


def grades_sum(l):
    total = 0
    for grade in l:
        total += grade
    return total


def grades_average(l):
    sum_of_grades = grades_sum(l)
    average = float(sum_of_grades) / len(l)
    return average


# Para calcular la varianza restamos a cada puntancion la media y
# los sumamos, lo elevamos al cuadrado y lo divimos entre 2
def grades_variance(scores, average):
    sumatorio = 0
    for data in scores:
        sumatorio += (average - float(data)) ** 2
    variance = float(sumatorio) / len(l)
    return variance


grades = [2, 7, 1, 5, 1, 6, 6, 2, 8, 6]
print("La varianza de ",l, " es: ",grades_variance(l, grades_average(l)))
