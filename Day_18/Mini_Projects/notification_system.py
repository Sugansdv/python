import functools

# Custom notification decorator with header and footer
def notify(header, footer):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f" {header}")
            result = func(*args, **kwargs)
            print(f" {footer}")
            return result
        return wrapper
    return decorator

@notify(header=" New Notification Start ", footer="End of Notification ")
def process_order(order_id):
    print(f"Processing order #{order_id}")
    return f"Order {order_id} processed successfully"


if __name__ == "__main__":
    output = process_order(101)
    print("Returned Value:", output)
