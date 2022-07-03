from shape import Shape


class Square(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Square'

class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Circle'

class Triangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Triangle'