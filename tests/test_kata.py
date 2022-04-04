import pytest
from main import Character


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

