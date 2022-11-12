'''Este código em Python verifica e exibe na tela quantos e quais são os números primos entre 1 e n, sendo n dado pelo usuário.'''

#recebendo o número n:
n = int(input("Quero saber quantos números primos há entre 1 e: "))
#lista dos números primos entre 1 e n:
primos = []

print("\n---NÚMEROS PRIMOS ENTRE 1 E {}:---\n".format(n))

#números de 1 a n:
for i in range(1, n+1):
    #variável divisores, que contém a quantidade de números que dividem i:
    divisores = 0
    #para cada i, verificaremos quantos números entre 1 e i o dividem. Para cada divisor, adicionamos 1 à variável divisores.
    for j in range(i, 0, -1):
        if i%j==0:
            divisores += 1
    #se i tem dois divisores (1 e ele mesmo), então i é primo e deve ser adicionado à lista primos.
    if divisores == 2:
        primos.append(i)
print("HÁ {} NÚMEROS PRIMOS ENTRE 1 E {}. \nLISTA DOS NÚMEROS PRIMOS ENTRE 1 E {}: {}".format(len(primos), n, n, primos))
