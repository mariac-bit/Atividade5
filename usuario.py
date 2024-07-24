class Usuario:
    def __init__(self):
        self.nome = ""
        self.__senha = ""
        self._codigo = ""
        self.pag_visitadas = 0

    def setDados(self, nome):
        self.nome = nome
    def getDados(self):
        print(">Nome: "+self.nome)
    def setSenha(self, senha):
        if len(senha)>8:
            self.__senha = senha
    def getSenha(self):
        return self.__senha
    def getCodigo(self):
        return self._codigo
    def setCodigo(self, cod):
        self._codigo = cod
