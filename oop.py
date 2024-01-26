# oop-is one of the popular paradigms that uses objects and classes in programming 
# a paradigm is an approach amethods used to solve aproblems
# programming paradigm therefore means approach used to solve some problems using aprogramming languages
# A class- is ablue print or templates of an objects
# An object-is an instance of a class
# Encappsulation-this putting restrictions on accessing variable and method directly
# inheritance-this refer to the capabilities of one class to inherit properties from another class
# Abstractions-it hides unaccessing code details from the User
# polymophisim-this means having many forms

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.discount = 0.10

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('River between', 12, 'Ngugi wa thiongo', 120)
book2 = Book('Utengano', 18, 'Bin Abdalla', 220)
book3 = Book('Mayai, waziri wa marathi', 28, 'Author 3', 320)


print(book1)
print(book1.author)
print(book1.discount) 
 
# class Book: 
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.__price = price
#         self.__discount = None

#     def set_discount(self, discount):
#       self.__discount = discount

#     def get_price(self):
#       if self.__discount:
#           return self.__price * (1-self.__discount)
#       return self.__price

#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"



# single_book = Book('Two States', 1, 'Chetan Bhagat', 200)
# print(single_book)

# bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
# bulk_books.set_discount(0.20)
# print(bulk_books)
        


