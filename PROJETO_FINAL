#LISTAS PARA ARMAZENAR OS DADOS EM MEMÓRIA

alunos=[]                                 
professores=[]                            
disciplinas=[]                            
turmas=[]                              

# =============================== E X T R A S =============================== #

# FUNÇÃO PARA DAR BOAS VINDAS AO USUÁRIO

def boas_vindas():                        
    nome=input('Digite o seu nome:\n')   
    print('\nSaudações, {}.\n'.format(nome))
    back_menu()

# FUNÇÃO DE VOLTAR AO MENU    

def back_menu():                         
    back=input('Você deseja acessar o menu?\n') 
    if back.lower()=='sim':  
        menu()                           
    elif back.lower()=='não':
        exit()                           
    else:
        print('Digite "Sim" ou "Não"')    
        back_menu() 

# FUNÇÃO PARA DIZER QUE A OPÇÃO ESTÁ INVÁLIDA  

def wrong():                              
    print('Opção inválida!\nDigite uma opção dentro do campo escolhido.') 
    return back_menu()                    

# -----------------> FUNÇÕES USADAS NO CREATE DE TURMA

def cpf_alunos():
    teste_vazio=len(alunos)
    if teste_vazio==0:
        print('Não há alunos cadastrados!\nVá para a área de criação e adicione novos alunos!')
        return back_menu()
    adicionavel=False
    cpf_aluno=input('Digite o CPF do aluno:\n')
    for i in range(len(alunos)):
       teste=alunos[i]
       if cpf_aluno in teste:
           print('Aluno adicionado com sucesso.\n')
           adicionavel=True
           return cpf_aluno
           
    if adicionavel==False:
        print('Aluno não encontrado. Tente novamente.\n')
        return cpf_alunos()

def cpf_professores():
    teste_vazio=len(professores)
    if teste_vazio==0:
        print('Não há professores cadastrados!\nVá para a área de criação e adicione novos professores!')
        return back_menu()
    adicionavel=False
    cpf_prof=input('Digite o CPF do professor:\n')
    for i in range(len(professores)):
       teste=professores[i]
       if cpf_prof in teste:
           print('Professor adicionado com sucesso.\n')
           adicionavel=True
           return cpf_prof
           
    if adicionavel==False:
        print('Professor não encontrado. Tente novamente.\n')
        return cpf_professores()

def codigo_disciplina():
    teste_vazio=len(disciplinas)
    if teste_vazio==0:
        print('Não há disciplinas cadastrados!\nVá para a área de criação e adicione novas disciplinas!')
        return back_menu()
    adicionavel=False
    codigo=input('Digite o código de disciplina:\n')
    for i in range(len(disciplinas)):
       teste=disciplinas[i]
       if codigo in teste:
           print('Código de disciplina adicionado com sucesso.\n')
           adicionavel=True
           return codigo
           
    if adicionavel==False:
        print('Código de disciplina não encontrado. Tente novamente.\n')
        return codigo_disciplina()



# ============================= C  R  E  A  T E ============================= #


# -----------------> GRAVANDO EM ARQUIVOS


# ESCREVE NO ARQUIVO-->GRAVA NO FINAL DO ARQUIVO-->FECHA O ARQUIVO

# CRIA UM ARQUIVO DE DISCIPLINA 

def write_disciplina():              
    arq = open("disciplinas.txt","a+")   
    for i in disciplinas:
        name=str(i[0])
        codigo=str(i[1])
        arq.write('%s %s\n'%(name,codigo))
    arq.close()                                   

# CRIA UM ARQUIVO DE PROFESSOR

def write_professor():               
    arq = open("professor.txt","a+")     
    for i in professores:
        name=str(i[0])
        cpf=str(i[1])
        dep=str(i[2])
        arq.write('%s %s %s\n'%(name, cpf, dep))
    arq.close()                          

# CRIA UM ARQUIVO DE TURMA

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

# CRIA UM ARQUIVO DE ALUNO

def write_aluno():                  
    arq = open("alunos.txt","a+")        
    for i in alunos:
        name=str(i[0])
        cpf=str(i[1])
        arq.write('%s %s\n'%(name, cpf))
    arq.close()                          



# -----------------> GRAVANDO NA MEMÓRIA


# ADICIONA NOVOS DADOS DE PROFESSORES

def create_professor():                    
    while True:                         
        lista=[]
        name=input('Digite um nome:\n') 
        cpf=input('Digite um CPF:\n')
        dep=input('Digite o departamento:\n')
        continuar=input('Você deseja continuar adicionando?(Tecle ENTER para continuar)\n')
        lista.append(name)
        lista.append(cpf)
        lista.append(dep)
        professores.append(lista)
        if continuar.lower()=='não':
            back_menu()

    # CHAMA  A FUNÇÃO DE SALVAR EM ARQUIVO
        
    write_professor()
    print('Dado(s) gravado(s) com sucesso!')
    return menu()   

# ADICIONA NOVOS DADOS DE ALUNOS

def create_aluno():                       
    while True:                            
        lista=[]
        name=input('Digite um nome:\n') 
        cpf=input('Digite um CPF:\n')
        continuar=input('Você deseja continuar adicionando?(Tecle ENTER para continuar)\n')
        lista.append(name)
        lista.append(cpf)
        alunos.append(lista)
        if continuar.lower()=='não':
            back_menu()
    
    # CHAMA  A FUNÇÃO DE SALVAR EM ARQUIVO

    write_aluno()
    print('Dado(s) gravado(s) com sucesso!')
    return menu()      

# ADICIONA NOVOS DADOS DE TURMAS

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


# ADICIONA NOVOS DADOS DE DISCIPLINAS

def create_turma():                            
    lista=[]
    codigo=input('Digite o código da turma:\n')
    periodo=input('Digite o período da turma:\n')
    cod_disciplina=codigo_disciplina()
    cpf_prof=cpf_professores()
    cpf_aluno=cpf_alunos()


    lista.append(codigo)
    lista.append(periodo)
    lista.append(cod_disciplina)
    lista.append(cpf_prof)
    lista.append(cpf_aluno)


    turmas.append(lista)
    write_turma()

# ================================= R E A D ============================== #


# FAZENDO A LEITURA DOS DADOS CONTIDOS NA MEMÓRIA E EM ARQUIVOS !!!!!!!!************LEMBRAR DE TERMINAR EM ARQUIVOS MAIS TARDE ****************!!!!!!!

# MENU DE OPÇÕES 

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
            print ('{}              {}'.format(nome,cpf))
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

# MENU DE OPÇÕES 

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
   
# MENU DE OPÇÕES 

def read_disciplina():
    print("""Menu de opções

     0 - Ler todas as disciplinas
     1 - Buscar disciplina
     2 - Voltar
     
     """)
    
    opção=input('Digite a opção desejada:\n')
    if opção == '0':
        print('-'*45)
        print ('Nome          Código')
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

# MENU DE OPÇÕES 

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



# ============================= U P D A T E ============================ #


# FAZ ALTERAÇÕES NOS DADOS

def update_professor():
    lista=[]
    atualizavel=False
    cpf=input('Digite o CPF de um professor a ser atualizado:')
    
    # EXCLUI DA MEMÓRIA 

    for i in range(len(professores)):
        print(professores[i])
        if professores[i][1]==cpf:
            del professores[i]
            atualizavel=True

    # CÓDIGO DE DISCIPLINA NÃO ENCONTRADO

    if atualizavel==False:
        print('Professor não encontrado')
        return update_professor()

    print('Digite novos dados a serem atualizados:')
    name=input('Digite o nome de um professor:')
    cpf=input('Digite o CPF de um professor:')
    dep=input('Digite o departamento de um professor:')
    
    # SALVA EM MEMÓRIA

    lista.append(name)
    lista.append(cpf)
    lista.append(dep)
    professores.append(lista)

    # SALVA EM ARQUIVOS

    write_professor()
    print('Dado(s) gravado(s) com sucesso!')
    
    voltar=input('Você deseja continuar atualizando?')

    if voltar.lower()=='sim':
        update_professor()
    else:
        back_menu()



def update_disciplina():
    lista=[]
    atualizavel=False
    codigo=input('Digite o código de uma disciplina a ser atualizada:')
    
    # EXCLUI DA MEMÓRIA 

    for i in range(len(disciplinas)):
        if disciplinas[i][1]==codigo:
            del disciplinas[i]
            atualizavel=True

    # CÓDIGO DE DISCIPLINA NÃO ENCONTRADO

    if atualizavel==False:
        print('Código não encontrado')
        return update_disciplina()
    
    print('Digite novos dados a serem atualizados:')
    nome=input('Digite o nome de uma disciplina:')
    cpf=input('Digite o código de uma disciplina:')

    # CÓDIGO DE DISCIPLINA NÃO ENCONTRADO

    if atualizavel==False:
        print('Código não encontrado')
        return update_disciplina()
    
    # SALVA EM MEMÓRIA

    lista.append(name)
    lista.append(codigo)
    disciplinas.append(lista)

    # SALVA EM ARQUIVOS

    write_disciplina()
    print('Dado(s) gravado(s) com sucesso!')
    
    voltar=input('Você deseja continuar atualizando?')

    if voltar.lower()=='sim':
        update_disciplina()
    else:
        back_menu()



def update_aluno():
    for i in professores():
        if i[1]==cpf:
            del professores[i]
            atualizavel=True
    lista=[]
    atualizavel=False
    cpf=input('Digite o CPF de um professor a ser atualizado:')
    
    # EXCLUI DA MEMÓRIA 

    for i in professore:
        if i[1]==cpf:
            del professores[i]
            atualizavel=True
    print('Digite novos dados a serem atualizados:')
    nome=input('Digite o nome de um professor:')
    cpf=input('Digite o CPF de um professor:')
    dep=input('Digite o departamento de um professor:')
    
    # CÓDIGO DE DISCIPLINA NÃO ENCONTRADO

    if atualizavel==False:
        print('Código não encontrado')
        return update_disciplina()
    
    # SALVA EM MEMÓRIA

    lista.append(name)
    lista.append(cpf)
    lista.append(dep)
    professores.append(lista)

    # SALVA EM ARQUIVOS

    write_professor()
    print('Dado(s) gravado(s) com sucesso!')
    
    voltar=input('Você deseja continuar atualizando?')

    if voltar.lower()=='sim':
        update_professor()
    else:
        back_menu()



def update_turma():
    lista=[]
    atualizavel=False
    cpf=input('Digite o CPF de um professor a ser atualizado:')
    
    # EXCLUI DA MEMÓRIA 

    for i in professore:
        if i[1]==cpf:
            del professores[i]
            atualizavel=True
    print('Digite novos dados a serem atualizados:')
    nome=input('Digite o nome de um professor:')
    cpf=input('Digite o CPF de um professor:')
    dep=input('Digite o departamento de um professor:')
    
    # CÓDIGO DE DISCIPLINA NÃO ENCONTRADO

    if atualizavel==False:
        print('Código não encontrado')
        return update_disciplina()
    
    # SALVA EM MEMÓRIA

    lista.append(name)
    lista.append(cpf)
    lista.append(dep)
    professores.append(lista)

    # SALVA EM ARQUIVOS

    write_professor()
    print('Dado(s) gravado(s) com sucesso!')
    
    voltar=input('Você deseja continuar atualizando?')

    if voltar.lower()=='sim':
        update_professor()
    else:
        back_menu()




# =========================== D E L E T E ============================ #

# DELETA CERTOS DADOS ESCOLHIDOS PELO USUÁRIO

def delete_professor():
    excluido=False
    cpf=input('Digite um CPF de um professor a ser excluído:')
    for i in professores:
        if i[1]==cpf:
            del professores[i]
            print("Professor excluído com sucesso!")
            excluido=True
    if excluido==False:
        print('CPF não encontrado!')
    pergunta=input('Deseja continuar excluindo?')
    if pergunta.lower()=='sim':
        return delete_professor()
    else:
        return back_menu()


def delete_disciplina():
    excluido=False
    codigo=input('Digite um código de uma disciplina a ser excluído:')
    for i in disciplinas:
        if i[1]==codigo:
            del disciplinas[i]
            print("Disciplina excluída com sucesso!")
            excluido=True
    if excluido==False:
        print('Codigo não encontrado!')
    pergunta=input('Deseja continuar excluindo?')
    if pergunta.lower()=='sim':
        return delete_disciplina()
    else:
        return back_menu()


def delete_aluno():
    excluido=False
    cpf=input('Digite um CPF de um aluno a ser excluído:')
    for i in alunos:
        if i[1]==cpf:
            del alunos[i]
            print("Aluno excluído com sucesso!")
            excluido=True
    if excluido==False:
        print('CPF não encontrado!')
    pergunta=input('Deseja continuar excluindo?')
    if pergunta.lower()=='sim':
        return delete_aluno()
    else:
        return back_menu()


def delete_turma():
    excluido=False
    cpf=input('Digite um CPF a ser excluído:')
    for i in professores:
        if i[1]==cpf:
            del professores[i]
            print("Professor excluído com sucesso!")
            excluido=True
    if excluido==False:
        print('CPF não encontrado!')
    pergunta=input('Deseja continuar excluindo?')
    if pergunta.lower()=='sim':
        return delete_professor()
    else:
        return back_menu()


# ============================== M E N U =============================== #

# ABRE O MENU DE OPÇÕES 

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


   # SELEÇÃO DE OPÇÕES DO MENU

   # RETORNAM FUNÇÕES JÁ EXISTENTES 


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

    elif option=='3.1':
        update_professor()

    elif option=='3.2':
        update_disciplina()

    elif option=='3.3':
        update_aluno()

    elif option=='3.4':
        update_turma()

    elif option=='4.1':
        delete_professor()

    elif option=='4.2':
        delete_disciplina()

    elif option=='4.3':
        delete_aluno()

    elif option=='4.4':
        delete_turma()

    else:
        return wrong()

# CHAMA A FUNÇÃO BOAS VINDAS, PARA RECEPCIONAR O USUÁRIO

boas_vindas()

