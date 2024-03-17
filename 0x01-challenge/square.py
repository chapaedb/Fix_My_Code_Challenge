class Square:
    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if value < 0:
            raise ValueError("Side length cannot be negative.")
        self.__side_length = value

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length

    def __str__(self):
        return "Square (Side Length: {})".format(self.__side_length)


if __name__ == "__main__":
    s = Square(side_length=5)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

    s.side_length = 10
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
