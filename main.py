import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ").strip().lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Invalid option. Please choose, small, medium, large, off, or report")

if __name__=="__main__":
    main()
