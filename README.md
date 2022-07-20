# MethodsProject

Inventory:

Display stock: gets queries from the sql inventory table to display the items in the terminal
Add Item: creates an sql insert command to add inventory items to the inventory table
Lower stock: creates an sql update command to lower the stock number of an inventory item depending on the number of that item being bought through the shopping cart

Shopping cart:
Display shopping cart: gets queries from sql shopping cart table to display the items in the terminal
Add to cart: creates an sql insert command to add an item to the shopping cart table
Remove from cart: creates an sql delete command to remove an item from shopping cart
Checkout: should use the "Lower stock" function from Inventory to lower stock numbers, then uses an sql command to delete all items in the shopping cart
