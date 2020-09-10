from csv import DictReader

from django.core.management import BaseCommand

from cookies.models import Cookie



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        if Cookie.objects.exists():
            print('Pet data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Cookies data for pets available for adoption")
        for row in DictReader(open('./cookies_data.csv')):
            cookie = Cookie()
            cookie.name = row['Cookie']
            cookie.calories = row['Calories']
            cookie.type = row['Type']
            cookie.size = row['Size']
            cookie.description = row['Cookie Description']
            cookie.imagepath = row['Cookie Image Path']
            cookie.save()

