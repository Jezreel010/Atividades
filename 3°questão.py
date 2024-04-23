class Estudante:
    def __init__ (self, nome, idade, nota):
        self.nome = nome
        self.matricula = idade
        self.ano = nota 
    def média(self):
        return f"{self.nome} está na média"
    def aprovação(self):
        return f"{self.nome} está aprovadíssimo"
    
if __name__ == "__main__":
    estudante1 = Estudante("Ian", "16", "9.5")
print(estudante1.média())
print(estudante1.aprovação())