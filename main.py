
def attack_between_two_characters(character_attacker,
                                  character_attacked,
                                  amount_of_damage):
    dif_level_to_modify_damage = 5
    damage_factor = 2
    if not is_same_character(character_attacker, character_attacked):
        level_dif = level_comparison(character_attacker, character_attacked)
        if level_dif >= dif_level_to_modify_damage:
            amount_of_damage = amount_of_damage * damage_factor
        elif level_dif <= - dif_level_to_modify_damage:
            amount_of_damage = amount_of_damage / damage_factor

        character_attacked.received_damage(amount_of_damage)

    return character_attacker, character_attacked


def is_same_character(character_1, character_2):
    return character_1.id == character_2.id


def level_comparison(character_1, character_2):
    level_dif = character_1.level - character_2.level
    return level_dif


def heal_between_chars(character_1, character_2, amount_of_heal):
    if is_same_character(character_1, character_2):
        character_1.heal(amount_of_heal)

    return character_1, character_2


class Character:
    def __init__(self, id=None):
        self.max_health = 1000
        self.min_health = 0
        self.health = 1000
        self.level = 1
        self.alive = True
        self.id = id

    def received_damage(self, amount_of_damage):
        self.health = max(self.min_health,
                          self.health - amount_of_damage)

        self.alive = self.is_alive()

    def is_alive(self):
        return self.health > self.min_health

    def heal(self, amount_of_heal):
        if self.alive is False:
            raise ValueError("Character already dead")
        else:
            self.health = min(self.max_health,
                              self.health + amount_of_heal)
