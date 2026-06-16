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
    
    @product_name.setter
    def product_name(self,new_name):
        self._name = new_name
    
    @price.setter
    def price(self,new_price):
        if new_price <= 0:
            print("Price must be greater than 0")
        else:
            self._price = new_price

    def replenish_stock(self,qty):
        if qty <= 0:
            print("Quantity must be a Postive Number")
        else:
            self._stock += qty
            print("Succesfully replenish Stocks")



    
class Clothing(Product):
    def __init__ (self,productID,price,name,stocks,size,material):
        super().__init__(productID,price,name,stocks)

        self._size = size
        self._material = material
    def get_details(self):
        return super().get_details() + f" | Size: {self._size} | Material: {self._material}"

class Electronics(Product):
    def __init__(self, productID,price,name,stocks,warranty):
        super().__init__(productID,price,name,stocks)

        self._warranty = warranty
    def get_details(self):
        return super().get_details() + f" | Warranty: {self._warranty}"

class Food(Product):
    def __init__(self,productID,price,name,stocks,expiration,is_vegan):
        super().__init__(productID,price,name,stocks)

        self._expiration = expiration
        self._is_vegan = is_vegan

    def get_details(self):
        vegan_status = "Yes" if self._is_vegan else "No"
        return super().get_details() + f" | Expiration:{self._expiration} | Vegan: {vegan_status}"

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
            if product.product_id.lower() == query.lower() or product.product_name.lower() == query.lower():
                return product
        return 

    def update_product_info(self,product_id, new_name,new_price):
        product = self.search_product(product_id)
        if product:
            product.product_name = new_name
            product.price = new_price
    
    def replenish_stock(self,product_id,qty):
        product = self.search_product(product_id)
        if product:
            product.replenish_stock(qty)

    def delete_product(self,product_id):
        product = self.search_product(product_id)
        if product:
            self._products.remove(product)
        
