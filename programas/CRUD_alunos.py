import oracledb as orcl

import pandas as pd

def main():
    conexao, str_connect, inst_SQL = conectar_DB()
    opc = 1
    while (opc != 5 and conexao == True):
        print("1 - Inserçaõ do aluno")
        print("2 - Alteração do aluno")
        print("3 - Exclusão do aluno")
        print("4 - Exibiçaõ dos alunos")
        print("5 - Sair")
        opc = int(input("Digite a opção desejada: "))
        match opc:
            case 1:
                try:
                    rm = int(input("Digite o RM do aluno: "))
                    nome = (input("Digite o nome do aluno: "))
                    curso = (input("Digite o curso do aluno: "))
                    idade = int(input("Digite a idade do aluno: "))
                except ValueError:
                    print("Digite dados númericos")
                else:
                    str_insert = f"""INSERT INTO alunos(ALUNO_RM, ALUNO_NOME, ALUNO_CURSO, ALUNO_IDADE) VALUES ({rm}, '{nome}','{curso}', {idade}) """
                    executar_SQL(str_connect, inst_SQL, str_insert)
            case 2:
                lista_dados = []
                id = int(input("Digite o id do aluno a ser alterarado: "))
                str_consulta = f"""SELECT * FROM alunos WHERE ALUNO_ID = {id}"""
                inst_SQL.execute(str_consulta)

                dados = inst_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id do aluno não existe na tabela")
                else:
                    try:
                        rm = int(input("Digite o novo RM do aluno: "))
                        nome = (input("Digite o novo nome do aluno: "))
                        curso = (input("Digite o novo curso do aluno: "))
                        idade = int(input("Digite a nova idade do aluno: "))
                    except ValueError:
                        print("Digite dados númericos")
                    else:
                        str_update = f"""UPDATE alunos SET ALUNO_RM = {rm}, ALUNO_NOME = '{nome}', ALUNO_CURSO = '{curso}', ALUNO_IDADE = {idade} WHERE ALUNO_ID = {id}"""
                        executar_SQL(str_connect, inst_SQL, str_update)
            case 3:
                lista_dados = []
                id = int(input("Digite o id do aluno a ser alterarado: "))
                str_consulta = f"""SELECT * FROM alunos WHERE ALUNO_ID = {id}"""
                inst_SQL.execute(str_consulta)

                dados = inst_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                if (len(lista_dados) == 0):
                    print("O id do aluno não existe na tabela")
                else:
                    try:
                        str_delete = f"""DELETE FROM ALUNOS WHERE ALUNO_ID = {id}"""
                        executar_SQL(str_connect, inst_SQL, str_delete)
                    except:
                        print("Digite valores numericos")
                    else:
                        executar_SQL(str_connect, inst_SQL, str_delete)

            case 4:
                lista_dados = []

                inst_SQL.execute("SELECT * FROM alunos")
                dados = inst_SQL.fetchall()

                for dado in dados:
                    lista_dados.append(dado)

                df_alunos =pd.DataFrame.from_records(lista_dados, columns=['ID', 'RM', 'NOME', 'CURSO', 'IDADE'], index=['ID'])

                if (df_alunos.empty):
                    print("Não existe dados na tabela")
                else:
                    print(df_alunos)

            case _:
                print("Opção invalida")






def conectar_DB():
    try:
        dados_serv = orcl.makedsn("oracle.fiap.com.br", 1521, "ORCL")
        str_connect = orcl.connect(user="XXXXXXX", password="XXXXX",  dsn= dados_serv)

        inst_SQL = str_connect.cursor()
    except ValueError as e:
        print(f"Erro: {e}")
        conexao = False
        str_connect = ""
        inst_SQL = ""

    else:
        conexao = True

    return (conexao, str_connect, inst_SQL)


def executar_SQL(str_connect, inst_SQL, str_SQL):
    try:
        inst_SQL.execute(str_SQL)
        str_connect.commit()
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"Transação executada com sucesso")

if __name__ == "__main__":
    main()