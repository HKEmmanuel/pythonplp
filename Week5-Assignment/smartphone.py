

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # GB
        self.battery = battery  # %

    def make_call(self, number):
        print(f"{self.brand} {self.model} calling {number} 📞")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")

    def info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")


class SmartphoneGaming(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} 🎮")

    def info(self):
        super().info()
        print(f"GPU: {self.gpu}")


# --- Test ---
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15", 256, 80)
    phone1.info()
    phone1.make_call("123-456-7890")
    phone1.charge(15)

    gaming_phone = SmartphoneGaming("Samsung", "Galaxy S24 Ultra", 512, 50, "Adreno 740")
    gaming_phone.info()
    gaming_phone.play_game("Genshin Impact")
    gaming_phone.charge(30)
