

class Inventory:

   def __init__(self, title, author, publisher, stock, price, isbn):

      self.Title = title

      self.Author = author

      self.Publisher = publisher

      self.Stock = stock

      self.Price = price

      self.ISBN = isbn

   

   def getTitle(self):

      return self.Title

   def getAuthor(self):

      return self.Title

   def getPublisher(self):

      return self.Title

   def getStock(self):

      return self.Title

   def getPrice(self):

      return self.Title

   def getISBN(self):

      return self.ISBN

   



class Cart:

   def __init__(self, isbn, quantity, price):

      self.ISBN = isbn

      self.Quantity = quantity

      self.Total = price



   def getISBN(self):

      return self.ISBN

   def getQuantity(self):

      return self.Quantity

   def getTotal(self):

      return self.Total



