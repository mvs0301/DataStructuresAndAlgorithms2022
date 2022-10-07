def cook_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"Готовим вкусную {size}-дюймовую пиццу с начинкой:")
    for t in toppings:
        print(f'- {t}')