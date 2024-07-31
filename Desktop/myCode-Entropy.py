import numpy as np

def create_incremental_diagonal_matrix():
    rows = int(input("Entrez le nombre de lignes: "))
    cols = int(input("Entrez le nombre de colonnes: "))

    matrix = np.zeros((rows, cols), dtype=int)

    value = 0
    start_row = 0
    nonzero = np.count_nonzero(matrix)
    zeroes = (rows*cols)-nonzero
    r= 0
    c = 0

    while zeroes != 1 :
            
            matrix[r, c] = value
            value += 1
            print(r,c)

            if(c < cols-1 and r < rows-1) :
                r += 1
                c += 1
                print("case 1")

            else:
                if (c == cols-1 and r <= rows-1) :
                    c = 0
                    r = start_row+1
                    start_row = r
                    print("case 2")

                elif(r <= rows-1 and c < cols-1) :
                    r = 0
                    c = c + 1
                    print("case 3")

            nonzero = np.count_nonzero(matrix)
            zeroes = (rows*cols)-nonzero
            print(matrix)
    return matrix

# Appelle la fonction et affiche le résultat
matrix = create_incremental_diagonal_matrix()
print(matrix)
