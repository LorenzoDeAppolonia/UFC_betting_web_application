from database_script.populate_database_fight import populate_database_fight_from_csv
from database_script.populate_database_fighter import populate_database_fighter_from_csv
from database_script.populate_database_weight import populate_database_weight_from_csv
import os


def populate_database():
    flag_file = 'db_initialized.flag'

    if os.path.exists(flag_file):
        print("Databases already populated. Skipping population.")
        return True

    try:
        populate_database_fighter_from_csv('preprocessing/preprocessed_data.csv')
        populate_database_weight_from_csv('preprocessing/preprocessed_data.csv')
        populate_database_fight_from_csv('preprocessing/preprocessed_data.csv')

        # Create the flag file after successful population
        open(flag_file, 'a').close()
        print("All databases populated successfully.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
