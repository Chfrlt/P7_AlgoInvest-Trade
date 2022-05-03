class Stock:
    def __init__(self, name: str, price: float, benefit: float) -> None:
        self.name = name
        self.price = price
        self.percent = benefit / 100
        self.benefit = self.price * self.percent
        self.ratio = self.benefit // self.price if self.price > 0 else 0

    def __repr__(self) -> str:
        return f"{self.name}"

    def __lt__(self, other):
        return self.ratio > other.ratio
