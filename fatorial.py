n1 = int(input('digite um número para calcular seu fatorial: '))
c = n1
f = 1

print(f"calculando o fatorial de {n1}! = ", end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c =c -1
print(f'{f}')