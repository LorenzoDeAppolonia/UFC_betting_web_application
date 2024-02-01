import pandas as pd
from db_models.weight_class import WeightClass
from sqlalchemy.exc import SQLAlchemyError
from application.db import db


def populate_database_weight_from_csv(csv_file_path):

    if WeightClass.query.first() is not None:
        print("WeightClass table already populated. Skipping population.")
        return

    print("start populating weight_class")

    df = pd.read_csv(csv_file_path)
    existing_weights = set(w.weight for w in WeightClass.query.all())
    added_weights = set()

    for index, row in df.iterrows():
        weight = row['weight_class']
        if weight not in existing_weights and weight not in added_weights:
            weight_class = WeightClass(
                weight=weight
            )
            db.session.add(weight_class)
            added_weights.add(weight)

    try:
        if added_weights:
            db.session.commit()
#            print(f"Added new weight classes: {added_weights}")
        else:
            print("No new weight classes to add.")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        return False

    print("\nWEIGHT_CLASS table population finished.\n")

    return True

