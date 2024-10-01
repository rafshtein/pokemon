from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(30, 60)
        self.hp = randint(200, 400)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://upload.wikimedia.org/wikipedia/ru/7/77/Pikachu.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "Враг применил защиту в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
                Здоровье твоего покемона: {self.hp}
                Сила твоего покемона: {self.power}"""
        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def trainer_info(self):
        return self.pokemons.keys()
    
    def rare_info(self):
        if self.pokemon_number >= 700:
            return "Поздровлем вы нашли редкого покемона!"
        else:
            return "Вы нашли обычного покемона"


class Wizard(Pokemon):
    pass


class Fighter(Pokemon):
    
    def attack(self, enemy):
        
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result +f"\nбоец применил супер атаку: {super_power}"
    
    
