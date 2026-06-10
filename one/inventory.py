class Product:
    def __init__(self,productID,price,name,stocks):
        self._productID = productID
        self._price = price
        self._name = name
        self._stock = stocks


    def get_details(self):
        return (f"Product_ID: {self._productID} | Name: {self._name} | Stocks: {self._stock} | Price: {self._price}")

    def deduct_stock(self,quantity):
        if quantity <=0:
            print("Quantity must be a Positive Number")
            return 
        
        if self._stock >= quantity:
            self._stock -= quantity
            print("Succesfully Deducted on the Stocks")
        else :
            print("Not Enough Stocks")   
        
    @property
    def stock(self):
        return self._stock

    @property
    def price(self):
        return self._price
    
    @property
    def product_id(self):
        return self._productID
    
    @property
    def product_name(self):
        return self._name
    
class Clothing(Product):
    def __init__ (self,productID,price,name,stocks,size,material):
        super().__init__(productID,price,name,stocks)

        self._size = size
        self._material = material

class Electronics(Product):
    def __init__(self, productID,price,name,stocks,warranty):
        super().__init__(productID,price,name,stocks)

        self._warranty = warranty

class Food(Product):
    def __init__(self,productID,price,name,stocks,expiration,is_vegan):
        super().__init__(productID,price,name,stocks)

        self._expiration = expiration
        self._is_vegan = is_vegan

class Inventory:

    def __init__(self):
        self._products = []

    def add_stock(self,product):
        self._products.append(product)

    def view_stock(self):
        if len(self._products) == 0: 
            print("Inventory is Empty")
        
        for product in self._products:
            print(product.get_details())

    def search_product(self,query):

        for product in self._products:
            print(product.get_details()) 
            if product.product_id.lower() == query.lower() or product.name.lower() == query.lower():
                return product
        return 
