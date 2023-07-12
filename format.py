from data import FormatName

class Format:
    def __init__(
        self,
        name: FormatName,
        size: int,
        barColor: str,
    ):
        self.name = name
        self.size = size
        self.barColor = barColor