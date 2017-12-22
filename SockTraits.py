from enum import Enum, auto

class Color(Enum):
    White = auto()
    Blue = auto(),
    Yellow = auto(),
    Black = auto(),
    Green = auto(),
    Red = auto()

class Length(Enum):
    Ankle = auto(),
    Knee = auto(),
    Calf = auto(),
    MidCalf = auto(),
    Crew = auto(),
    QuarterLength = auto()

class Material(Enum):
    Cotton = auto(),
    Wool = auto(),
    Nylon = auto(),
    Acrylic = auto(),
    Polyester = auto(),
    Spandex = auto()

class Pattern(Enum):
    Plain = auto(),
    MarkedHeel = auto(),
    MarkedToe = auto(),
    MarkedToeAndHeel = auto(),
    Stars = auto(),
    Stripes = auto()

class Size(Enum):
    Small = auto(),
    Medium = auto(),
    Large = auto()

