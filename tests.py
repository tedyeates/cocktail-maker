import unittest
import cocktail_maker

class TestCocktailMaker(unittest.TestCase):
    def test_invalid_ingredients(self):
        with self.assertRaises(TypeError):
            cocktail_maker.get_cocktails_with_ingredient(2)
        
        
    def test_empty_ingredient_list(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([])
        self.assertEqual(cocktails, set())
    
    def test_skips_invalid_ingredient(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([1, 2])
        self.assertEqual(cocktails, set())
    
    def test_small_ammount_of_ingredients(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient(["lime", "light rum", "mint", "sugar", "soda water"])
        self.assertTrue("Mojito" in cocktails)
    
    def test_large_ammount_of_ingredients(self):
        cocktails = cocktail_maker.get_cocktails_with_ingredient([
            "lime", "mint", "sugar", "tea", "rum", "gin", "vodka", "Orange", "Grape juice", "Carbonated soft drink", "Sherbet", "Dark rum", "Surge", "Cranberry juice"
        ])
        
        self.assertTrue("Holloween Punch" in cocktails)
        self.assertTrue("Bleeding Surgeon" in cocktails)

if __name__ == '__main__':
    unittest.main()