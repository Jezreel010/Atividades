class Conta_bancária:
 def __init__(self, numero_da_conta, saldo, titular):
  self.numero_da_conta = numero_da_conta
  self.saldo = saldo
  self.titular = titular
if __name__ == "__main__":
 conta1 = Conta_bancária("123456", "R$100", "João")
 conta2 = Conta_bancária("345678", "R$1000","Ana")
 print(conta1.numero_da_conta, conta1.saldo, conta1.titular)
 print(conta2.numero_da_conta, conta2.saldo, conta2.titular)