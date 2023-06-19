class Recipe:

    def __init__(self, count_ingred, list_of_ingred):
        self.count_ingred = count_ingred
        self.list_of_ingred = list_of_ingred




class ValidatedRecipe(Recipe):

    def __init__(self, recipe: Recipe, allCountA: int, allCountB: int, isValid: bool):
        super().__init__(recipe.count_ingred, recipe.list_of_ingred)
        self.allCountA = allCountA
        self.allCountB = allCountB
        self.isValid = isValid


class Question:

    def __init__(self, count_A, count_B, potion_number):
        self.count_A = count_A
        self.count_B = count_B
        self.potion_number = potion_number

class QuestionA(Question):

    def __init__(self, question: Question, answer):
        super().__init__(question.count_A, question.count_B, question.potion_number)
        self.answer = answer

# 7
# 3 1 1 2
# 2 1 3
# 3 4 3 4
# 1 7
# 1 6
# 3
# 8 4 5
# 9 2 5
# 10 10 6

def main():
    recipes_count = input()
    # составляем список рецептов
    # создаем список с двумя базовыми ингридиентами А и Б в виде базовых рецептов
    recipes_list = list([Recipe(1, list([1])), Recipe(1, list([2]))])
    i = 2
    while i < int(recipes_count):
        recipe_str = input()  # читаем строку рецепта
        recipe_list = [int(s) for s in recipe_str.split(' ')]
        count_ingred = recipe_list.pop(0)  # выбираем число ингридиентов
        recipes_list.append(Recipe(count_ingred, recipe_list))
        i += 1

    # составляем список вопросов
    question_count = input()
    question_list = list()
    i = 0
    while i < int(question_count):
        question_str = input()
        question_by_array = [int(s) for s in question_str.split(' ')]  # input to list
        question_list.append(Question(*question_by_array))
        i += 1

    resultStr = ''
    a_question_list = object_input(recipes_list, question_list)
    i = 0
    while i < len(a_question_list):
        resultStr += '1' if a_question_list[i].answer == True else '0'
        i += 1

    return resultStr




def object_input(recipes_list, question_list):
    validated_recipe_list = formationValidatedRecipeList(recipes_list)

    qIndex = 0
    while qIndex < len(question_list):
        question_list[qIndex] = QuestionA(question_list[qIndex], findAnswer(question_list[qIndex], validated_recipe_list))
        qIndex += 1

    return question_list



def findAnswer(question, validated_recipe_list):
    recipe : ValidatedRecipe = validated_recipe_list[question.potion_number - 1]
    if recipe.isValid == True:
        return recipe.allCountA <= question.count_A and recipe.allCountB <= question.count_B
    return False


def formationValidatedRecipeList(recipes_list):
    # формируем список проверенных рецептов
    validated_recipe_list = [None for x in range(len(recipes_list))]  # сразу создадим список нуного размера, чтобы в дальнейшем обращаться по индексу к рецепту
    validated_recipe_list[0] = ValidatedRecipe(Recipe(1, list([1])), 1, 0, True)
    validated_recipe_list[1] = ValidatedRecipe(Recipe(1, list([2])), 0, 1, True)

    recipeIndex = 2
    while recipeIndex < len(recipes_list):
        checkRecipe(recipeIndex, [], recipes_list, validated_recipe_list)
        recipeIndex += 1

    return validated_recipe_list


def checkRecipe(recipeIndex, loopCheckerList, recipes_list, validated_recipe_list):
    loopCheckerList.append(recipeIndex)  # добавляем изначально сами себя

    current_validating_recipe = ValidatedRecipe(recipes_list[recipeIndex], 0, 0, True)  # создаем объект текущего рецепта на проверке

    for ingredientIndex in recipes_list[recipeIndex].list_of_ingred:  # получаем cписок игридиентов (их индекс - 1)
        ingredient_recipe: ValidatedRecipe = checkIngredient(ingredientIndex - 1, loopCheckerList,  recipes_list, validated_recipe_list)
        if ingredient_recipe.isValid:
            current_validating_recipe = ValidatedRecipe(recipes_list[recipeIndex], current_validating_recipe.allCountA + ingredient_recipe.allCountA, current_validating_recipe.allCountB + ingredient_recipe.allCountB, True)
        else:
            current_validating_recipe = ValidatedRecipe(recipes_list[recipeIndex], 0, 0, False)
            break

    validated_recipe_list[recipeIndex] = current_validating_recipe

    return current_validating_recipe


def checkIngredient(ingredientIndex, loopCheckerList, recipes_list, validated_recipe_list):
    if loopCheckerList.count(ingredientIndex) == 0 : # проверяем. ссылается ли ингридиенты на самого себя или зацикленные рецепты
        # не ссылается
        # проверяем. есть ли в провереных рецептах рецепт нашего ингридиента
        if validated_recipe_list[ingredientIndex] is not None:
            return validated_recipe_list[ingredientIndex]
        else:
            return checkRecipe(ingredientIndex, loopCheckerList, recipes_list, validated_recipe_list)
    else: #  ссылается
        return ValidatedRecipe(recipes_list[ingredientIndex], 0, 0, False)



if __name__ == '__main__':
    print(main())