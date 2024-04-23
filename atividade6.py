class Pessoa:
 def __init__(self, nome, idade, altura):
  self.nome = nome
  self.idade = idade
  self.altura = altura
if __name__ == "__main__":
 pessoa1 = Pessoa("João", "15 anos", "1.80")
 pessoa2 = Pessoa("Maria", "15 anos","1.60")
 print(pessoa1.nome, pessoa1.idade, pessoa1.altura)
 print(pessoa2.nome, pessoa2.idade, pessoa2.altura)