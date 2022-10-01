from typing import List
import requests


class PowerstatsHeroes:
    URL = 'https://akabab.github.io/superhero-api/api'

    def __init__(self, *args):
        self.names_heroes = args

    def _get_all_heroes(self) -> List[dict]:
        """Возвращает список данных обо всех супергероях"""
        response = requests.get(f'{self.URL}/all.json')
        return response.json()

    def get_id_by_name(self) -> dict:
        """Осуществляет поиск id супергероя по имени"""
        heroes_id = {}
        all_heroes = self._get_all_heroes()

        for hero_name in self.names_heroes:
            for hero in all_heroes:
                if hero['name'] == hero_name:
                    heroes_id[hero_name] = hero['id']

        return heroes_id

    def get_powerstats_of_heroes(self) -> dict:
        """Осуществляет поиск данных о супергерое по id и возвращает их"""
        heroes_id = self.get_id_by_name()
        heroes_powerstats = {}

        for name, id in heroes_id.items():
            response = requests.get(f'{self.URL}/powerstats/{id}.json')
            heroes_powerstats[name] = response.json()

        return heroes_powerstats


def search_max_intelligence(heroes_names: list) -> str:
    """Поиск самого умного (intelligence) супергероя"""
    heroes_stats_array = PowerstatsHeroes(*heroes_names)
    heroes_stats = heroes_stats_array.get_powerstats_of_heroes()
    high_intelligence = 0
    name_best_hero = ''

    for name, power_stats in heroes_stats.items():
        if power_stats['intelligence'] > high_intelligence:
            name_best_hero = name
            high_intelligence = power_stats['intelligence']

    return name_best_hero


if __name__ == '__main__':
    heroes = ['Hulk', 'Captain America', 'Thanos']
    result = search_max_intelligence(heroes)
    print(result)
