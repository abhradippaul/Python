from enemy import Enemy, Zombie, MegaZombie

def main():
    print("--- General Enemy ---")
    generic_enemy = Enemy(type_of_enemy="Goblin", health_points=50, attack_damage=8)
    generic_enemy.__type_of_enemy = "test"
    generic_enemy.talk()
    generic_enemy.walk_forward()
    generic_enemy.attack()

    print("\n--- Regular Zombie ---")
    zombie = Zombie(health_points=100, attack_damage=15)
    zombie.talk()
    zombie.walk_forward()
    zombie.attack()

    print("\n--- Mega Zombie ---")
    mega_zombie = MegaZombie(health_points=250, attack_damage=45)
    mega_zombie.talk()
    mega_zombie.walk_forward()
    mega_zombie.attack()

if __name__ == "__main__":
    main()
