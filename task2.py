class Customer:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculateBill(self):
        self.amount=0.1 * self.units
        
    def displayBill(self):
        print(f"Name: {self.name}\nUnits: {self.units}")
        print(f"The amount = {self.amount}")


class ResidentialCustomer(Customer):
    def __init__(self, name, units, family_number):
        super().__init__(name, units)
        self.family_number = family_number

    def calculateBill(self):
        base_amount = 0.1 * self.units
        discount = 0.2 * self.family_number
        self.amount = base_amount - discount

    def displayBill(self):
        super().displayBill()
        print(f"Family members: {self.family_number}")


class CommercialCustomer(Customer):
    def __init__(self, name, units, business_type):
        super().__init__(name, units)
        self.business_type = business_type

    def calculateBill(self):
        if self.business_type.lower() == "small":
            base_amount = 0.12 * self.units
            discount = (base_amount / 10) * 100
            self.amount = base_amount - discount
        elif self.business_type.lower() == "large":
            base_amount = 0.12 * self.units
            discount = (base_amount / 10) * 100
            self.amount = base_amount + discount

    def displayBill(self):
        super().displayBill()
        print(f"Business Type: {self.business_type}")


# Example Usage
residential_customer = ResidentialCustomer("John Doe", 200, 3)
residential_customer.calculateBill()
residential_customer.displayBill()

commercial_customer = CommercialCustomer("ABC Group", 500, "large")
commercial_customer.calculateBill()
commercial_customer.displayBill()
