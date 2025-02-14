"""Trabalho front end 2. Atividade 1.
Aluna: Anne Izabelle - Curso: Ciência da Computação.
Professor: Glaucio."""

while True:

    dados_pessoas = []

    for i in range(1, 16):
        print("Pessoa", i)
        try:
            altura = float(input("Altura (m): "))
        except ValueError:
            print("Valor inválido! Digite um número.")
            continue
        genero = input("Gênero (M/F): ").strip().lower()
        while genero not in ['m', 'f']:
            print("Opção inválida! Use 'M' ou 'F'.")
            genero = input("Gênero (M/F): ").strip().lower()

        genero = 'masculino' if genero == 'm' else 'feminino'
        dados_pessoas.append((altura, genero))

    if not dados_pessoas:
        print("Nenhum dado foi registrado.")
        continue

    alturas = [p[0] for p in dados_pessoas]
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    alturas_homens = [p[0] for p in dados_pessoas if p[1] == 'masculino']
    if alturas_homens:
        media_homens = sum(alturas_homens) / len(alturas_homens)
    else:
        media_homens = 0

    total_mulheres = sum(1 for p in dados_pessoas if p[1] == 'feminino')

    # resultados abaixo
    print("\nResultados:")
    print("Maior altura:", maior_altura, "m")
    print("Menor altura:", menor_altura, "m")
    print("Média altura dos homens:", round(media_homens, 2), "m")
    print("Total de mulheres:", total_mulheres)

    # encerrando e reiniciando
    opcao = input("Deseja reiniciar? (S/N): ").strip().lower()
    if opcao != 's':
        print("Programa encerrado.")
        break
