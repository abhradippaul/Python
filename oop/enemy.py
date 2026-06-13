class Enemy:

    __type_of_enemy: str
    __health_points: int
    __attack_damage: int

    def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int):
        self.__type_of_enemy = type_of_enemy
        self.__health_points = health_points
        self.__attack_damage = attack_damage

    def get_type_of_enemy(self) -> str:
        return self.__type_of_enemy

    def get_health_points(self) -> int:
        return self.__health_points

    def get_attack_damage(self) -> int:
        return self.__attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walks forward")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.__attack_damage} damage")


class Zombie(Enemy):
    def __init__(self, health_points: int, attack_damage: int, type_of_enemy: str = "Zombie"):
        super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print(f"{self.get_type_of_enemy()} says: *Grumble* *Mumble*")


class MegaZombie(Zombie):
    def __init__(self, health_points: int, attack_damage: int):
        super().__init__(health_points=health_points, attack_damage=attack_damage, type_of_enemy="Mega Zombie")

    def attack(self):
        print(f"{self.get_type_of_enemy()} performs a mega-slam attack dealing {self.get_attack_damage()} damage!")