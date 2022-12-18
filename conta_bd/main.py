
import pymysql.cursors

connection = pymysql.connect(host='localhost', # Nome do host (servidor) do SGBD
                                user='root', # Usuário que irá conectar ao banco
                                password='', # Senha da conexão
                                database='prova03', # Nome o banco que será utilizado
                                charset='utf8mb4', # Conjunto de caracteres a utilizar
                                cursorclass=pymysql.cursors.DictCursor) # Classe do cursor que será gerado

class Funcao:
   def __init__(self, cod, nome):
      self.cod = cod
      self.nome = nome
   
   def cadastrar_funcao(self):
      with connection.cursor() as c:
        # Create a new record
         sql = f"INSERT INTO funcao (cod, nome)" + f"VALUES ('{self.cod}', '{self.nome}')"
         c.execute(sql)
         connection.commit()
         print('Cadastrado com sucesso!')

        
   def pesquisar_funcao(cod_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcao "
         c.execute(sql)
         res_all = c.fetchall()
         #print(res_all)
         for index in res_all:
            if index['cod'] == cod_busca:
               print(f'Codico encontrado!')
               print( index['nome'])
               print(index['cod'])
               return index['nome']
         print('Funcao não cadastrada na base de dados!')
         novo_cod = input('Informe codigo novamente: ')
         Funcao.pesquisar_funcao(novo_cod)
         print( index['nome'])
         print(index['cod'])
         return index['nome']
   
   def buscar_funcao(nome_busca):
      with connection.cursor() as c:
         sql = f"SELECT * FROM funcao "
         c.execute(sql)
         res_all = c.fetchall()
         for index in res_all:
            if index['nome'] == nome_busca:
               print(f'nome encontrado!')
               return index['nome']
         print('Funcao não cadastrada na base de dados!')
         novo_nome = input('Informe nome novamente: ')
         Funcao.buscar_funcao(novo_nome)
         return index['nome']

   def editar_funcao(self):
      with connection.cursor() as c:
         nome = Funcao.buscar_funcao(self.nome)
         name = input('Informe novo nome:')
         sql = f"UPDATE funcao SET cod = '{self.cod}', nome = '{name}' WHERE nome = '{nome}'"
         c.execute(sql)
         connection.commit()
         print('Dados atualizados com sucesso!')
   
   def deletar_funcao(self):
      with connection.cursor() as c:
         name = input('Nome:')
         sql = f"DELETE FROM funcao WHERE nome = '{self.nome}'"
         c.execute(sql)
         connection.commit()

op2=1
while op2 !=0:
   print('\n********** MANTER FUNCAO **********')
   print('#  1. Cadastrar Funcao\n#  2. Pesquisar Funcao\n#  3. Editar Funcao\n#  4. Deletar Funcao \n#  0. Voltar ao Menu Principal')
   print('####################################')
   op2=int(input('\nInforme uma das opcoes acima: '))

   if op2 == 1:
      print('\n********** CADASTRAR FUNCAO *********')
      cod = input('Informe cod: ')
      nome = input('Informe nome: ')
      obj = Funcao(cod, nome )
      obj.cadastrar_funcao()
   
   elif op2 == 2:
      print('\n********* PESQUISAR FUNCAO *********')
      cod_funcao = input('Informe codigo da Funcao: ')
      Funcao.pesquisar_funcao(cod_funcao)

   elif op2 == 3:
      print('\n********** EDITAR FUNCAO **********')
      cod = input('Informe codigo da nova Funcao a ser cadastrada: ')
      nome = input('Informe o nome da Funcao que desejar editar: ')
      obj = Funcao(cod, nome )
      Funcao.editar_funcao(obj)
   
   elif op2 == 4:
      print('\n********* DELETAR FUNCAO *********')
      cod = input('Informe cod: ')
      nome = input('Informe nome: ')
      obj = Funcao(cod, nome )
      obj.excluir()

   


   
