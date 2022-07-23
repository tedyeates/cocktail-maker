import unittest
import cocktail_maker

class TestCocktailMaker(unittest.TestCase):
    def test_empty_ingredient_list(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([])
        self.assertEqual(cocktails, [])
    
    def test_skips_invalid_ingredient(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([1, 2])
        self.assertEqual(cocktails, [])
    
    def test_small_ammount_of_ingredients(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient(["lime", "light rum" "mint", "soda water"])
        self.assertTrue("Mojito" in cocktails)
    
    def test_large_ammount_of_ingredients(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([
            "lime", "mint", "sugar", "tea", "rum", "gin", "vodka", "Orange", "Grape juice", "Carbonated soft drink", "Sherbet", "Dark rum", "Surge", "Cranberry juice"
        ])
        
        self.assertTrue("Halloween Punch" in cocktails)
        self.assertTrue("Bleeding Surgeon" in cocktails)