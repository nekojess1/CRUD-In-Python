alunos=[]                                 
professores=[]                            
disciplinas=[]                            
turmas=[]                              

# --------------------------------------------------------------------------------------#


def boas_vindas():                        
    nome=input('Digite o seu nome:\n')   
    print('\nSaudações, {}.\n'.format(nome))
    back_menu()

def back_menu():                         
    back=input('Você deseja acessar o menu?\n') 
    if back.lower()=='sim':  
        menu()                           
    elif back.lower()=='não':
        exit()                           
    else:
        print('Digite "Sim" ou "Não"')    
        back_menu()        

def wrong():                              
    print('Opção inválida!\nDigite uma opção dentro do campo escolhido.') 
    return back_menu()                    



# --------------------------------------C  R  E  A  T  E----------------------------------#

#GRAVANDO EM ARQUIVOS

#ESCREVE NO ARQUIVO-->GRAVA NO FINAL DO ARQUIVO-->FECHA O ARQUIVO

def write_disciplina():              
    arq = open("disciplinas.txt","a+")   
    for i in disciplinas:
        name=str(i[0])
        codigo=str(i[1])
        arq.write('%s %s\n'%(name,codigo))
    arq.close()                                   



def write_professor():               
    arq = open("professor.txt","a+")     
    for i in professores:
        name=str(i[0])
        cpf=str(i[1])
        dep=str(i[2])
        arq.write('%s %s %s\n'%(name, cpf, dep))
    arq.close()                          


def write_turma():                   
    arq = open("turma.txt","a+")      
    for i in turmas:
        cod_turma=str(i[0])
        periodo=str(i[1])
        cod_disciplina=str(i[2])
        cpf_prof=str(i[3])
        cpf_aluno=str(i[4])
        arq.write('%s %s %s %s %s\n'%(cod_turma, periodo, cod_disciplina,cpf_prof,cpf_aluno))
    arq.close()                        


def write_aluno():                  
    arq = open("alunos.txt","a+")        
    for i in alunos:
        name=str(i[0])
        cpf=str(i[1])
        arq.write('%s %s\n'%(name, cpf))
    arq.close()                          

# OBTENDO OS DADOS E GRAVANDO NA MEMÓRIA

# PEDE OS DADOS REQUERIDOS NOS CRITÉRIOS

def create_professor():                    
    while True:                         
        lista=[]
        name=input('Digite um nome:\n') #Pede um nome,cpf e departamento a ser adicionado 
        cpf=input('Digite um CPF:\n')
        dep=input('Digite o departamento:\n')
        continuar=input('Você deseja continuar?("Não" para voltar ao menu)\n')
        lista.append(name)
        lista.append(cpf)
        lista.append(dep)
        professores.append(lista)
        if continuar.lower()=='não':                       #para o loop
            break
    write_professor()
    print('Dado(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()    


def create_aluno():                       
    while True:                            
        lista=[]
        name=input('Digite um nome:\n') 
        cpf=input('Digite um CPF:\n')
        continuar=input('Você deseja continuar("Não" para voltar ao menu)\n')
        lista.append(name)
        lista.append(cpf)
        alunos.append(lista)
        if continuar.lower()=='não':
            break
    write_aluno()
    print('Dado(s) gravado(s) com sucesso!')
    return back_menu()      


def create_turma():                       
    while True:                         
        lista=[]
        cod_turma=input('Digite o código da turma:\n') 
        periodo=input('Digite o período:\n')
        disciplina=input('Digite o código da disciplina:\n')
        cpf_prof=input('Digite o CPF do professor:\n')
        cpf_aluno=input('Digite o CPF do aluno:\n')
        continuar=input('Você deseja continuar?("Não" para voltar ao menu)\n')
        lista.append(cod_turma)
        lista.append(periodo)
        lista.append(disciplina)
        lista.append(cpf_prof)
        lista.append(cpf_aluno)
        turmas.append(lista)
        if continuar.lower()=='não':                      
            break
    write_turma()
    print('Dado(s) gravado(s) com sucesso!')
    return back_menu()    


def create_disciplinas():                            
    while True:                           
        lista=[]
        name=input('Digite um nome:\n') 
        codigo=input('Digite um codigo de disciplina:\n')
        continuar=input('Você deseja continuar("Não" para voltar ao menu)\n')
        lista.append(name)
        lista.append(codigo)
        disciplinas.append(lista)
        if continuar.lower()=='não':
            break
    write_disciplina()
    print('Dados(s) gravado(s) com sucesso!')#avisa que os nomes foram gravados
    return back_menu()  

# ---------------------------------R E A D -----------------------------------#

def read_aluno():
    print("""Menu de opções

     0 - Ler todos os alunos
     1 - Buscar alunos
     2 - Voltar

     """)

    opção=input('Digite a opção desejada:')
    if opção == '0':
        print('-'*45)
        print ('Aluno              CPF')
        print('-'*45)
        for i in alunos:
            nome=i[0]
            cpf=i[1]
            print ('{}           {}'.format(nome,cpf))
    elif opção == '2':
        menu()
    elif opção == '1':
        nome=input('Digite um nome a ser procurado:\n')
        for i in alunos:
            if i[0]==nome:
                print('Nome: {}     CPF: {}'.format(i[0],i[1]))
        return back_menu()
    else:
        return wrong()


def read_professor():
    print("""Menu de opções

     0 - Ler todos os professores
     1 - Buscar professores 
     2 - Voltar
     
     """)

    opção=input('Digite a opção desejada:\n')
    if opção == '0':
        print('-'*45)
        print ('Professor            CPF         Departamento')
        print('-'*45)
        for i in professores:
            nome=i[0]
            cpf=i[1]
            departamento=i[2]
            print ('{}           {}             {}'.format(nome,cpf,departamento))
        return back_menu()
    elif opção == '2':
        menu()
    elif opção == '1':
        nome=input('Digite um nome a ser procurado:\n')
        for i in professores:
            if i[0]==nome:
                print('Nome: {}     CPF:    {} Departamento: {}'.format(i[0],i[1],i[2]))
        return back_menu()
    else:
        return wrong()
   

def read_disciplina():
    print("""Menu de opções

     0 - Ler todas as disciplinas
     1 - Buscar disciplina
     2 - Voltar
     
     """)
    
    opção=input('Digite a opção desejada:\n')
    if opção == '0':
        print('-'*45)
        print ('Código          Nome')
        print('-'*45)
        for i in disciplinas:
            code=i[0]
            nome=i[1]
            print ('{}           {}'.format(code,nome))
        return back_menu()
    elif opção == '2':
        menu()
    elif opção == '1':
        nome=input('Digite um código a ser procurado:\n')
        for i in disciplinas:
            if i[0]==nome:
                print('Código: {}     Nome: {}'.format(i[0],i[1]))
        return back_menu()
    else:
        return wrong()


def read_turma():
    print("""Menu de opções

     0 - Ler todas as turmas
     1 - Buscar turma
     2 - Voltar

     """)

    opção=input('Digite a opção desejada:\n')
    if opção == '0':
        print('-'*45)
        print ('Código da turma         Período         Código da disciplina         CPF(professor)             CPF(aluno)')
        print('-'*45)
        for i in turma:
           cod_turma=i[0]
           periodo=i[1]
           cod_disciplina=i[2]
           cpf_prof=i[3]
           cpf_aluno=i[4]
           print ('{}          {}           {}           {}           {}'.format(cod_turma,periodo,cod_disciplina,cpf_prof,cpf_aluno))
        return back_menu()
    elif opção == '2':
        menu()
    elif opção == '1':
        nome=input('Digite um código a ser procurado:\n')
        for i in turmas:
            if i[0]==nome:
                print('Código da turma: {}    Período:{}     Código da disciplina:{}    CPF(professor): {}      CPF(aluno): {}\n'.format(i[0],i[1],i[2],i[3],i[4]))
        return back_menu()
    else:
        return wrong()



# -------------------------------- M E N U -----------------------------------#
def menu(): 
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


   # OPÇÕES DO MENU


    option=input('Digite a opção desejada:\n') 

    if option=='0':                         
        exit()

    elif option=='1.1':                      
        return create_professor()

    elif option=='1.2':                      
        return create_disciplinas()

    elif option=='1.3':                     
        return create_aluno()

    elif option=='1.4':                     
        return create_turma()

    elif option=='2.1':
        read_professor()

    elif option=='2.2':
        read_disciplina()

    elif option=='2.3':
        read_aluno()

    elif option=='2.4':
        read_turma()

    else:
        return wrong()

boas_vindas()

