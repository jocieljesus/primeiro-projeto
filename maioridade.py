maiores_de_idade = 0
menores_de_idade = 0
for i in range(1, 8):

    ano_nasc = int(input(f"Digite o ano de nascimento da pessoa {i} :"))
    idade = 2026 - ano_nasc
    if idade >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1
print(f"Os maiores de idade são {maiores_de_idade} e os menores de idade são {menores_de_idade}")
