import pytest
from main import Character, attack_between_two_characters,\
    heal_between_chars


class TestCharacter:
    def test_is_alive(self):
        character = Character()
        alive = character.is_alive()

        assert alive is True

        character.health = -10
        alive = character.is_alive()

        assert alive is False

    def test_received_damage(self):
        character = Character()
        character.received_damage(100)

        assert character.health == 900
        assert character.is_alive() is True

        character.received_damage(1000)

        assert character.health == 0
        assert character.is_alive() is False

    def test_heal(self):
        character = Character()

        character.received_damage(2000)
        with pytest.raises(ValueError):
            assert character.heal(100)

        assert character.health == 0

        character = Character()
        character.received_damage(500)
        character.heal(300)

        assert character.health == 800

        character.heal(300)

        assert character.health == 1000


class TestInteractions:
    def test_attack_between_two_characters(self):
        attacker_char = Character(id='attacker')
        attacked_char = Character(id='attacked')
        attacker_char, attacked_char = attack_between_two_characters(attacker_char, attacked_char, 100)

        assert attacked_char.health == 900
        assert attacker_char.health == 1000

        attacker_char = Character(id='attacker')
        attacked_char = Character(id='attacker')
        attacker_char, attacked_char = attack_between_two_characters(attacker_char, attacked_char, 100)

        assert attacked_char.health == 1000
        assert attacker_char.health == 1000

    def test_attack_between_two_characters_with_dif_level(self):
        attacker_char = Character(id='attacker')
        attacked_char = Character(id='attacked')

        attacker_char.level = 6
        attacker_char, attacked_char = attack_between_two_characters(attacker_char, attacked_char, 100)

        assert attacked_char.health == 800

        attacked_char.level = 11
        attacker_char, attacked_char = attack_between_two_characters(attacker_char, attacked_char, 100)
        assert attacked_char.health == 750

    def test_heal_between_two_characters(self):
        healer_char = Character(id='healer')
        healed_char = Character(id='healed')

        healed_char.received_damage(100)

        healer_char, healed_char = heal_between_chars(healer_char,
                                                      healed_char,
                                                      100)

        assert healed_char.health == 900

        healer_char, healed_char = heal_between_chars(healed_char,
                                                      healed_char,
                                                      100)

        assert healed_char.health == 1000




