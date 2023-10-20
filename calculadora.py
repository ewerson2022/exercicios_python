print("=-"*24)
print("BEM VINDO A CALCULADORA BÁSICA")
print("=-"*24)


while True:
    
    n1 = (input("escolha o número que desejar ver a tabuada: "))
    if n1.isnumeric():
        n1 = int(n1)
        pass
    else:
        print("erro escolha um número inteiro")
        continue
    
    while True:
        resp = (input('''Escolha a operação matematica de 1 a 4:
        

        [1] ADIÇÃO
        [2] SUBTRAÇÃO
        [3] MULTIPLICAÇÃO
        [4] DIVISÃO

        Insira sua resposta:'''))
        
        if resp.isnumeric():
            resp = int(resp)
            pass
        if resp != 1 and resp !=2 and resp !=3 and resp != 4: 
            print("erro escolha um número de 1 a 4")
            continue
    
        print(type(n1))
        print(type(resp))
        

        if resp == 1:
            print("=-"*24)
            print("TABUADA DE ADIÇÃO")
            c = 0
            while c <= 10:
                for c in range(1,11):
                    r = n1+c
                    print(f"{n1} + {c} = {r}")
                c = c + 1
            break
        
        
        if resp == 2:
            print("=-"*24)
            print("TABUADA DE SUBTRAÇÃO")
            c = 0
            while c <= 10:
                for c in range(1,11):
                    r = n1 - c
                    print(f"{n1} - {c} = {r}")
                c = c + 1
            break   
        
        
        if resp == 3:
            print("=-"*24)
            print("TABUADA DE MULTIPLICAÇÃO")
            c  = 0
            while c <= 10:
                for c in range(1,11):
                    r = n1 * c
                    print(f"{n1} * {c} = {r}")
                c = c + 1
            break
        
        if resp == 4:
            print("=-"*24)
            print("TABUADA DE DIVISÃO")
            c = 0
            while c <= 10:
                for c in range(1,11):
                    r = n1 / c
                    print(f"{n1} / {c} = {r}")
                c = c + 1
            break           
        
    break       
                        
