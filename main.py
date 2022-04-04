
def attack_between_two_characters(character_attacker,
                                  character_attacked,
                                  amount_of_damage):
    is_same_faction = character_attacker.check_if_other_character_has_common_faction(character_attacked)

    if not is_same_character(character_attacker, character_attacked)\
            and not is_same_faction:
        modified_damage = get_modify_amount_of_damage(character_attacker,
                                                      character_attacked,
                                                      amount_of_damage)

        character_attacked.received_damage(modified_damage)

    return character_attacker, character_attacked


def get_modify_amount_of_damage(character_attacker, character_attacked, amount_of_damage):
    dif_level_to_modify_damage = 5
    level_dif = level_comparison(character_attacker, character_attacked)
    if level_dif >= dif_level_to_modify_damage:
        amount_of_damage = amount_of_damage * 1.5
    elif level_dif <= - dif_level_to_modify_damage:
        amount_of_damage = amount_of_damage / 2

    return amount_of_damage


def is_same_character(character_1, character_2):
    return character_1.id == character_2.id


def level_comparison(character_1, character_2):
    level_dif = character_1.level - character_2.level
    return level_dif


def heal_between_chars(character_healer, character_healed, amount_of_heal):
    is_same_faction = character_healer.check_if_other_character_has_common_faction(character_healed)
    if is_same_character(character_healer, character_healed) or is_same_faction:
        character_healed.heal(amount_of_heal)

    return character_healer, character_healed


class Character:
    def __init__(self, id=None):
        self.max_health = 1000
        self.min_health = 0
        self.health = 1000
        self.level = 1
        self.alive = True
        self.id = id
        self.factions = set()

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

    def join_factions(self, faction_name=None):
        if faction_name not in self.factions:
            self.factions.update([faction_name])

    def leave_faction(self, faction_name=None):
        if faction_name in self.factions:
            self.factions.remove(faction_name)

    def check_if_other_character_has_common_faction(self, character):
        intersected_set = self.factions.intersection(character.factions)
        return len(intersected_set) > 0

