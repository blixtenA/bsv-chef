import pytest
from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet, from_string

# Mock data for testing
recipes_high_readiness = [
    {'name': 'Salad', 'readiness': 0.9},
    {'name': 'Soup', 'readiness': 0.8},
    {'name': 'Pasta', 'readiness': 0.85},
    {'name': 'Curry', 'readiness': 0.7},
    {'name': 'Stew', 'readiness': 0.75}
]

# TC01
@pytest.mark.unit
def test_no_recipes_match_diet():
    print("running test_no_recipes_match_diet")
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=True)
    print(result)

    # Verify
    assert result is None

#TC02
@pytest.mark.unit
def test_all_high_readiness_take_best_true():
    for _ in range(10): # Run the test 10 times
        print("running test_all_high_readiness_take_best_true")
        
        # Setup
        controller = RecipeController(MagicMock())
        controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_high_readiness})
        diet = Diet.VEGAN

        # Execute
        result = controller.get_recipe(diet, take_best=True)

        print(result)
        # Verify
        assert result == 'Salad'

#TC03
@pytest.mark.unit
def test_all_high_readiness_take_best_false():
    results = []
    iterations = 10  # Run the test 10 times

    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_high_readiness})
    diet = Diet.VEGAN

    for _ in range(iterations):
        result = controller.get_recipe(diet, take_best=False)
        results.append(result)
        print(result) 

    # Check if not all results are the same
    assert len(set(results)) > 1, "Randomness check failed: All results are the same"