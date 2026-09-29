# ***Cálculo de Média***

Programa desenvolvido em Python para calcular a média de duas notas de um aluno e informar se ele foi aprovado ou reprovado.

# ***Tecnologias Utilizadas***

**Python 3**
```
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
```

**Como Funciona:**

O programa solicita duas notas, realiza o cálculo da média e apresenta o resultado.

A nota deve estar entre 0 e 10.

Média maior ou igual a 7: Aprovado

Média menor que 7: Reprovado

# ***Como Instalar e Executar***

Clone o repositório:

git clone URL_DO_SEU_REPOSITORIO


Entre na pasta do projeto:

cd calculo-de-media


Execute o programa:

python main.py

#   ***Exemplo de Uso***
=== Sistema de Notas do Aluno ===
Digite a 1ª nota (0 a 10): 8
Digite a 2ª nota (0 a 10): 7

A média final é: 7.50
Status: APROVADO!

# ***Autor e Contato***

Danilo Menino do Nascimento

Linkedin: https://www.linkedin.com/in/.danimome

Watsapp: (11) 95843-0364
