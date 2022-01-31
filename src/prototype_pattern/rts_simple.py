class Knight:

    def __init__(self, level):
        self.unit_type = "Knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "short sword"
        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 6
            self.attack_range = 2
            self.weapon = "long sword"

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
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "short bow"
        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 3
            self.attack_range = 10
            self.weapon = "long bow"

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
