from usuario import Usuario
class Pessoa(Usuario):
    def cadastro(self):
        nome = input("Digite o nome do moderador: ")
        senha = input("Digite a senha do moderador: ")
        cod = input("Cadastre um código: ")
        self.setCodigo(cod)
    def getDados(self):
        print("> Nome: "+self.nome)
        print("> Código: "+self.codigo)
