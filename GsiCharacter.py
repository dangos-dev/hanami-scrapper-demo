from dataclasses import dataclass
from typing import Any

'''
Proporciona una estructura de datos para representar personajes con sus atributos principales
El método from_row() facilita la creación de objetos GsiCharacter a partir de datos extraídos de una tabla HTML
'''

@dataclass
class GsiCharacter:
    name: str
    rarity: str
    weapon: str
    element: str

    @staticmethod
    def from_row(row: Any, coltag='td') -> 'GsiCharacter':
        data = row.find_all(coltag)  # Obtiene todas las columnas de la línea

        # Se omite la validación de en que index se encuentra la columna con los datos esperados
        o_name = data[1].get_text()
        o_rariry = data[2].get_text()
        o_weapon = data[3].get_text()
        o_element = data[4].get_text()

        return GsiCharacter(o_name, o_rariry, o_weapon, o_element)
