from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.screen import Screen


class Theater:
    def __init__(self, theater_id: int, name: str, city: str, screens: list["Screen"]):
        self.theater_id = theater_id
        self.name = name
        self.city = city
        self.screens = screens

    def __repr__(self):
        return f"Theater(theater_id={self.theater_id}, name={self.name}, city={self.city})"