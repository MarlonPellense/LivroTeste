class Livro:
    def __init__(self, titulo, autor, numPag, dispo):
        self.titulo = titulo
        self.autor = autor
        self.numPag = numPag
        self.dispo = dispo

    def verificaDispo(self):
        if self.dispo == True:
            print("Livro Disponível.")
        else:
            print("Livro Indisponível.")

    def emprestaLivro(self):
        if self.dispo == True:
            print("Você pegou o livro emprestado, devolva quando terminar de ler!")
            self.dispo = False
        else:
            print("O livro já foi pego por alguém, volte mais tarde!")

    def devolveLivro(self):
        if self.dispo == True:
            print("O livro ainda não foi emprestado, talvez você queira pegá-lo emprestado?")
        else:
            print("Obrigado, esperamos que tenha gostado do livro!")
            self.dispo = True
    
    def infoLivro(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.numPag}\n")

livro = Livro("O Homem de Giz", "C. J. Tudor", 272, True)

livro.infoLivro()
livro.verificaDispo()
livro.emprestaLivro()
livro.verificaDispo()
livro.devolveLivro()
livro.verificaDispo()