from math import cos

resp = 1
lista_usuario = []

while (resp != 0):
    print("1 - Inserir usuário")
    print("2 - Alterar usuário")
    print("3 - Remover usuário")
    print("4 - Exibir usuário")
    opc = int(input("Digite a opção desejada (1 - 4)"))


    if (opc == 1):
        try:
            codigo =  int(input("Digite o codogio do usuário:"))
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuario: "))
            senha = input("Digite a senha do usário: ")
        except ValueError:
            print("Digite um valor numerico para o cógido")
        else:
            usuario = {'Codigo': codigo, 'Nome':nome, 'Idade': idade, 'Senha': senha}
            lista_usuario.append(usuario)
        finally:
            print("Operação finalizada!")
    elif (opc == 2):
        codigo =  int(input("Digite o codogio do usuário, que deseja alterar: "))
        pos = -1
        for i in range (len(lista_usuario)):
            if  (lista_usuario[i]['Código']== codigo):
                pos = i
        if (pos != -1):
            try:
                nome = input("Digite o nome do usuário: ")
                idade = int(input("Digite a idade do usuario: "))
                senha = input("Digite a senha do usário: ")
            except ValueError:
                print("Digite um valor numerico para o cógido")
            else:
                lista_usuario[pos]['Nome'] == nome
                lista_usuario[pos]['Idade'] == idade
                lista_usuario[pos]['Senha'] == senha
            finally:
                print("Operação finalizada!")

        else:
            print("Usuário não encontrado!")
    elif (opc == 3):
        codigo =  int(input("Digite o codogio do usuário, que deseja alterar: "))
        pos = -1
        for i in range(len(lista_usuario)):
            if  (lista_usuario[i]['Código']== codigo):
                pos = i
        if(pos != -1):
            lista_usuario.pop(pos)
        else:
            print("Usuário não encontrado!")
    elif (opc == 4):
        print(lista_usuario)

    resp = int(input("Deseja continuar? 1 - SIM  2 - Não"))
