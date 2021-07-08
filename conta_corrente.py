import minidb

class ContaCorrente(minidb.Model):
    saldo = float

    def __init__(self):
        self.saldo = 0
    
    def consultar_saldo(self):
        return self.saldo
    
    def sacar(self, quantidade):
        if self.saldo - quantidade >= 0:
            self.saldo -= quantidade
    
    def depositar(self, quantidade):
        self.saldo += quantidade
    
    def receber_transferencia(self, quantidade):
        self.saldo += quantidade
    
    def transferir(self, quantidade, outra_conta):
        if self.saldo - quantidade >= 0:
            self.saldo -= quantidade
            outra_conta.receber_transferencia(quantidade)
    
if __name__ == "__main__":
    db = minidb.Store('database.db', debug=True)
    db.register(ContaCorrente)
    conta1 = ContaCorrente()
    conta1.depositar(100)
    conta1.sacar(10)
    print(conta1.consultar_saldo())
    conta2 = ContaCorrente()
    conta1.transferir(10, conta2)
    print(conta1.consultar_saldo())
    print(conta2.consultar_saldo())