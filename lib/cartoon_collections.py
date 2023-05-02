def roll_call_dwarves(names):
    for index, name in enumerate(names, 1):
        print(f'{index}. {name}')

def summon_captain_planet(planets):
    return [f'{planet.capitalize()}!' for planet in planets]


def long_planeteer_calls(planets):
    for planet in planets:
        if len(planet) > 4:
            return True
    return False

def find_the_cheese(list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    # for cheese in cheese_list:
    #     if cheese in list:
    #         return cheese

    for food in list:
        if food in cheese_list:
            return food
    return None
