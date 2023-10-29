from time import sleep
import numpy as np

print("=-"* 40)
print("seja bem vindo a")
print("calculadora juros simples e composto")
print("=-"* 40)
sleep(2)


print("aqui está as formulas de como calcular os juros simples e composto:")



print(f'''
    JUROS SIMPLES           JUROS COMPOSTO              NOMECLATURA
      
    M = c(1 + I.N)          M = C (1.I)^N               M = MONTANTE N = TEMPO 
    J = C.I.N               taxa de equivalencia        C = CAPITAL  I  = TAXA 
    M = C + J               (1+I)^N = (1+I)^N                 J = JUROS
''')


print("=-"* 40)
sleep(2)
print("agora escolha o que vc gostaria de calcular, basta digita a letra corresponde ao que se quer calcular:")
while True:
  
  resp = input('''
               
 [M] = MONTANTE 
 [C] = CAPITAL 
 [J] = JUROS
 [I]  = TAXA  
 [N] = TEMPO 
 
 

 digite aqui sua resposta: ''')

  print("=-"* 40)
  sleep(2)


  
  if resp in "Mm":
    
    
      print("você escolheu calcular o montante, digite os valores em seus respectivos campos: ")
      
      while True:
        
          c = (input("digite o valor do capital [C]:"))
          if c.isnumeric():
            c = float(c)
            pass
          else:
              print("erro escolha um número válido para o capital")
              continue
          
          
          while True: 
                i = (input("digite o valor da taxa [I]: "))
                try: 
                  i= int(i)
                  break
                except ValueError:
                  try:
                    i = float(i)
                    break
                  except ValueError:
                    print("isso não é um número valido")
                    continue
              
          while True: 
            n = (input("digite a quantidade de meses [N]: "))
            if n.isdigit():
              n = int(n)
              break
            else:
                print("erro escolha um número válido")
                continue
            
          
          i = i/100
          montante = c *( 1 + (i*n))
          
          print(f"visto os valores passado o seu montante será de: {montante:.2f}")
          exit()

      
  elif resp in "Jj":
    print("você escolheu calcular o juros, por favor entre com os respectivos valores em seu campo:")
    
    
    while True:

      c = (input("digite o valor do capital[c]: "))
      try: 
        c= int(c)
        break
      except ValueError:
        try:
          c = float(c)
          break
        except ValueError:
          print("isso não é um número valido")
          continue
          
           
    while True: 
            i = (input("digite o valor da taxa [I]: "))
            try: 
              i= int(i)
              break
            except ValueError:
              try:
                i = float(i)
                break
              except ValueError:
                print("isso não é um número valido")
              continue  
            
    while True: 
            n = (input("digite a quantidade de meses [N]: "))
            if n.isdigit():
              n = int(n)
              break
            else:
                print("erro escolha um número válido")
                continue
            
    i = i/100
    print(i)
    juros =   c *( i * n)
    print(f"visto os valores passado o seu juros será de: {juros:.2f}")
    exit()

   
  elif resp in "Cc":
    
    
    print("você escolheu calcular o capital, digite os valores em seus respectivos campos: ")
    
    while True:
      
        m = (input("digite o valor do montante [M]: "))
        try: 
          m= int(m)
          break
        except ValueError:
          try:
            m = float(m)
            break
          except ValueError:
            print("isso não é um número valido")
            continue
          
    while True: 
      
          i = (input("digite o valor da taxa [I]: "))
          try: 
            i= int(i)
            break
          except ValueError:
            try:
              i = float(i)
              break
            except ValueError:
              print("isso não é um número valido")
              continue  
    
    while True: 
            n = (input("digite a quantidade de meses [N]: "))
            if n.isdigit():
              n = int(n)
              break
            else:
                print("erro escolha um número válido")
                continue
    i = i /100
    print(i)
    capital = m / ((1 + i) ** n)
  
    print(f"visto os valores passado o seu juros será de: {capital:.2f}")
    exit()

        
  elif resp in "Ii":
    
    print("você escolheu calcular a taxa, por favor adicione os valores em seus designados campos: ")
    
    while True:
      
      while True:
          c = input("digite o valor do capital [C]: ")
          try:
            c = int(c) 
            break
          except ValueError:
            try:
              c = float(c)
              break
            except:
              ValueError
              print("erro, por favor digite um número válido")
              continue
            
            
      while True:
        m = input("digite o valor do montante [M]: ")
        try:
          m = int(m)
          break
        except ValueError:
          
          try:
            m = float(m)
            break
          except ValueError:
            print("erro, por favor digite um número válido")
            continue
            
            
      while True: 
            n = (input("digite a quantidade de meses [N]: "))
            if n.isdigit():
              n = int(n)
              break
            else:
                print("erro escolha um número válido")
                continue
  
      multi = c * n
      taxa  = m - c       
      taxa = taxa/multi
      taxa = (taxa *100)
     
      print(f"visto os valores passado a sua taxa ao ano será de: {taxa:.2%}")
      exit()


  elif resp in "Nn":
    
    print("você escolheu calcular o tempo, digite os valores em seus respectivos campos: ")
    
    while True:
      
      m = input("digite um valor para o montante [M]: ")
      try:
        m = int(m)
        break
      except ValueError:
        try:
          m = float(m)
          break
        except ValueError:
           print("erro escolha um número válido")
           continue
    
    while True:
      
      c = input("digite um valor para o capital [C]: ")
      try:
        c = int(c)
        break
      except ValueError:
        try:
          c = float(c)
          break
        except ValueError:
           print("erro escolha um número válido")
           continue
            
   
         
    while True: 
                i = (input("digite o valor da taxa [I]: "))
                try: 
                  i= int(i)
                  break
                except ValueError:
                  try:
                    i = float(i)
                    break
                  except ValueError:
                    print("isso não é um número valido")
                    continue
    i = i/100
    tempo = (np.log10(m/c)) / (np.log10(1+i))
    
    print(f"visto os valores passado o seu tempo será igual há: {tempo:.2f} meses")
    exit()

  else:
    print("por favor digite uma opção válida")