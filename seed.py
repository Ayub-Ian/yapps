import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yapps.settings')
django.setup()

from core.models import Restaurant
from menu.models import Menu, MenuItem, Category
import snoop

@snoop
def create_seed_data():
    # Create Restaurants
    restaurant1 = Restaurant.objects.create(name='The Great Cafe')
    restaurant2 = Restaurant.objects.create(name='Pasta Paradise')

    # Create Menus
    breakfast_menu = Menu.objects.create(restaurant=restaurant1, name='Breakfast')
    lunch_menu = Menu.objects.create(restaurant=restaurant1, name='Lunch')
    drinks_menu = Menu.objects.create(restaurant=restaurant1, name='Drinks')
    
    dinner_menu = Menu.objects.create(restaurant=restaurant2, name='Dinner')
    drinks_menu_2 = Menu.objects.create(restaurant=restaurant2, name='Drinks')

    # Create Categories and Menu Items for Restaurant 1
    breakfast_category = Category.objects.create(menu=breakfast_menu, name='Breakfast Items')
    MenuItem.objects.create(name='Pancakes', description='Fluffy pancakes with syrup.', price=5.99, category=breakfast_category)
    MenuItem.objects.create(name='Omelette', description='Cheese and veggie omelette.', price=7.99, category=breakfast_category)

    lunch_category = Category.objects.create(menu=lunch_menu, name='Lunch Items')
    MenuItem.objects.create(name='Caesar Salad', description='Fresh Caesar salad with dressing.', price=8.99, category=lunch_category)
    MenuItem.objects.create(name='Club Sandwich', description='Classic club sandwich with fries.', price=10.99, category=lunch_category)

    drinks_category = Category.objects.create(menu=drinks_menu, name='Beverages')
    MenuItem.objects.create(name='Coffee', description='Freshly brewed coffee.', price=2.99, category=drinks_category)
    MenuItem.objects.create(name='Tea', description='A selection of fine teas.', price=2.49, category=drinks_category)

    # Create Categories and Menu Items for Restaurant 2
    dinner_category = Category.objects.create(menu=dinner_menu, name='Dinner Items')
    MenuItem.objects.create(name='Spaghetti Bolognese', description='Classic spaghetti with meat sauce.', price=12.99, category=dinner_category)
    MenuItem.objects.create(name='Fettuccine Alfredo', description='Creamy Alfredo pasta.', price=11.99, category=dinner_category)

    drinks_category_2 = Category.objects.create(menu=drinks_menu_2, name='Beverages')
    MenuItem.objects.create(name='Red Wine', description='A fine selection of red wines.', price=15.99, category=drinks_category_2)
    MenuItem.objects.create(name='Sparkling Water', description='Refreshing sparkling water.', price=1.99, category=drinks_category_2)



if __name__ == "__main__":
    create_seed_data()