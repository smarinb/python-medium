### Lists Comprehension###

my_original_list = [1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)]
print(my_list)

def area_cuadrado(lado):
    return lado*lado

my_list_areas_cuadrado = [area_cuadrado(lado) for lado in range(8)]
print(my_list_areas_cuadrado)

my_range = range(8)
print(list(my_range))



