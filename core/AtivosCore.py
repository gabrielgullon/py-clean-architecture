class Ativos:
    # Getter method
    @property
    def id(self):
        return self._id

    # Setter method
    @id.setter
    def id(self, id):
        self._id = id

    # Getter method
    @property
    def cnpj(self):
        return self._cnpj

    # Setter method
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    # Getter method
    @property
    def nome(self):
        return self._nome

    # Setter method
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Getter method
    @property
    def cod_cvm(self):
        return self._cod_cvm

    # Setter method
    @cod_cvm.setter
    def cod_cvm(self, cod_cvm):
        self._cod_cvm = cod_cvm

    def __init__(
        self,
        cnpj,
        nome,
        cod_cvm,
        id=None,
    ) -> None:
        self._id = id
        self._cnpj = cnpj
        self._nome = nome
        self._cod_cvm = cod_cvm

    @staticmethod
    def vazio():
        return Ativos("", "", "")

    @staticmethod
    def from_dict(source):
        return Ativos(source["cnpj"], source["nome"], source["cod_cvm"], source["id"])

    def to_dict(self):
        return {
            "cnpj": self.cnpj,
            "nome": self.nome,
            "cod_cvm": self.cod_cvm,
        }
