class Usuario:
    nome = ""
    senha = ""
    codigo = ""
    pag_visitadas = 0

    def setDados(self, nome):
        self.nome = nome
    def getDados(self):
        print(">Nome: "+self.nome)
    def setSenha(self, senha: str):
        if len(senha)>8:
            self._senha = senha
    def getSenha(self):
        return self._senha
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, cod):
        self.codigo = cod
    def getpag_visitadas(self):
        return self.pag_visitadas
    def setpag_visitadas(self):
        self.pag_visitadas +=1
