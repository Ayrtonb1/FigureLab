from figurelab.recipes.models import ProcessingStep, Recipe


def test_recipe_preserves_ordered_steps():
    recipe = Recipe(
        name="example",
        steps=(
            ProcessingStep("baseline", {"method": "example"}),
            ProcessingStep("smooth", {"window": 5}),
        ),
    )

    assert [step.operation for step in recipe.steps] == ["baseline", "smooth"]
