class DemoShop:
    def __init__(self, session):
        self.demoqa = session
        self.cart = None

    def login(self):
        pass

    def add_to_cart(self):
        return self.post(url="/addproducttocart/catalog/31/1/1")

    def addition_succes_status(self):
        return self.cart.json()["success"]

    def cart_products_count(self):
        return self.cart.json()["updatetopcartsectionhtml"]

