import webbrowser

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount, color):
        self.name = name
        self.amount = amount
        self.color = color

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def use(self, use_amount):
        self.amount -= use_amount
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + ' and ' + other.name
        new_amount = self.amount + other.amount
        return Ingredient(name=new_name, amount=new_amount, color = "")
    def get_info(self):
        """Makes a new wiki url for each ingredient"""
        url = f'https://en.wikipedia.org/wiki/{self.name}'
        return(url)
    


i = Ingredient("Peas",23,"green")
c = Ingredient("Cauliflower",2,"white")
b = Ingredient("Broccoli",2,"green")
d = Ingredient("Dandelion",0.5,"yellow")


webbrowser.open_new_tab(i.get_info())