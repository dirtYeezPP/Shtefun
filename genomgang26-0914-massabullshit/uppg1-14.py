class Book():
    books_amount = 0 
    _secret_code = 0 # purely a warning that this var is internal ("Protected")
                     # the interpreter does nothing to restrict or change the variable. 
    __very_secret_code = 0 # ("Private")
                     # is rewritten behind the scenes with the class name included 
                     # _className__attributeName 
                     # the variable doesnt live under "__very_secret_code" in memory. 
    def __init__(self, title, author, publication_year):
        self.title = title 
        self.author = author 
        self.publication_year = publication_year
        Book.books_amount += 1 
    def __str__(self):
        return f"Book: {self.title} \n written by {self.author} \n published year: {self.publication_year}"

    @classmethod 
    def show_books_amount(cls):
        return f"This many books have been created: {cls.books_amount}"
    @staticmethod
    def is_old(year):
        return year < 1990   # om det är äldre än 1990 = True 

bok1 = Book("We Were Liars", "E. Lockhart", 2014)
bok2 = Book("Alla Ljuder", "Camilla Grebe", 2021)
bok3 = Book("Alla Nattens Älskare", "Mieko Kawakami", 2024)

print(Book.books_amount)
print(Book.is_old(1882))
print(Book._secret_code) #ts works because its only private to the extent of us not being meant to change it 
#print(Book.__very_secret_code) 
# type object book has no such attribute, did u mean book blabla
print(Book._Book__very_secret_code) # the value of the private var is stored in memory with "_Book__attribute..." yes





