class Knight:

    def __init__(self, level) -> None:
        self.unit_type = "Knight"

        filename = f"{self.unit_type}_{level}.dat"

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"""
        Type: {self.unit_type}
        Life: {self.life}
        Speed: {self.speed}
        Attack Power: {self.attack_power}
        Attack Range: {self.attack_range}
        Weapon: {self.weapon}
        """


class Archer:

    def __init__(self, level) -> None:
        self.unit_type = "Archer"

        filename = f"{self.unit_type}_{level}.dat"

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"""
        Type: {self.unit_type}
        Life: {self.life}
        Speed: {self.speed}
        Attack Power: {self.attack_power}
        Attack Range: {self.attack_range}
        Weapon: {self.weapon}
        """


class Barracks:

    def build_unit(self, unit_type, level):
        if unit_type == "knight":
            return Knight(level)
        elif unit_type == "archer":
            return Archer(level)


if __name__ == "__main__":
    barracks = Barracks()
    knight_1 = barracks.build_unit("knight", 1)
    archer_1 = barracks.build_unit("archer", 2)

    print(f"[knight] {knight_1}")
    print(f"[archer] {archer_1}")
