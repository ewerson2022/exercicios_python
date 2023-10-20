matriz = [[0,0,0],  [0,0,0], [0,0,0]]

for  l in range(0,3):
    for c in range(0,3):
     matriz[l][c] = int(input(f'digite um valor[{l},{c}]: '))
        
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')