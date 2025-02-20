def somas(n):
    if n == 1:
        return -n
    else:
        return -5 * somas(n - 1) + n

resul = somas(4)
print(resul)