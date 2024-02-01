import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from db_models.fight import Fight
from db_models.fighter import Fighter
from db_models.weight_class import WeightClass
from application.db import db
import hashlib


def get_fighter_code(name):
    fighter = Fighter.query.filter_by(name=name).first()
    return fighter.code if fighter else None


def fight_exists(code):
    fight = Fight.query.filter_by(code=code).first()
    return fight is not None


def get_weight_class_code(weight_class):
    weight_class_obj = WeightClass.query.filter_by(weight=weight_class).first()
    return weight_class_obj.code if weight_class_obj else None


def populate_database_fight_from_csv(csv_file_path):

    if Fight.query.first() is not None:
        print("Fight table already populated. Skipping population.")
        return

    print("start populating fight")

    df = pd.read_csv(csv_file_path)

    df['Referee'].fillna('Unknown', inplace=True)
    df['R_age'] = pd.to_numeric(df['R_age'], errors='coerce').fillna(0)
    df['B_age'] = pd.to_numeric(df['B_age'], errors='coerce').fillna(0)
    df['B_Weight_lbs'] = pd.to_numeric(df['B_Weight_lbs'], errors='coerce').fillna(0)
    df['R_Weight_lbs'] = pd.to_numeric(df['R_Weight_lbs'], errors='coerce').fillna(0)
    new_fights = 0

    for index, row in df.iterrows():
        red_fighter_code = get_fighter_code(row['R_fighter'])
        blue_fighter_code = get_fighter_code(row['B_fighter'])

        fight = Fight(
                referee=row['Referee'],
                location=row['location'],
                fight_date=pd.to_datetime(row['date']),
                weight_class_code=get_weight_class_code(row['weight_class']),
                winner=row['Winner'],
                fighter_rc_code=red_fighter_code,
                fighter_bc_code=blue_fighter_code,
                age_rc=row['R_age'],
                weight_rc=row['R_Weight_lbs'],
                win_streak_rc=row['R_current_win_streak'],
                wins_rc=row['R_wins'],
                losses_rc=row['R_losses'],
                age_bc=row['B_age'],
                weight_bc=row['B_Weight_lbs'],
                win_streak_bc=row['B_current_win_streak'],
                wins_bc=row['B_wins'],
                losses_bc=row['B_losses'],
            )
        db.session.add(fight)
        new_fights += 1

    try:
        if new_fights:
            db.session.commit()
        else:
            print("No new fights to add.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"An error occurred while populating fights: {e}")
        return False

    print("\nFIGHT table population finished.\n")

    return True


