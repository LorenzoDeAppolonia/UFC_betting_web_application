import pandas as pd
from db_models.fighter import Fighter
from application.db import db
from sqlalchemy.exc import SQLAlchemyError


def add_fighter_if_new(fighters_set, name, height, reach, stance):
    if name not in fighters_set:
        fighter = Fighter(
            name=name,
            height=height,
            reach=reach,
            stance=stance
        )
        try:
            db.session.add(fighter)
            fighters_set.add(name)
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return False
    return False


def populate_database_fighter_from_csv(csv_file_path):

    if Fighter.query.first() is not None:
        print("Fighter table already populated. Skipping population.")
        return

    print("start populating fighter")

    df = pd.read_csv(csv_file_path)
    df['R_Height_cms'] = pd.to_numeric(df['R_Height_cms'], errors='coerce').fillna(0)
    df['R_Reach_cms'] = pd.to_numeric(df['R_Reach_cms'], errors='coerce').fillna(0)
    df['B_Height_cms'] = pd.to_numeric(df['B_Height_cms'], errors='coerce').fillna(0)
    df['B_Reach_cms'] = pd.to_numeric(df['B_Reach_cms'], errors='coerce').fillna(0)
    df['R_Stance'].fillna('', inplace=True)
    df['B_Stance'].fillna('', inplace=True)

    existing_fighters = set(f.name for f in Fighter.query.all())
    new_fighters = set()

    for index, row in df.iterrows():
        red_fighter_name = row['R_fighter']
        blue_fighter_name = row['B_fighter']

        if add_fighter_if_new(existing_fighters, red_fighter_name,
                              row['R_Height_cms'], row['R_Reach_cms'], row['R_Stance']):
            new_fighters.add(red_fighter_name)

        if add_fighter_if_new(existing_fighters, blue_fighter_name,
                              row['B_Height_cms'], row['B_Reach_cms'], row['B_Stance']):
            new_fighters.add(blue_fighter_name)

    try:
        db.session.commit()

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        return False

    print("\nFIGHTER table population finished.\n")

    return True




