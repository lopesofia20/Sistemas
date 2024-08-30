def palindromo(string):
    size = len(string)
    if size == 0:
        return False
    return all(string[i] == string[size - i - 1] for i in range(0, size // 2))

texto1 = "arara"
texto2 = "capivara"

print (palindromo(texto1))

print (palindromo(texto2))