import sys


def get_cocktails_with_ingredient(ingredients):
    """Accepts a list of ingredients and uses cocktaildb.com
    to obtain cocktails that can be made with those ingredients

    Args:
        ingredients (list of str): List of ingredients supported by cocktaildb.com

    Returns:
        list of str: List of cocktails that can be made with ingredients
    """
    
    
    return []

if __name__ == '__main__':
    ingredients = sys.argv[1].split(",")
    cocktails = get_cocktails_with_ingredient(ingredients)
    
    for cocktail in cocktails:
        print(cocktail)