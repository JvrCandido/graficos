import matplotlib.pyplot as plt


# ==========================
# FUNÇÃO: Coletar dados
# ==========================
def coletar_dados():
    categorias = []
    valores = []

    print("\n=== INSERÇÃO DE DADOS ===\n")

    while True:
        try:
            qtd = int(input("Quantas categorias você deseja inserir? "))
            if qtd <= 0:
                print("Digite um número maior que zero.")
                continue
            break
        except:
            print("Digite um número válido.")

    print()

    for i in range(qtd):
        nome = input(f"Nome da categoria {i+1}: ")

        while True:
            try:
                valor = float(input(f"Valor de {nome}: "))
                if valor < 0:
                    print("Digite um valor positivo.")
                    continue
                break
            except:
                print("Digite um número válido.")

        categorias.append(nome)
        valores.append(valor)
        print()

    return categorias, valores


# ==========================
# FUNÇÃO: Mostrar relatório
# ==========================
def mostrar_relatorio(categorias, valores):
    total = sum(valores)

    print("\n========== RELATÓRIO ==========\n")

    for i in range(len(categorias)):
        porcentagem = (valores[i] / total) * 100
        print(f"{categorias[i]}: {valores[i]} → {porcentagem:.2f}%")

    print(f"\nTOTAL: {total}")
    print("===============================\n")


# ==========================
# FUNÇÃO: Gráfico Pizza
# ==========================
def grafico_pizza(categorias, valores):
    plt.figure()

    plt.pie(
        valores,
        labels=categorias,
        autopct="%1.1f%%",
        startangle=90,
        shadow=True
    )

    plt.title("Gráfico de Pizza - Porcentagem")
    plt.axis("equal")

    plt.show()


# ==========================
# FUNÇÃO: Gráfico Barras
# ==========================
def grafico_barras(categorias, valores):
    plt.figure()

    plt.bar(categorias, valores)

    plt.title("Gráfico de Barras - Valores")
    plt.xlabel("Categorias")
    plt.ylabel("Quantidade")

    for i in range(len(valores)):
        plt.text(i, valores[i], valores[i],
                 ha='center', va='bottom')

    plt.show()


# ==========================
# FUNÇÃO: Salvar relatório
# ==========================
def salvar_relatorio(categorias, valores):
    total = sum(valores)

    nome_arquivo = "relatorio_graficos.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write("RELATÓRIO DE DADOS\n")
        arquivo.write("====================\n\n")

        for i in range(len(categorias)):
            porcentagem = (valores[i] / total) * 100

            linha = f"{categorias[i]}: {valores[i]} → {porcentagem:.2f}%\n"
            arquivo.write(linha)

        arquivo.write(f"\nTOTAL: {total}\n")

    print(f"\nRelatório salvo em: {nome_arquivo}\n")


# ==========================
# FUNÇÃO: Menu
# ==========================
def menu():
    print("===================================")
    print("   SISTEMA DE GRÁFICOS EM PYTHON")
    print("===================================")
    print("1 - Inserir dados")
    print("2 - Mostrar relatório")
    print("3 - Gerar gráfico de pizza")
    print("4 - Gerar gráfico de barras")
    print("5 - Salvar relatório em arquivo")
    print("0 - Sair")
    print("===================================")


# ==========================
# PROGRAMA PRINCIPAL
# ==========================
def main():

    categorias = []
    valores = []

    while True:

        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            categorias, valores = coletar_dados()

        elif opcao == "2":

            if not categorias:
                print("\nInsira os dados primeiro!\n")
            else:
                mostrar_relatorio(categorias, valores)

        elif opcao == "3":

            if not categorias:
                print("\nInsira os dados primeiro!\n")
            else:
                grafico_pizza(categorias, valores)

        elif opcao == "4":

            if not categorias:
                print("\nInsira os dados primeiro!\n")
            else:
                grafico_barras(categorias, valores)

        elif opcao == "5":

            if not categorias:
                print("\nInsira os dados primeiro!\n")
            else:
                salvar_relatorio(categorias, valores)

        elif opcao == "0":

            print("\nEncerrando o sistema...")
            print("Obrigado por usar!\n")
            break

        else:
            print("\nOpção inválida.\n")


# ==========================
# EXECUÇÃO
# ==========================
if __name__ == "__main__":
    main()
