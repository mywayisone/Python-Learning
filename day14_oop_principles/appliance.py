# 📝 Practice Task

# Create an abstract class Appliance:
# __init__(self, brand)
# Abstract method: turn_on()
# Abstract method: turn_off()

# Then create two classes:
# WashingMachine(Appliance) – custom turn_on/turn_off
# Microwave(Appliance) – custom turn_on/turn_off
# Create objects and test their behavior.

from abc import ABC, abstractmethod

class Appliance(ABC):
    # Define abstract class constructor
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    # Define derived class constructor
    def __init__(self, brand):
        super().__init__(brand)

    # Define custom turn_on() method
    def turn_on(self):
        print("Washing machine is turned on.")
    
    # Define custom turn_off() method
    def turn_off(self):
        print("Washing machine is turned off.")

class Microwave(Appliance):
    # Define the derived class constructor
    def __init__(self, brand):
        super().__init__(brand)
    
    # Define custom turn_on() method
    def turn_on(self):
        print("Microwave is turned on")

    # Define custom turn_off() method
    def turn_off(self):
        print("Microwave is turned off")


def main():
    washingmachine = WashingMachine("Binatone")
    microwave = Microwave("Philip")

    washingmachine.turn_on()
    washingmachine.turn_off()
    microwave.turn_on()
    microwave.turn_off()

# Define entry point
if __name__ == "__main__":
    main()