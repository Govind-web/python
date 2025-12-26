# Parent class
class Father:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    
    def show_details(self):
        print(f"Father's Name: {self.name}")
        print(f"Father's Occupation: {self.occupation}")

# Child class (inherits from Father)
class Banku(Father):
    def __init__(self, name, occupation, hobby):
        # Call parent constructor using super()
        super().__init__(name, occupation)
        self.hobby = hobby
    
    def show_details(self):
        # Extend parent method
        super().show_details()
        print(f"Banku's Hobby: {self.hobby}")

# Create objects
father_obj = Father("Ramesh", "Engineer")
banku_obj = Banku("Banku", "Student", "Football")

# Display details
print("Father Object:")
father_obj.show_details()

print("\nBanku Object:")
banku_obj.show_details()
