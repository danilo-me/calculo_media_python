def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota

            print("⚠️ A nota deve estar entre 0 e 10.")

        except ValueError:
            print("⚠️ Digite apenas um número válido.")


print("=== Sistema de Notas do Aluno ===")

n1 = ler_nota(1)
n2 = ler_nota(2)

media = calcular_media(n1, n2)

print(f"\nA média final é: {media:.2f}")

if media >= 7:
    print("Status: ✅ APROVADO!")
else:
    print("Status: ❌ REPROVADO.")
