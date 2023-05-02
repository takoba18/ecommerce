import csv

products = {}


def save_product(product_id, product_name, price):
    if product_id in products:
        products[product_id]['name'] = product_name
        products[product_id]['price'] = float(price)
    else:
        products[product_id] = {'name': product_name, 'price': float(price), 'balance': 0, 'purchases': [],
                                'orders': []}


def purchase_product(product_id, quantity, price):
    if product_id in products:
        products[product_id]['balance'] += int(quantity)
        products[product_id]['purchases'].append({'quantity': int(quantity), 'price': float(price)})
    else:
        print("Product not found")


def order_product(product_id, quantity):
    if product_id in products:
        if products[product_id]['balance'] < int(quantity):
            print("Not enough stock")
        else:
            products[product_id]['balance'] -= int(quantity)
            products[product_id]['orders'].append({'quantity': int(quantity), 'price': products[product_id]['price']})
    else:
        print("Product not found")


def get_quantity_of_product(product_id):
    if product_id in products:
        return products[product_id]['balance']
    else:
        print("Product not found")


def get_average_price(product_id):
    if product_id in products:
        purchases = products[product_id]['purchases']
        if len(purchases) == 0:
            print("No purchase history")
        else:
            total_price = sum(p['price']*p['quantity'] for p in purchases)
            total_purchases = sum(p['quantity'] for p in purchases)
            average_price = total_price / total_purchases
            return average_price
    else:
        print("Product not found")


def get_product_profit(product_id):
    if product_id in products:
        purchases = products[product_id]['purchases']
        orders = products[product_id]['orders']
        if len(purchases) == 0:
            print("No purchase history")
            return
        total_purchase_price = sum(p['quantity'] * p['price'] for p in purchases)
        if len(orders) == 0:
            print("No orders for this product")
            return
        total_orders = sum(o['quantity'] for o in orders)
        total_purchases = sum(p['quantity'] for p in purchases)
        total_order_price = sum(o['quantity'] * o['price'] for o in orders)
        profit_per_unit = total_order_price / total_orders - total_purchase_price / total_purchases
        total_profit = profit_per_unit * total_orders
        return total_profit
    else:
        print("Product not found")


def get_fewest_product():
    if len(products) == 0:
        print("No products found")
        return
    min_name = min(products.values(), key=lambda p: p['balance'])['name']
    return min_name


def get_most_popular_product():
    if len(products) == 0:
        print("No products or orders found")
        return
    max_orders = 0
    for product_id in products:
        orders = products[product_id]['orders']
        temp = sum(o['quantity'] for o in orders)
        if temp>max_orders:
            popular = products[product_id]['name']
    return popular


def get_orders_report():
    report = []
    for product_id in products:
        product = products[product_id]
        for order in product['orders']:
            cogs = order['quantity'] * get_average_price(product_id)
            selling_price = order['price']
            report.append({'product_id': product_id, 'product_name': product['name'], 'quantity': order['quantity'],
                           'price': product['price'], 'cogs': cogs, 'selling_price': selling_price})
    return report


def export_orders_report(path):
    report = get_orders_report()
    with open(path, mode='w', newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=['product_id', 'product_name', 'quantity', 'price', 'cogs', 'selling_price'])
        writer.writeheader()
        for row in report:
            writer.writerow(row)
        print(f"Report exported to {path}")

