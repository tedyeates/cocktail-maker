import sys
import requests


def drink_contains_ingredients(drink, ingredients):
    """Checks if drink found contains only ingredients found in ingredients list

    Args:
        drink (dict of (str,str)): Dictionary of drink attributes including strIngredient<1-15>
        ingredients (list of str): List of ingredients supported by cocktaildb.com

    Returns:
        bool: Does the drink contain the correct ingredients?
    """
    searchIngredient = set(ingredients)
    for key, value in drink.items():
        if "strIngredient" not in key: continue
        
        if value is not None and value.lower() not in searchIngredient:
            return False
        
    return True
    

def get_cocktails_with_ingredient(ingredients):
    """Accepts a list of ingredients and uses cocktaildb.com
    to obtain cocktails that can be made with those ingredients

    Args:
        ingredients (list of str): List of ingredients supported by cocktaildb.com

    Returns:
        list of str: List of cocktails that can be made with ingredients
    """
    if not isinstance(ingredients, list):
        raise TypeError("ingredients must be a list")
    
    # Remove invalid ingredients
    ingredients = [ingredient.lower() for ingredient in ingredients if isinstance(ingredient,str)]
    
    drinks_that_can_be_made = []
    already_processed_drinks = set()
    for ingredient in ingredients:
        # Get drinks associated with ingredient
        drink_response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}")
        for drink in drink_response.json()["drinks"]:
            drink_name = drink["strDrink"]
            
            # Ignore drinks that have either already been added or not able to be made
            if drink_name in already_processed_drinks: continue
            already_processed_drinks.add(drink_name)

            # Get all ingredients associated with each drink
            drink_detailed_response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink['idDrink']}")
            drink_data = drink_detailed_response.json()["drinks"][0]
            
            if drink_contains_ingredients(drink_data, ingredients):
                drinks_that_can_be_made.append(drink_name)
                
    return drinks_that_can_be_made


if __name__ == '__main__':
    ingredients = sys.argv[1].split(",")
    cocktails = get_cocktails_with_ingredient(ingredients)
    
    for cocktail in cocktails:
        print(cocktail)