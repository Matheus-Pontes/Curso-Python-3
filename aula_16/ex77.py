#   coloque numa tupla varias palavras e
#   diga quais vogais aparecem em cada palavra



palavras = ("aprender",
"programar",
"linguagem", 
"pyton")

print("-"*30)
print(f"{'Vogais das palavras':^30}")
print("-"*30)

#   CADA PALAVRA É UMA LISTA

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos", end=" ")
    for letras in p:
        if letras.lower() in "aeiou":
            print(letras, end=" ")
