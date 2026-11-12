class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, max_capacity=500):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.max_capacity = max_capacity
        self.number_served = 0
    
    def set_number_served(self, number):
        if 0 <= number <= self.max_capacity:
            self.number_served = number 
            return True
        return False
    
    def increment_number_served(self, additional_served):
        if additional_served >= 0 and (self.number_served + additional_served) <= self.max_capacity:
            self.number_served += additional_served
            return True
        return False
    
    def get_status(self):
        return f"Served: {self.number_served}/{self.max_capacity}"

def main():
    restaurant_name, cuisine_type, max_capacity = [x.strip() for x in input().split(',')]
    restaurant = Restaurant(restaurant_name, cuisine_type, int(max_capacity))
    q = int(input())
    for _ in range(q):
        tp, va = input().split()
        if tp == "SET":
            if restaurant.set_number_served(int(va)):
                print("SET OK -> " + restaurant.get_status())
            else:
                print("SET REJECTED")
        else:
            if restaurant.increment_number_served(int(va)):
                print("INC OK -> " + restaurant.get_status())
            else:
                print("INC REJECTED") 

if __name__ == "__main__":
    main()
