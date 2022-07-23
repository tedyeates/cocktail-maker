# cocktail-maker
Application for querying what cocktails can be made from specified ingredients

## Quick Start
To run the program use `python -m cocktail_maker ingredient1,ingredient2,"ingredient with spaces"` for example `python -m cocktail_maker lime,"light rum",mint,sugar,"soda water"` should return "Mojito"

## Notes
The api for searching by multiple ingredients is available only to patreons, using this could avoid numerous api calls which would greatly improve the speed of the program. The api data returned seems incomplete, for instance https://thecocktaildb.com/api/json/v1/1/filter.php?i=Soda%20water does not return "Mojito" despite it showing it as an ingredient in it's ingredient list.
