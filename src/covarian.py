import numpy as np

# Melakukan perkalian matrix


def multiplyTranspose(matrix):
    transpose = np.matrix.transpose()
    result = np.matmul(matrix, transpose)
    return result

# Menghitung nilai covarian


def covarian(listOfPhi):
    sum = multiplyTranspose(listOfPhi[0])
    for i in range(1, len(listOfPhi)):
        sum += multiplyTranspose(listOfPhi[i])
    cov = sum/len(listOfPhi)
    return cov