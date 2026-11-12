class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        return f"Battery: {self.battery_size}-kWh"
    
    def get_range(self):
        if self.battery_size <= 75:
            range_miles = 260
        elif self.battery_size <= 100:
            range_miles = 315
        else:
            range_miles = 375
        return f"Estimated range: {range_miles} miles on full charge."
    
    def upgrade_battery(self, target_capacity=100):
        if self.battery_size < target_capacity:
            self.battery_size = target_capacity
            return f"Battery upgraded to {self.battery_size}-kWh."
        else:
            return f"Battery already at or above {target_capacity}-kWh."

class ElectricCar:
    def __init__(self, make, model, year, battery_size=75):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery(battery_size)
    
    def get_descriptive_name(self):
        return f"{self.year} {self.make.title()} {self.model.title()}"

def main():
    make, model, year, initial_battery_size = [x.strip() for x in input().split(',')]
    elcar = ElectricCar(make, model, int(year), int(initial_battery_size))
    
    q = int(input())
    for _ in range(q):
        tp = input()
        if tp == "INFO":
            print(f"{elcar.get_descriptive_name()} | {elcar.battery.describe_battery()}")
        elif tp == "RANGE":
            print(elcar.battery.get_range())
        else:
            tp = tp.split()
            print(elcar.battery.upgrade_battery(int(tp[1])))
    
if __name__ == "__main__":
    main()
