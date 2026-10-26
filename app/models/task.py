from dataclasses import dataclass
from typing import List


@dataclass
class Shoe:
    id: int
    name: str
    description: str
    price: float


class ShoeModel:
    def __init__(self):
        self._shoes: List[Shoe] = []
        self._next_id = 1

    def add_shoe(self, name: str, description: str, price: float) -> bool:
        name = name.strip()
        description = description.strip()

        if not name or not description or price <= 0:
            return False

        shoe = Shoe(
            id=self._next_id,
            name=name,
            description=description,
            price=price
        )

        self._shoes.append(shoe)
        self._next_id += 1
        return True

    def get_all_shoes(self) -> List[Shoe]:
        return self._shoes.copy()

    def delete_shoe(self, shoe_id: int) -> bool:
        for shoe in self._shoes:
            if shoe.id == shoe_id:
                self._shoes.remove(shoe)
                return True

        return False