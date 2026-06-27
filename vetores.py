lista_alunos = [ "Davi", "Lucca", "Wesley", "Iasmym", "Felipe", "Romário", "Thiago", "DaviC", "Welinton","Elisson", "Vitória", "Samily", "Julianny", "Josias", "Lorrany", "Franciellen", "WRaphael", "Isabelle", "Ana Clara", "Alisson", "Joao Elias", "Thales"]

notas = [9.2, 8.6, 10, 9.3, 9.9]
print(lista_alunos[2])
# print("\n Aluno ".join(lista_alunos))

lista_alunos.sort() #ordenacao

for i in range(len(lista_alunos)):
    print(f" {i+1}° Aluno(a) {lista_alunos[i]}")


print("--------------------------")
print("Usando For")
print("--------------------------")
for aluno in lista_alunos:
    print(aluno)


print("--------------------------")
print("Usando While")
print("--------------------------")
contador = 0
while contador < len(lista_alunos):
    print(lista_alunos[contador])
    contador += 1
