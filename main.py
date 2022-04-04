

class Character:
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True

    def received_damage(self, amount_of_damage):
        self.health -= amount_of_damage
        if self.health < 0:
            self.health = 0

        self.alive = self.is_alive()

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def heal(self, amount_of_heal):
        if self.alive is False:
            raise ValueError("Character already dead")
        else:
            self.health += amount_of_heal
            if self.health > 1000:
                self.health = 1000
