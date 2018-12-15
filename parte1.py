alunos=[]                                 #lista com os nomes salvos na memória 
professores=[]                            #lista com os nomes salvos na memória 
disciplinas=[]                            #lista com as materias salvos na memória 
turmas=[]                                 #lista com as turmas salvos na memória 

def boas_vindas():                        #Recolhe o nome do usuário e dá boas vindas para ele
    nome=input('Digite o seu nome:\n')    #Pede o nome do usuário
    print('\nSaudações, {}.'.format(nome))#Saudações usuário! \o/
    return back_menu()                    #pergunta se deseja acessar o menu

def back_menu():                          #Faz voltar ao menu
    back=input('Você deseja acessar o menu?\n') #pergunta se deseja acessar o menu
    if back.lower()=='sim':  
        menu()                            #retorna o menu
    elif back.lower()=='não':
        exit()                            #fecha o programa
    else:
        print('Digite "Sim" ou "Não"')    #A resposta foi inválida, precisará perguntar mais uma vez
        back_menu()                       #retorna a função
#                    C  R  E  A  T  E
def write_disciplina(texto):              # Escreve no arquivo
    arq = open("disciplinas.txt","a+")    # grava no final do arquivo
    arq.writelines('\n'+texto)            # escreve no arquivo
    arq.close()                           # Fecha o arquivo

def write_professor(texto):               # Escreve no arquivo
    arq = open("professor.txt","a+")      # grava no final do arquivo
    arq.writelines('\n'+texto)            # escreve no arquivo
    arq.close()                           # Fecha o arquivo

def write_turma(texto):                   # Escreve no arquivo
    arq = open("turma.txt","a+")         # grava no final do arquivo
    arq.writelines('\n'+texto)            # escreve no arquivo
    arq.close()                           # Fecha o arquivo

def write_aluno(texto):                  # Escreve no arquivo
    arq = open("alunos.txt","a+")         # grava no final do arquivo
    arq.writelines('\n'+texto)            # escreve no arquivo
    arq.close()                           # Fecha o arquivo

def wrong():                              #Opção fora da lista do menu
    print('Opção inválida!\nDigite uma opção dentro do campo escolhido. Exemplo:2.2') #Comenta sobre a opção inválida e mostra uma opção correta 
    return back_menu()                    #Retorna ao menu 

#OPÇÃO DE CRIAR

def create_professor():                     #adiciona novos dados
    while True:                             #cria um loop para adicionar vários alunos simultaneamente 
        name=input('Digite um nome, cpf e departamento a ser adicionado: ("0" para sair)\n').split() #Pede um nome,cpf e departamento a ser adicionado 
        if name=='0':                       #para o loop
            break
        for i in name:
            professores.append(i)
                                  #adiciona os nomes em uma lista na memória
        write_professor(name)               #adiciona os nomes em arquivos
    print('Nome(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()    
def create_aluno():                        #adiciona novos dados
    while True:                            #cria um loop para adicionar vários alunos simultaneamente 
        name=input('Digite o código e o nome a ser adicionado: ("0" para sair)\n') #Pede um nome a ser adicionado 
        if name=='0':                      #para o loop
            break
        alunos.append(name)                #adiciona os nomes em uma lista na memória
        write_aluno(name)                  #adiciona os nomes em arquivos
    print('Nome(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()                    #retorna a função para voltar ao menu

def create_turma():                       #adiciona novos dados
    while True:                           #cria um loop para adicionar vários alunos simultaneamente 
        dados=input('Digite um nome a ser adicionado: ("0" para sair)\n').split() #Pede um nome a ser adicionado 
        if name=='0':                     #para o loop
            break
        turmas.append(name)                #adiciona os nomes em uma lista na memória
        write_turma(name)                  #adiciona os nomes em arquivos
    print('Nome(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()                    #retorna a função para voltar ao menu

def create_disciplinas():                             #adiciona novos dados
    while True:                           #cria um loop para adicionar vários alunos simultaneamente 
        name=input('Digite um nome a ser adicionado: ("0" para sair)\n') #Pede um nome a ser adicionado 
        if name=='0':                     #para o loop
            break
        disciplinas.append(name)                #adiciona os nomes em uma lista na memória
        write_disciplina(name)                       #adiciona os nomes em arquivos
    print('Nome(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()                    #retorna a função para voltar ao menu


def menu(): #apresenta o menu com as suas funções
    print('''Bem vind@ ao menu! =)        

        0 - Sair --> Fecha o programa
        1 - Create --> Criação de dados. 
             1.1 - Professores 
             1.2 - Disciplinas
             1.3 - Alunos
             1.4 - Turma
        2 - Read --> Consultar dados.
             2.1 - Professores 
             2.2 - Disciplinas
             2.3 - Alunos
             2.4 - Turma
        3 - Update --> Modificar dados.
             3.1 - Professores 
             3.2 - Disciplinas
             3.3 - Alunos
             3.4 - Turma
        4 -  Delete --> Destruir dados.
             4.1 - Professores 
             4.2 - Disciplinas
             4.3 - Alunos
             4.4 - Turma
        5 - Generate --> Gerador de listas, atas e etc.
          ''')

          
    option=input('Digite a opção desejada:\n') #pergunta a função desejada

    if option=='0':                          #sai do programa
        exit()
    elif option=='1.1':                      #cria dados -> professor
        return create_professor()
    elif option=='1.2':                      #cria dados -> disciplina
        return create_disciplinas()
    elif option=='1.3':                      #cria dados -> aluno
        return create_aluno()
    elif option=='1.4':                      #cria dados -> turma
        return create_turma()
    elif option=='2.1':
        print('-------Alunos-------')
        for i in alunos:
            print(i)
    elif option=='2.2':
        print('-------Alunos-------')
        for i in names:
            print(i)
    elif option=='2.3':
        print('-------Alunos-------')
        for i in names:
            print(i)
    elif option=='2.4':
        print('-------Alunos-------')
        for i in professores:
            print(i)
        print(professores)

    else:
        return wrong()
boas_vindas()

