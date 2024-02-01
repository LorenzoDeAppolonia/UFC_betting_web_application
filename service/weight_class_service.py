from typing import List
from sqlalchemy.exc import SQLAlchemyError
from db_models.weight_class import WeightClass
from exceptions.ufc_betting_error import UfcBettingError


class WeightClassService:

    @staticmethod
    def get_weight_class_statistics(code: int) -> dict | None | bool:
        try:
            weight_class = WeightClass.query.filter_by(code=code).one_or_none()
            return weight_class.to_dict() if weight_class else None

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_weight_classes() -> List[dict] | bool:
        try:
            weight_classes = WeightClass.query.distinct().all()
            return [weight_class.to_dict() for weight_class in weight_classes]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))
