from autor import Autor
from livro import Livro

def main():
    autor1 = Autor("J.K. Rowling", "1965-07-31")
    livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, 1997)

    print(autor1)
    print(livro1)

if __name__ == "__main__":
    main()