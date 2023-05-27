def rotateMatrix(matrix):
    
    if (len(matrix)==0) or (len(matrix) != len(matrix[0])):
        return False

    n = len(matrix)
    m = n//2

    for layer in range(m):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i - first

            top = matrix[first][i]  #set top

            matrix[first][i] = matrix[last - offset][first]  # left -> top

            matrix[last - offset][first] = matrix[last][last - offset] # bottom -> left

            matrix[last][last - offset] = matrix[i][last]  # right -> bottom

            matrix[i][last] = top # top -> right

    return matrix

print(rotateMatrix([[2,3,4],[5,6,7],[8,9,1]]))