#   NÚMEROS PRIMOS

num = int(input("Digite um número: "))
tot = 0

for c in range(1, num + 1 ):
    if num % c == 0:
        print( end=' ')
        tot += 1 
    else:
         print( end=' ') 
    print('{}'.format(c), end=' ')
print("O número {} é divisível {} vezes".format(num, tot))
    
       
