

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

      return self.Author

   def getPublisher(self):

      return self.Publisher

   def getStock(self):

      return self.Stock

   def getPrice(self):

      return self.Price

   def getISBN(self):

      return self.ISBN

   def Connect_inventory():
      try:
         connection = mysql.connector.connect(host="localhost" ,user="root", password="", database="MethodsProject")
         print("Successful connection.")
         cursor = connection.cursor()
         return connection, cursor
      except:
         print("Failed connection.")
         sys.exit()   



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

   def Connect_cart():
      try:
         connection = mysql.connector.connect(host="localhost",user="root",password="",database="MethodsProject")
         print("Successful connection.")
         cursor = connection.cursor()
         return connection, cursor
      except:
         print("Failed connection.")
         sys.exit()
   def Checkout():
      connection, cursor = Cart.Connect_cart()
      #rows = cursor.execute("SELECT COUNT(ISBN) FROM cart")
      #for r in rows:
         #Inventory.lowerstock()
      cursor.execute("DELETE FROM cart")
      connection.commit()
      print(cursor.rowcount, "records deleted, cart cleared")
      cursor.close()
      connection.close()
      print("Connection closed")
