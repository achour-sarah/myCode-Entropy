import numpy as np

def create_incremental_diagonal_matrix():
    # Demande à l'utilisateur d'entrer le nombre de lignes et de colonnes
    rows = int(input("Entrez le nombre de lignes: "))
    cols = int(input("Entrez le nombre de colonnes: "))

    # Crée un tableau de zéros de la taille spécifiée
    matrix = np.zeros((rows, cols), dtype=int)

    # Initialise la valeur à insérer et les indices de départ pour les lignes et les colonnes
    value = 0
    start_row = 0
    start_col = 0

    # Continue à remplir les diagonales jusqu'à ce que toutes les lignes et colonnes soient traitées
    while start_row < rows and start_col < cols:
        r, c = start_row, start_col
        # Remplit la diagonale actuelle
        while r < rows and c < cols:
            matrix[r, c] = value
            value += 1
            r += 1
            c += 1
        
        # Si possible, incrémente l'indice de départ de la ligne pour la prochaine diagonale
        if start_row + 1 < rows:
            start_row += 1
        else:
            # Sinon, commence une nouvelle diagonale en incrémentant l'indice de départ de la colonne
            start_col += 1

        # Remplir la diagonale suivante si elle commence dans la première ligne
        if start_row == rows and start_col < cols:
            r, c = 0, start_col
            # Remplit la diagonale à partir de la première ligne
            while r < rows and c < cols:
                if matrix[r, c] == 0:  # Ne pas écraser les valeurs existantes
                    matrix[r, c] = value
                    value += 1
                r += 1
                c += 1
            start_col += 1

    return matrix

# Appelle la fonction et affiche le résultat
matrix = create_incremental_diagonal_matrix()
print(matrix)
