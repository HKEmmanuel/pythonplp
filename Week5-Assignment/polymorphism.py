
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛴️")


# --- Test ---
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()
