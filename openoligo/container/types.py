"""
A cartridge is a container containing a set of different categories of reagents,
in 2 different sizes of bottles (small and large).
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BottleSize(Enum):
    """The type of container."""

    SMALL = 1
    LARGE = 2


class ReagentType(Enum):
    """The type of reagent."""

    LIQUID = 1
    LYOPHILIZED = 2


class ReagentCategory(str, Enum):
    """The category of reagent."""

    CAPPING = "capping"
    DEPROTECTION = "deprotection"
    COUPLING = "coupling"
    ACTIVATION = "activation"
    PHOSPHORAMIDITE = "phosphoramidite"
    SOLVENT = "solvent"


class SlotID(Enum):
    """The ID of the bottle slot."""

    A1 = 1
    A2 = 2
    A3 = 3
    A4 = 4
    A5 = 5
    A6 = 6
    A7 = 7
    A8 = 8

    B1 = 9
    B2 = 10
    B3 = 11
    B4 = 12
    B5 = 13
    B6 = 14
    B7 = 15
    B8 = 16

    C1 = 17
    C2 = 18
    C3 = 19
    C4 = 20
    C5 = 21
    C6 = 22
    C7 = 23
    C8 = 24

    D1 = 25
    D2 = 26
    D3 = 27
    D4 = 28
    D5 = 29
    D6 = 30
    D7 = 31
    D8 = 32


@dataclass
class Reagent:
    """A reagent."""

    name: str
    type: ReagentType
    category: ReagentCategory
    description: str = ""


@dataclass
class Slot:
    """A slot in the cartridge."""

    slot_id: SlotID
    associated_valve: int
    reagent: Optional[Reagent]
    size: BottleSize = BottleSize.SMALL
    associated_solvent: Optional[Reagent] = None
