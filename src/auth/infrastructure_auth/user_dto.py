from typing import Dict

from domain_auth.entities import User


class UserDTO:
    @staticmethod
    def to_dto(user: User) -> Dict:
        return {
            "user_id": user.user_id,
            "username": user.username,
            "password": user.password,
            "first_name": user.first_name,
            "phone": user.phone,
            "address": user.address,
        }

    @staticmethod
    def from_dto(data: Dict) -> User:
        return User(
            user_id=data["user_id"],
            username=data["username"],
            first_name=data["first_name"],
            phone=data["phone"],
            address=data["address"],
            password=data["password"],
        )
