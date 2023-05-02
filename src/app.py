from product import *

class App:
    def simulation(self):
        while True:
            command = input("Enter command: ")
            if command.startswith("save_product"):
                _, product_id, product_name, price = command.split()
                save_product(product_id, product_name, price)
            elif command.startswith("purchase_product"):
                _, product_id, quantity, price = command.split()
                purchase_product(product_id, quantity, price)
            elif command.startswith("order_product"):
                _, product_id, quantity = command.split()
                order_product(product_id, quantity)
            elif command.startswith("get_quantity_of_product"):
                _, product_id = command.split()
                print(get_quantity_of_product(product_id))
            elif command.startswith("get_average_price"):
                _, product_id = command.split()
                print(get_average_price(product_id))
            elif command.startswith("get_product_profit"):
                _, product_id = command.split()
                print(get_product_profit(product_id))
            elif command.startswith("get_fewest_product"):
                print(get_fewest_product())
            elif command.startswith("get_most_popular_product"):
                print(get_most_popular_product())
            elif command.startswith("get_orders_report"):
                print(get_orders_report())
            elif command.startswith("export_orders_report"):
                _, path = command.split()
                export_orders_report(path)
            elif command == "exit":
                break
            else:
                print("Invalid command")
