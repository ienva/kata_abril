

class Character:
    def __init__(self):
        self.max_health = 1000
        self.min_health = 0
        self.health = 1000
        self.level = 1
        self.alive = True

    def received_damage(self, amount_of_damage):
        self.health -= amount_of_damage
        if self.health < self.min_health:
            self.health = self.min_health

        self.alive = self.is_alive()

    def is_alive(self):
        return self.health > self.min_health

    def heal(self, amount_of_heal):
        if self.alive is False:
            raise ValueError("Character already dead")
        else:
            self.health += amount_of_heal
            if self.health > self.max_health:
                self.health = self.max_health
