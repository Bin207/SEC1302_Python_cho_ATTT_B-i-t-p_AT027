class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return f"Restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine."
    
    def open_restaurant(self):
        return f"Restaurant '{self.restaurant_name}' is now open for business!"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream", flavors=None):
        super().__init__(restaurant_name, cuisine_type)
        if flavors:
            self.flavors = flavors
        else:
            self.flavors = []
    
    def add_flavor(self, flavor):
        if not any(exist.lower() == flavor.lower() for exist in self.flavors):
            self.flavors.append(flavor)
    
    def remove_flavor(self, flavor):
        for exist in self.flavors:
            if exist.lower() == flavor.lower():
                self.flavors.remove(exist)
                return True
        return False
    
    def display_flavors(self):
        if not self.flavors:
            return "No flavors currently available."
        else:
            return "Available flavors: " + ', '.join(self.flavors)

def main():
    restaurant_name = input()
    flavors = input()
    if flavors:
        flavors = [x.strip() for x in flavors.split(',')]
    else:
        flavors = []
    res_ice = IceCreamStand(restaurant_name, flavors=flavors)
    
    q = int(input())
    for _ in range(q):
        tp = input()
        if tp == "SHOW":
            print(res_ice.display_flavors())
        elif tp == "DESCRIBE":
            print(res_ice.describe_restaurant())
        else:
            tp = tp.split()
            if tp[0] == "ADD":
                res_ice.add_flavor(tp[1])
            else:
                if res_ice.remove_flavor(tp[1]):
                    print("REMOVED", tp[1])
                else:
                    print("NOT FOUND", tp[1])
    
if __name__ == "__main__":
    main()
