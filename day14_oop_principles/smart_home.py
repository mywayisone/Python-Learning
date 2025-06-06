# 🧪 Mini Challenge (Optional)

# - If you want a bit more:
# - Create a SmartHome class that stores a list of appliances and can turn them all on/off.

from abc import ABC, abstractmethod

class Appliance(ABC):
    """Define the abstract class constructor without 
    the abstract method decorator - @abstractmethod.
    This enables the derived class to inherit it"""
    def __init__(self, brand):
        self.brand = brand
    
    # Define abstract method - turn_on()
    @abstractmethod
    def turn_on(self):
        pass

    # Define abstract method - turn_off()
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    # Define class constructor from abstract constructor
    def __init__(self, brand):
        super().__init__(brand)

    # Define the custom turn_on() method
    def turn_on(self):
        print(f"Washing machine({self.brand}) is turned on")
    
    # Define the custom turn_off() method
    def turn_off(self):
        print(f"Washing machine({self.brand}) is turned off")
    
class Microwave(Appliance):
    # Define class constructor from abstract constructor
    def __init__(self, brand):
        super().__init__(brand)
    
    # Define the custom turn_on() method
    def turn_on(self):
        print(f"Microwave({self.brand}) is turned on")

    # Define the custom turn_off() method
    def turn_off(self):
        print(f"Microwave({self.brand}) is turned off")

class SmartHome():
    # Define the class constructor
    def __init__(self):
        self.appliances = []

    # Define add_appliance() method
    def add_appliance(self, appliance):
        self.appliances.append(appliance)
    
    # Define turn_all_on() method
    def turn_all_on(self):
        for appliance in self.appliances:
            appliance.turn_on()
    # Define turn_all_off() method
    def turn_all_off(self):
        for appliance in self.appliances:
            appliance.turn_off()
    
    # Define show_all_appliances() method
    def show_all_appliances(self):
        for appliance in self.appliances:
            print(f"{appliance.__class__.__name__} - {appliance.brand}") # object.__class__.__name__ returns the object class name.

# Define the entry point
def main():
    appliances = [
        WashingMachine("Philip"),
        Microwave("Plastic"),
        WashingMachine("Thermacool"),
        Microwave("Binatone"),
        WashingMachine("Bezo"),
        Microwave("Skep"),
        WashingMachine("Dusk"),
        Microwave("Sebin")
    ]

    smart_home = SmartHome()
    for appliance in appliances:
        smart_home.add_appliance(appliance)
    
    smart_home.show_all_appliances()
    smart_home.turn_all_on()
    smart_home.turn_all_off()

if __name__ == "__main__":
    main()