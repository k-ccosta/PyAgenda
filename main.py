import json

MENU_OPCOES = ["Salvar", "Editar", "Deletar", "Favoritar", "Sair"]

def salvar_contato():
    
    contato = {
        "nome":input("\nDigite o nome do contato: "),
        "numero":int(input("Digite o número do contato: "))
    }

    with open("lista_de_contatos.txt", "a") as arq:
        arq.write(json.dumps(contato)+"\n")

def exibir_titulo():
    mensagem = "Bem-vindo ao PyAgenda"
    borda = "*" * (len(mensagem) + 2)
    print(borda)
    print(mensagem)
    print(borda)
    print("")
def exibir_menu():
    for indice, opcao in enumerate(MENU_OPCOES, start=1):
        print(f"[{indice}] > {opcao}")
def obter_opcao_usuario():
    while True:
        try:
            opcao_selecionada = int(input("\nO que você deseja fazer? "))
            if opcao_selecionada in range(1, len(MENU_OPCOES) + 1):
                return opcao_selecionada
            else:
                print("\nERROR! Selecione uma opção disponível")
        except ValueError:
            print("\nERROR! Informe um número inteiro válido")
def executar_opcao(opcao_selecionada):
    if opcao_selecionada == 1:
        salvar_contato()
    elif opcao_selecionada == 2:
        print("Você escolheu: Editar")
    elif opcao_selecionada == 3:
        print("Você escolheu: Deletar")
    elif opcao_selecionada == 4:
        print("Você escolheu: Favoritar")
    else:
        print("Encerrando programa")

def main():
    exibir_titulo()
    exibir_menu()
    opcao_selecionada = obter_opcao_usuario()
    executar_opcao(opcao_selecionada)

if __name__ == "__main__":
    main()