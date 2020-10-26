# Joseph Chetta 1640405

class FoodItem:
    def __init__(self, name='None', fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = float(((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings)
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, calories))
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    #total = int(input())
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    servings = float(input())

    food = FoodItem()
    food.print_info()
    food.get_calories(servings)
    print()
    food = FoodItem(name, fat, carbs, protein)
    food.print_info()
    food.get_calories(servings)


