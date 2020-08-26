#   Adicionando e ordenando valores da lista


num = []

for c in range(0, 5):

    n = int(input("Digite um valor: "))

    #   Se for o primeiro valor adiciona
    #   ou no meio ou no fim 

    if c == 0 or num[len(num) - 1] :
        num.append(n)
        print("Adicionado ao final da lista...")
    
    else:
        pos = 0
        #   Andar pelo vetor 
        
        while pos < len(num):
            
            if n <= num[pos]:
                #   Posição expecifica
                num.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
    
    
print(f"Os valores digitados em ordem foram {num}")