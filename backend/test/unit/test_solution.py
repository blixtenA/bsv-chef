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

recipes_mixed_readiness = [
    {'name': 'Salad', 'readiness': 0.9},
    {'name': 'Soup', 'readiness': 0.05},
    {'name': 'Pasta', 'readiness': 0.1},
    {'name': 'Curry', 'readiness': 0.02},
    {'name': 'Stew', 'readiness': 0.3}
]

recipes_low_readiness = [
    {'name': 'Salad', 'readiness': 0.05},
    {'name': 'Soup', 'readiness': 0.04},
    {'name': 'Pasta', 'readiness': 0.02},
    {'name': 'Curry', 'readiness': 0.01},
    {'name': 'Stew', 'readiness': 0.03}
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
    print("running test_all_high_readiness_take_best_false")
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_high_readiness})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=False)
    print(result)

    # Verify
    # Should be a random choice from high readiness recipes
    assert result in ['Salad', 'Soup', 'Curry', 'Pasta', 'Stew']  

#TC04
@pytest.mark.unit
def test_mixed_readiness_take_best_true():
    print("running test_mixed_readiness_take_best_true")
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_mixed_readiness})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=True)
    print(result)

    # Verify
    assert result == 'Salad' 

#TC05
@pytest.mark.unit
def test_mixed_readiness_take_best_false():
    print("running test_mixed_readiness_take_best_false")    
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_mixed_readiness})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=False)
    print(result)

    # Verify
    # Random choice but only from those above 0.1
    assert result in ['Salad', 'Pasta', 'Stew']  

#TC06
@pytest.mark.unit
def test_all_low_readiness_take_best_true():
    print("running test_all_low_readiness_take_best_true")       
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_low_readiness})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=True)
    print(result)
    # Verify
    assert result is None

#TC07
@pytest.mark.unit
def test_all_low_readiness_take_best_false():
    print("running test_all_low_readiness_take_best_false")        
    # Setup
    controller = RecipeController(MagicMock())
    controller.get_readiness_of_recipes = MagicMock(return_value={r['name']: r['readiness'] for r in recipes_low_readiness})
    diet = Diet.VEGAN

    # Execute
    result = controller.get_recipe(diet, take_best=False)
    print(result)
    # Verify
    assert result is None