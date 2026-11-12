class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' is now open for business!")

def main():
    n = int(input())
    for _ in range(n):
        restaurant_name, cuisine_type = input().split(',')
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.describe_restaurant()
        restaurant.open_restaurant()

if __name__ == "__main__":
    main()
