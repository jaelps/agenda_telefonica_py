import csv

import os

from modulo_menu import menu

with open('logoAgenda.txt', 'r') as arquivo:
  conteudo = arquivo.read()
  print(conteudo)

while True:
  iniciar = input('iniciar (s/n):  ')
  if iniciar == 's':
    os.system('clear')
    base_dado_local = {
    "nome":[],
    "login":[],
    "senha":[]
  }
    sistem = 'sistem'
    nome_arquivo = 'dado.csv'
    
    #verifica se arquivo existe
    if not os.path.exists(nome_arquivo):
      with open('dado.csv', mode = 'w', newline ='') as arquivo_csv:
             escrever_csv = csv.writer(arquivo_csv)
                  
             escrever_csv.writerow(['nome','login', 'senha'])
          
             for i in range(len(base_dado_local['nome'])):
                    escrever_csv.writerow([base_dado_local['nome'][i],base_dado_local['login'][i], base_dado_local['senha'][i]])
            
    #leitura de dados de base de dados antes, para armazenar na base local
    with open(nome_arquivo, mode = 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
    
        for linha in leitor_csv:
          for chave, valor in linha.items():
            if chave in base_dado_local:
              base_dado_local[chave].append(valor)
            else:
              base_dado_local[chave] = [valor]
    while True: #inicio do login
      print('-'*30)
      user_login = input('Login:  ')#solicita login do usuario
      contador_userLogin = len(user_login)
      if contador_userLogin != 11:
          print('login deve ter 11 digitos')
      else:  
        if user_login in base_dado_local['login']: #se user_login estiver em base_dado_local
            
            indice = base_dado_local['login'].index(user_login) #verificar indice de user_login no dicionario
            base_senha = base_dado_local['senha'][indice]  #de acordo com indice de log, solicita dado senha
        
            user_senha = input('Senha:  ')#solicita senha do usuario
            contador_user_senha = len(user_senha)
            if contador_user_senha != 5:
              print('senha deve ter 5 caracteris entre letras e numeros')
            else:
              if base_senha == user_senha: # se a senha estiver correta
                print('processo ok')#incluir
                menu(user_login)
              
        else: # se não for encontrado na base
          
            print(f'{sistem} Usuario não cadastrado')
            #novo cadastro
      
            #deseja efetuar cadastro
            escolha = input('Deseja efetuar novo cadastro (s/n):  ').lower() 
          
            if escolha == 's':
                cadastra_nome = input('Nome:  ')
                base_dado_local['nome'].append(cadastra_nome)
              
                cadastro_login = input('Login:  ')
                base_dado_local['login'].append(cadastro_login) #introduz no dicionario o login informado
          
                cadastro_senha = input('Senha:  ')
                c_cadastro_senha = len(cadastro_senha)
                if c_cadastro_senha != 5:
                    print('senha deve ter 5 caracteris entre letras e numeros')
                else:
                    base_dado_local['senha'].append(cadastro_senha)#introduz no dicionario a senha informada
          
                with open('dado.csv', mode = 'w', newline = '') as arquivo_csv: #abre arquivo
                  escrever_csv = csv.writer(arquivo_csv)
                  
                  escrever_csv.writerow(['nome','login', 'senha'])
          
                  for i in range(len(base_dado_local['nome'])):
                    escrever_csv.writerow([base_dado_local['nome'][i],base_dado_local['login'][i], base_dado_local['senha'][i]])
                    
                agenda_local = {
                "nome":[],
                "telefone":[]
                }

                
                nome_arq = 'agenda_de_' + cadastra_nome + '.csv'

                with open(nome_arq, mode = 'w', newline ='') as arquivo_csv:
                   escrever_csv = csv.DictWriter(arquivo_csv, fieldnames=agenda_local.keys())
                   escrever_csv.writeheader()
                  
                   for linha in zip(agenda_local.values()):
                     escrever_csv.writerow(dict(zip(agenda_local.keys(),linha)))
            elif escolha == 'n':
              print('Programa finalizado')
              exit()
            else:
              print('erro')
  elif iniciar == 'n':
      print('sistema sendo finalizado')
      print('Tenha um bom dia')
      exit()
  else:
      print('erro')