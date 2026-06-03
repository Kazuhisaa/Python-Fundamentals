class Product:
    def __init__(self,productID,price,name,stocks):
        self._productID = productID
        self._price = price
        self._name = name
        self._stock = stocks


    def get_details(self):
        return (f"Product_ID: {self._productID} | Name: {self._name} | Stocks: {self._stock} | Price: {self._price}")

    def deduct_Stock(self):
        pass
    
    @property 
    def stock(self):
        return self._stock

    @property
    def price(self):
        return self._price
    
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