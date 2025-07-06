from datetime import date


print("\033[1m-=-\033[0m" * 15)
print("\033[1m===ALISTAMENTO MILITAR===\033[0m")
atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento
if idade == 18:
    print("Você precisa se alistar!!")
elif idade < 18:
    saldo = idade - 18
    ano = atual + saldo
    print(f"Faltam {saldo} para você se alistar, e seu alistamento será em {ano}!")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Você já deveria ter se alistado a {saldo} anos! Seu alistamento foi em {ano}.")



