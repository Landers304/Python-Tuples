#Task 1:


def print_order_details(orders):
    for i, order in enumerate(orders, start=1):
        customer_name, product, quantity = order
        print(f"Order {i}: Customer Name: {customer_name}, Product: {product}, Quantity: {quantity}")

# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Print order detail
print_order_details(orders)
