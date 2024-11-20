import numpy as np
# *********** EJERCICIO 1 ***********

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# n_arr = arr1 + arr2
# print(arr1[0])
# print(n_arr[2])

# *********** EJERCICIO 2 ***********

# a = np.array([1,2,3])
# b = 2
# r = a+b
# print(r)

# aa1 = np.array([[3,3,3],
#                 [3,3,3]])
# bb1 = np.array([2,2,4])
# rr1 = aa1 * bb1
# print(rr1)

# *********** EJERCICIO 3 ***********
# aa = np.array([[1,2,3],
#                 [4,5,6]])
# bb = np.array([1,2,3])

# res = aa*bb
# print(res)

# mat_1 = np.array([[1,2], [3,4]])
# print("matriz uno: \n", mat_1)
# mat_1_Trasp = mat_1.T
# print("matriz uno: \n", mat_1_Trasp)

# vec = np.array([10, 20, 30, 40])
# prom = np.mean(vec)
# std_desv = np.std(vec)

# print(prom)
# print(std_desv)


# *********** EJERCICIO 4 ***********
# data = np.array([10, 12, 23, 16, 23])



# *********** EJERCICIO 5 ***********
v = np.array([5,5,5])
norma_2 = np.sqrt(np.sum(v**2))


# dato curioso:
#     let vector = [2, 3, 4]
#
#     norma_del_vector = ( 2^2 + 3^2 +  6^2  )^2
#


# *********** EJERCICIO 6 - CAMINATA ALEATORIA ***********
pasos = 500

cambios = np.random.choice([-1, 1], size=pasos)
pos = np.cumsum(cambios)
print(f"valor final: {pos[-1]} \n---")




