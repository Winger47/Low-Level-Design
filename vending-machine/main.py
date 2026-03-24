print("Hello Vending Machine")

from vending_machine import VendingMachine
from item import Item
from coin import Coin

# 1. Create the machine
machine = VendingMachine()

# 2. Load inventory
machine.inventory.add_item("A1", Item("Coke", "A1", 50), 5)
machine.inventory.add_item("A2", Item("Chips", "A2", 20), 10)

# 3. Simulate user actions
machine.select_item("A1")
machine.insert_coin(Coin.QUARTER)
machine.insert_coin(Coin.QUARTER)
machine.dispense()

machine.select_item("B1")  # Invalid item
machine.refund()



