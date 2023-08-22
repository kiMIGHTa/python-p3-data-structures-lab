spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names=[spicy_food["name"] for spicy_food in spicy_foods]
    return food_names
    pass
#🌶 

def get_spiciest_foods(spicy_foods):
    spiciest_foods=[spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"]>5]
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: ' + "🌶"*food["heat_level"])
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    fetched_food=[food for food in spicy_foods if cuisine==food["cuisine"]]
    print(fetched_food)
    return fetched_food[0]
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"]>5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: ' + "🌶"*food["heat_level"])    
    
    pass

def get_average_heat_level(spicy_foods):
    heat_list=[food["heat_level"] for food in spicy_foods]
    average_heat_level=sum(heat_list)/len(heat_list)
    print(average_heat_level)
    return average_heat_level
    pass
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    if spicy_food:
        spicy_foods.append(spicy_food)
    return spicy_foods    
     
    
