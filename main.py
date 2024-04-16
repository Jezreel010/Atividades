class main():
    pass

from Cliente import Cliente
from Conta import Conta

c1=Cliente("João", "1234-4566")#instaciando objeto cliente
conta = Conta(c1.nome,6656,0)#instanciando objeto conta

print(conta.titular, "numero", conta.numero," seu saldo: ", conta.saldo,)