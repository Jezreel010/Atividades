class livro:
    def __init__(self, titulo, autor, paginas, palavras):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.palavras = palavras
    def informações(self):
        return f"O livro {self.titulo} foi escrito pelo autor {self.autor}, tem {self.paginas} paginas e {self.palavras} palavras"
    def total(self):
        return f"Tem {self.paginas} paginas e {self.palavras} palavras"

if __name__=="__main__":
    l1 = livro("O diario de um banana", "Jeff Kinney", "224", "1069")

print(l1.informações())
print(l1.total())
     
