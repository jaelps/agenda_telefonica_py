def menu(user_login):
  from escolha_menu import adicionarContato, todos_os_contatos, pesquisar_contato, excluir_contato, excluir_conta

  while True:
    print("""
  -------------[ Menu - Agenda ]-------------
  ||                                       ||
  ||     1. Adicionar contatos             ||
  ||     2. Verificar todos os contatos    ||
  ||     3. Pesquisar contato              ||
  ||     4. Excluir contato                ||
  ||     5. Excluir conta                  ||
  ||     0. Sair                           ||
  ||                                       ||
  -------------------------------------------
  """)
    opcao = input('opção: ')
    if opcao == '1':
      adicionarContato(user_login)
    elif opcao == '2':
      todos_os_contatos(user_login)
    elif opcao == '3':
      pesquisar_contato(user_login)
    elif opcao == '4':
      excluir_contato(user_login)
    elif opcao == '5':
      excluir_conta(user_login)
    else:
      print('erro')
