from contacts import Contact

class Supplier(Contact):
    def order(self, order : "Order") -> None:
        print(f"{order} order to {self.name}")

