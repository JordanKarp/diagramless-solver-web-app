from enum import Enum, auto

from solver.symmetry import (
    RotationalSym,
    UpDownSym,
    LeftRightSym,
    DiagonalTLBRSym,
    DiagonalTRBLSym,
    DualRotationalSym,
    ThreeWaySym,
    SuperSym,
    Asymmetry,
)


class Value(Enum):
    """Represents possible values that can be assigned to a square in a crossword puzzle grid."""

    BLACK = auto()
    EMPTY = auto()
    ACROSS = auto()
    DOWN = auto()
    ACROSSDOWN = auto()
    UNKNOWN = auto()
    FINAL = auto()

    def __repr__(self):
        name = self.name.title()
        if name == "Acrossdown":
            name = "AcrossDown"
        return name

    def __str__(self):
        name = self.name.title()
        if name == "Acrossdown":
            name = "AcrossDown"
        return name


OPTIONS = {Value.ACROSS, Value.DOWN, Value.ACROSSDOWN, Value.BLACK, Value.EMPTY}

CLUES = {Value.ACROSS, Value.DOWN, Value.ACROSSDOWN}


SYMBOLS = {
    Value.BLACK: "\u2587",
    Value.EMPTY: "-",
    Value.ACROSS: "A",
    Value.DOWN: "D",
    Value.ACROSSDOWN: "Z",
    Value.UNKNOWN: "_",
    Value.FINAL: "Y",
}

SYMMETRIES = {
    "Rotational": RotationalSym,
    "Up Down": UpDownSym,
    "Left Right": LeftRightSym,
    "Diagonal TRBL": DiagonalTRBLSym,
    "Diagonal TLBR": DiagonalTLBRSym,
    "Dual Rotational": DualRotationalSym,
    "Three Way": ThreeWaySym,
    "Super": SuperSym,
    "Asymmetry": Asymmetry,
    "None": Asymmetry,
    "": Asymmetry,
}
