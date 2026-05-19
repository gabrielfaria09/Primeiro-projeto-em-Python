def saudação(nome):
    return f"Olá, {nome}!"

print(saudação("Davi"))

soma = lambda x, y: x+ y
print(soma(3,5))

lista = [1,2,3,4,5,6,7,8,9]
pares = list(filter(lambda x: x%2 == 0, lista))
print(pares)