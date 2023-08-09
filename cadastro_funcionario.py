#Este programa fara a conexão com o MySql e fara o cadastro de funcionarios
#A biblioteca mysql.connector permite que o python se comunique com o Mysql

import mysql.connector

#Fazendo a conexão com o banco
conexao = mysql.connector.connect(host="localhost",password="A1un0proz@ds",user="root",database="aula_sql")

resp = "s"

while resp =="s":

    while True:
        
        try:

            print("Cadastro de funcionarios")

            nome = input ("Digite o nome:")
            cpf = input ("Digite o cpf:")
            endereco = input ("Digite o endereço:")

            #Obtendo o cursor,o cursor permite que façamos inserções, consultas, atualizações e deleções no banco.
            cursor =  conexao.cursor()

            #executando a inserção de dados na tabela funcionarios
            cursor.execute("insert into funcionarios(nome,cpf,endereco) values(%s,%s,%s);",(nome,cpf,endereco))

            #Confirmando a transação
            conexao.commit()
            break;
        except:
            print("Voce digitou alguma informaçao invalida! revise os dados.")
            
    resp = input("Deseja cadastrar um novo funcionario? 'S' para sim e 'N' para não.").lower()

#Fechando o cursor e a conexão
cursor.close()
conexao.close()
    
