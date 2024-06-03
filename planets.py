import csv


class Planets:
    def __init__(self) -> None:
        file = open("C:\\Users\\retr0\\Documents\\python3\\tools\\resources\\planets.csv", "r")
        reader = csv.DictReader(file)
        self.names = []
        self.planets_list = []
        for planet in reader:
            self.planets_list.append([planet[key] for key in planet.keys()])
            self.names.append(list(planet.keys()))
        print(self.names)
        self.planets_diameters = [float(planet[2]) for planet in self.planets_list]
        self.sun_diameter = 1.3927 * 1_000_000
        self.average_diameter = sum(self.planets_diameters) / len(self.planets_list)
        file.close()
