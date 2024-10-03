import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yapps.settings')
django.setup()

from core.models import Restaurant
from menu.models import Menu, MenuItem, Category


def create_seed_data():
    # Create Restaurants
    restaurant1 = Restaurant.objects.create(name='The Great Cafe', description="Traditional cafe cuisine from those who brought you the best before.", image_url="https://pixabay.com/photos/french-restaurant-brewery-paris-dog-2506490/")
    restaurant2 = Restaurant.objects.create(name='Pasta Paradise', description="Traditional italian cuisine from those who brought you La Mariana", image_url="https://pixabay.com/photos/restaurant-table-setting-table-449952/")

    # Create Menus
    breakfast_menu = Menu.objects.create(restaurant=restaurant1, name='Breakfast', image_url="https://pixabay.com/photos/food-breakfast-table-healthy-green-2569257/")
    lunch_menu = Menu.objects.create(restaurant=restaurant1, name='Lunch')
    drinks_menu = Menu.objects.create(restaurant=restaurant1, name='Drinks', image_url="https://pixabay.com/photos/glass-drink-cocktail-soft-drink-7482792/")

    dinner_menu = Menu.objects.create(restaurant=restaurant2, name='Dinner')
    drinks_menu_2 = Menu.objects.create(restaurant=restaurant2, name='Drinks', image_url="https://pixabay.com/photos/cocktail-drink-glass-beverage-389798/")

    # Create Categories and Menu Items for Restaurant 1
    breakfast_category = Category.objects.create(menu=breakfast_menu, name='Breakfast Items')
    MenuItem.objects.create(name='Pancakes', description='Fluffy pancakes with syrup.', price=5.99, category=breakfast_category, image_url="https://pixabay.com/photos/food-pancakes-breakfast-fatty-eat-715541/")
    MenuItem.objects.create(name='Omelette', description='Cheese and veggie omelette.', price=7.99, category=breakfast_category, image_url="https://pixabay.com/photos/breakfast-cheese-cooked-delicious-8266548/")

    lunch_category = Category.objects.create(menu=lunch_menu, name='Lunch Items')
    MenuItem.objects.create(name='Caesar Salad', description='Fresh Caesar salad with dressing.', price=8.99, category=lunch_category, image_url="https://pixabay.com/photos/salad-lambs-lettuce-corn-salad-7003903/")
    MenuItem.objects.create(name='Club Sandwich', description='Classic club sandwich with fries.', price=10.99, category=lunch_category, image_url="https://pixabay.com/photos/bread-sandwich-food-plate-toast-1867208/")

    drinks_category = Category.objects.create(menu=drinks_menu, name='Beverages')
    MenuItem.objects.create(name='Coffee', description='Freshly brewed coffee.', price=2.99, category=drinks_category, image_url="https://pixabay.com/photos/coffee-cup-caffeine-espresso-4618705/")
    MenuItem.objects.create(name='Tea', description='A selection of fine teas.', price=2.49, category=drinks_category, image_url="https://pixabay.com/photos/herbal-tea-tea-herbs-cups-teacups-1410565/")

    # Create Categories and Menu Items for Restaurant 2
    dinner_category = Category.objects.create(menu=dinner_menu, name='Dinner Items')
    MenuItem.objects.create(name='Spaghetti Bolognese', description='Classic spaghetti with meat sauce.', price=12.99, category=dinner_category, image_url="https://pixabay.com/photos/spaghetti-bolognese-parmesan-meal-787048/")
    MenuItem.objects.create(name='Fettuccine Alfredo', description='Creamy Alfredo pasta.', price=11.99, category=dinner_category, image_url="https://pixabay.com/photos/alfredo-fettuccine-pasta-cheese-8305773/")

    drinks_category_2 = Category.objects.create(menu=drinks_menu_2, name='Beverages')
    MenuItem.objects.create(name='Red Wine', description='A fine selection of red wines.', price=15.99, category=drinks_category_2, image_url="https://pixabay.com/photos/wine-red-wine-glass-drink-alcohol-541922/")
    MenuItem.objects.create(name='Sparkling Water', description='Refreshing sparkling water.', price=1.99, category=drinks_category_2, image_url="https://pixabay.com/photos/water-glass-sparkling-water-glass-3971098/")


if __name__ == "__main__":
    create_seed_data()
