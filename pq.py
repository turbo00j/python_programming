class library:
    def __init__(self,books):
        self.books_list=books
    def __add__(self,others):
        return self.books_list+others.books_list
booksrack1=int(input("Enter the books in rack 1:"))
rack1=library(booksrack1)
booksrack2=int(input("Enter the books in rack 1:"))
rack2=library(booksrack2)
print("the total no of books are :",rack1+rack2)
