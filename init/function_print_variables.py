# comando print
print("print", "do", "python", sep="-")
print("print", "do", "python", sep="-", end="\n")
print("print", "do", "python", sep="-", end="END")
#definindo variaveis
language = "python"
content = "print do"
#fim variaveis
print(type(language))
print(content, language)

## Exercício Alura "Personalizando a saída"
subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")

# qual será a saída do comando ´print´: 
# Resposta: Python_é_fantástico!

# Exércicio Alura: "Imprimindo datas"
dia = 15
mes = 10
ano = 2015

#  Sem alterar as variáveis e sem passar nenhuma string adicional à função print(), como faríamos para ter como resultado da impressão, uma data formatada: 15/10/2015

# Reposta:
print(dia, mes, ano, sep="/")