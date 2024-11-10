# # numeros = [1, 2, 3, 4, 5]

# # print(numeros)

# # for i in range(len(numeros)):
# #     print(numeros[i])
# # matriz = [[1, 4, 5, 9, 8],
# #           [3, 6, 9, 8, 7],
# #           [4, 8, 9, 10, 11]]
# # print(matriz[1][4])
# # matriz[2][2] = 1
# # print(matriz)


# # def buscar_elemento_producto(mensaje, lista):
# #     elemento_d_e_busqueda = input(mmensaje)
# #     for fil in len(lista)
# #     if lista[fil][col] == elemento_d_e_busqueda:
# #         print("el elemento se encronto")


# def inicializar_matriz(cantidad_filas: int, cantidad_columnas, valor_inicial: any) -> list:
#     """Crea una matriz con lista anidadas con los elementos inicializados en el valor inicial

#     Args:
#         cantidad_filas (int): cantidas de listas que tendra la matriz
#         cantidad_columnas (_type_): cantidad de elementos que posee cada lista interna
#         valor_inicial (any): valor deseados con que se quiere cada uno de los elentnso
#     Returns:
#         list: retorna una matriz con estructura de dato bidimensional
#     """
#     matriz = []
#     for i in range(cantidad_filas):
#         fila = [valor_inicial]*cantidad_columnas
#         matriz += fila
#     return matriz



# def buscar_elemento_producto(mensaje, lista):
#     elemento_d_e_busqueda = input(mmensaje)
#     for fil in len(lista)
#     if lista[fil][col] == elemento_d_e_busqueda:
#         print("el elemento se encronto")


# def inicializar_matriz(cantidad_filas: int, cantidad_columnas, valor_inicial: any) -> list:
#     """Crea una matriz con lista anidadas con los elementos inicializados en el valor inicial

#     Args:
#         cantidad_filas (int): cantidas de listas que tendra la matriz
#         cantidad_columnas (_type_): cantidad de elementos que posee cada lista interna
#         valor_inicial (any): valor deseados con que se quiere cada uno de los elentnso
#     Returns:
#         list: retorna una matriz con estructura de dato bidimensional
#     """
#     matriz = []
#     for i in cantidad_filas:
#         fila = [valor_inicial]*cantidad_columnas
#         matriz += fila
#     return matriz

def cargar_matriz_secuencialmente (matriz: list)-> list:
    """carga de elementos de una triz desde el primero hasta el ultimo en forma sucesiva"""
    if isinstance(matriz,list):
        for i in range(len( matriz)):
            for j in range(len(matriz[i])):
                matriz [i] [j] = int(input(f"por favor ingrese la fila {i} columna {j}"))
                
