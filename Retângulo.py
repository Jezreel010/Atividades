
class Retângulo:
 def __init__(self, largura, altura):
  self.largura = largura
  self.altura = altura
if __name__ == "__main__":
 retangulo1 = Retângulo("10", "15 ")
 retangulo2 = Retângulo("20", "10")
 print(retangulo1.largura, retangulo1.altura)
 print(retangulo2.largura, retangulo2.altura)


l1 = int(input("Digite a largura: "))
l2 = int(input("Digite a altura: "))
perimetro = l1 + l2 + l1 + l2
print(perimetro)
area = l1 * l2
print(area)
