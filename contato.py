from conexao import Conexao
class Contato:

    def __init__(self) -> None:
        self.conexao = Conexao().get_connection()
    
    def adicionar_contato(self, nome, email, telefone):
        with self.conexao.cursor() as cursor:
            cursor.execute(f"insert into contato(nome, email, telefone) values ('{nome}', '{email}', '{telefone}')")
            self.conexao.commit()

    def atualizar_nome(self, id_contato, nome):
        with self.conexao.cursor() as cursor:
            cursor.execute(f"UPDATE contato SET nome = '{nome}' WHERE id = {id_contato}")
            self.conexao.commit()

    def atualizar_email(self, id_contato, email):
        with self.conexao.cursor() as cursor:
            cursor.execute(f"UPDATE contato SET email = '{email}' WHERE id = {id_contato}")
            self.conexao.commit()

    def atualizar_telefone(self, id_contato, telefone):
        with self.conexao.cursor() as cursor:
            cursor.execute(f"UPDATE contato SET telefone = '{telefone}' WHERE id = {id_contato}")
            self.conexao.commit()

    def apagar_contato(self, id_contato):
        with self.conexao.cursor() as cursor:
            cursor.execute(f"DELETE FROM contato WHERE id = {id_contato}")
            self.conexao.commit()
