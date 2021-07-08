import uuid

class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.endereco = uuid.uuid4().hex

    
    def consultar_saldo(self):
        return self.saldo
    
    def sacar(self, quantidade):
        if self.saldo - quantidade >= 0:
            self.saldo -= quantidade
    
    def depositar(self, quantidade):
        self.saldo += quantidade
    
    def receber_transferencia(self, quantidade):
        self.saldo += quantidade
    
    def transferencias(self, quantidade, outra_conta):
        if self.saldo - quantidade >= 0:
            self.saldo -= quantidade
            outra_conta.receber_transferencia(quantidade)
    

        