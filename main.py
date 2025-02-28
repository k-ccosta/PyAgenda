import json

MENU_OPCOES = ["Salvar", "Editar", "Deletar", "Favoritar", "Sair"]

def salvar_contato():
    
    contato = {
        "nome":input("\nDigite o nome do contato: "),
        "numero":int(input("Digite o número do contato: "))
    }

    with open("lista_de_contatos.txt", "a") as arq:
        arq.write(json.dumps(contato)+"\n")
def editar_contato():
    # 1. Ler todos os contatos do arquivo
    with open("lista_de_contatos.txt", "r") as arq:
        linhas = arq.readlines()

    # 2. Exibir cada contato com seu índice
    for indice, linha in enumerate(linhas):
        contato_dict = json.loads(linha)

        print(f"[{indice}] - Nome: {contato_dict['nome']} | Número: {contato_dict['numero']}")
    
    # 3. Solicitar o índice do contato que deseja editar
    indice = int(input("\nDigite o código do contato que deseja ajustar: "))

    # 4. Carregar a linha correspondente
    contato_editado = json.loads(linhas[indice])

    # 5. Pedir ao usuário os novos dados
    novo_nome = input(f"Digite o novo nome (atual: {contato_editado['nome']}): ")
    novo_numero = input(f"Digite o novo número (atual: {contato_editado['numero']}): ")

    # Se o usuário não digitar nada, mantém o valor anterior
    if novo_nome.strip():
        contato_editado['nome'] = novo_nome
    if novo_numero.strip():
        contato_editado['numero'] = int(novo_numero)

    # 6. Converter de volta para JSON e substituir na lista de linhas
    linhas[indice] = json.dumps(contato_editado) + "\n"

    # 7. Sobrescrever o arquivo com os dados atualizados
    with open("lista_de_contatos.txt", "w") as arq:
        arq.writelines(linhas)

def deletar_contato():
    # 1. Ler todos os contatos do arquivo
    with open("lista_de_contatos.txt", "r") as arq:
        linhas = arq.readlines()

    # 2. Exibir cada contato com seu índice
    for indice, linha in enumerate(linhas):
        contato_dict = json.loads(linha)

        print(f"[{indice}] - Nome: {contato_dict['nome']} | Número: {contato_dict['numero']}")
    
    # 3. Solicitar o índice do contato que deseja editar
    indice = int(input("\nDigite o código do contato que deseja ajustar: "))

    # 4. Remover o contato da lista usando pop() ou del
    linhas.pop(indice)

    # 7. Sobrescrever o arquivo com os dados atualizados
    with open("lista_de_contatos.txt", "w") as arq:
        arq.writelines(linhas)
    


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
        editar_contato()
    elif opcao_selecionada == 3:
        deletar_contato()
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