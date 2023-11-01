import csv

def adicionarContato(user_login):
  while True:
    
      base_dado_local = {
        "nome":[],
        "login":[],
        "senha":[]
      }
    
      with open('dado.csv', 'r', newline = '') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
          base_dado_local['nome'].append(linha['nome'])
          base_dado_local['login'].append(linha['login'])
          base_dado_local['senha'].append(linha['senha'])
    
      indice = base_dado_local['login'].index(user_login)
      nome_titular = base_dado_local['nome'][indice]
    
      agenda = {
        "nome":[],
        "telefone":[]
      }
    
      nome = input('Nome:  ')
      agenda['nome'].append(nome)
    
      numero_telefone = input('Numero de Telefone:  ')
      agenda['telefone'].append(numero_telefone)
    
      nome_arq = 'agenda_de_' + nome_titular + '.csv'
      with open(nome_arq, mode = 'w', newline = '') as arquivo_csv: #abre arquivo
          escrever_csv = csv.writer(arquivo_csv)     
          escrever_csv.writerow(['nome','telefone'])
              
          for i in range(len(agenda['nome'])):
            escrever_csv.writerow([agenda['nome'][i],agenda['telefone'][i]])

      novo_c = input('Deseja adicionar outro contato (s/n):  ').lower()
      if novo_c == 'n':
        break
      elif novo_c == 's':
        continue
      else:
        print('erro')

def todos_os_contatos(user_login):
  base_dado_local = {
    "nome":[],
    "login":[],
    "senha":[]
  }

  with open('dado.csv', 'r', newline = '') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
      base_dado_local['nome'].append(linha['nome'])
      base_dado_local['login'].append(linha['login'])
      base_dado_local['senha'].append(linha['senha'])

  indice = base_dado_local['login'].index(user_login)
  nome_titular = base_dado_local['nome'][indice]

  agenda = {
    "nome":[],
    "telefone":[]
  }

  nome_arq = 'agenda_de_' + nome_titular + '.csv'
  with open(nome_arq, 'r', newline = '') as arquivo_csv:
          leitor_csv = csv.DictReader(arquivo_csv)
          for linha in leitor_csv:
            agenda['nome'].append(linha['nome'])
            agenda['telefone'].append(linha['telefone'])

  print('\nNumeros registrados\n')
  print('nome','    telefone')
  for i in agenda['nome']:
    for j in agenda['telefone']:
      print(f'{i}',f'   {j}')

def pesquisar_contato(user_login):
  base_dado_local = {
    "nome":[],
    "login":[],
    "senha":[]
  }

  with open('dado.csv', 'r', newline = '') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
      base_dado_local['nome'].append(linha['nome'])
      base_dado_local['login'].append(linha['login'])
      base_dado_local['senha'].append(linha['senha'])

  indice = base_dado_local['login'].index(user_login)
  nome_titular = base_dado_local['nome'][indice]

  agenda = {
    "nome":[],
    "telefone":[]
  }

  nome_arq = 'agenda_de_' + nome_titular + '.csv'
  with open(nome_arq, 'r', newline = '') as arquivo_csv:
          leitor_csv = csv.DictReader(arquivo_csv)
          for linha in leitor_csv:
            agenda['nome'].append(linha['nome'])
            agenda['telefone'].append(linha['telefone'])

  pesquisar_nome = input('Informar nome: ')
  if pesquisar_nome in agenda['nome']:
    indice = agenda['nome'].index(pesquisar_nome)
    telefone_pesquisado = agenda['telefone'][indice]
    print('Encontado')
    print(f'{pesquisar_nome} {telefone_pesquisado}')
  else:
    print('numero não contrado')

def excluir_contato(user_login):
  base_dado_local = {
    "nome":[],
    "login":[],
    "senha":[]
  }

  with open('dado.csv', 'r', newline = '') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
      base_dado_local['nome'].append(linha['nome'])
      base_dado_local['login'].append(linha['login'])
      base_dado_local['senha'].append(linha['senha'])

  indice = base_dado_local['login'].index(user_login)
  nome_titular = base_dado_local['nome'][indice]

  agenda = {
    "nome":[],
    "telefone":[]
  }

  nome_arq = 'agenda_de_' + nome_titular + '.csv'
  with open(nome_arq, 'r', newline = '') as arquivo_csv:
          leitor_csv = csv.DictReader(arquivo_csv)
          for linha in leitor_csv:
            agenda['nome'].append(linha['nome'])
            agenda['telefone'].append(linha['telefone'])

  pesquisar_nome = input('Informar nome do contato para exluir: ')
  if pesquisar_nome in agenda['nome']:
    indice = agenda['nome'].index(pesquisar_nome)
    agenda['nome'][indice] = None
    agenda['telefone'][indice] = None
    
    with open(nome_arq, 'w', newline = '') as arquivo_csv:
      escritor_csv = csv.writer(arquivo_csv)

      escritor_csv.writerow(agenda.keys())
      valores_transportados = zip(agenda)
      for linha in valores_transportados:
        escritor_csv.writerow(linha)

def excluir_conta(user_login):
  import os
  base_dado_local = {
    "nome":[],
    "login":[],
    "senha":[]
  }

  with open('dado.csv', 'r', newline = '') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
      base_dado_local['nome'].append(linha['nome'])
      base_dado_local['login'].append(linha['login'])
      base_dado_local['senha'].append(linha['senha'])

  indice = base_dado_local['login'].index(user_login)
  nome_titular = base_dado_local['nome'][indice]

  base_dado_local['nome'][indice] = None
  base_dado_local['login'][indice] = None
  base_dado_local['senha'][indice] = None

  with open('dado.csv', 'w', newline = '') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(base_dado_local.keys())
    valores_transportados = zip(base_dado_local)
    for linha in valores_transportados:
      escritor_csv.writerow(linha)

  nome_arq = 'agenda_de_' + nome_titular + '.csv'
  if os.path.exists(nome_arq):
    os.remove(nome_arq)
    print('conta cancelada')
    print('finalizando programa')
    exit()
  

  
  