
class Swag_Page:

    def __init__(self,page):
        self.page=page

        self.all_products = page.locator(".inventory_list .inventory_item")

    def get_number_of_products(self):
        #return self.page.locator(self.all_products).count()
        return self.all_products.count()













#.inventory_list div.inventory_item