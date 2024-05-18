class Book:
    def name(self,name):
        print(name)
    def author(self,author):
        print(author)
        
tom = Book()
tom.name(input('Введите название книги '))
tom.author(input('Введите автора '))
