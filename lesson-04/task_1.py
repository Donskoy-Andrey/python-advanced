"""
Нужно реализовать класс Seq, который будет принимать в метод __init__
любую последовательность Sequence[T], где T - некоторый тип (generic).
Для класса Seq нужно будет реализовать методы map, filter и take.
"""


from typing import Sequence, Any, Callable


class Seq:
    """Sequence class"""

    def __init__(self, sequence: Sequence[Any]):
        self.sequence = list(sequence)

    def map(self, func: Callable[[Any], Any]) -> "Seq":
        """
        Map sequence

        :param func: callable, transform all sequence
        :return:
            Transformed sequence
        """
        new_sequence = []
        for element in self.sequence:
            new_sequence.append(func(element))
        return Seq(new_sequence)

    def filter(self, func: Callable[[Any], bool]) -> "Seq":
        """
        Filter sequence

        :param func: callable, filter elements from sequence
        :return:
            Filtered sequence
        """
        new_sequence = []
        for element in self.sequence:
            if func(element) is True:
                new_sequence.append(element)
        return Seq(new_sequence)

    def take(self, number: int) -> "Seq":
        """
        Slice sequence

        :param number: number of element to slice by
        :return:
            Sliced sequence
        """
        return Seq(self.sequence[:number])

    def __repr__(self):
        return str(self.sequence)


def main():
    """Entry point for task"""

    original_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    seq_instance = Seq(original_sequence)

    mapped_seq = seq_instance.map(lambda x: x ** 2)
    print('Mapped Sequence:', mapped_seq)

    filtered_seq = seq_instance.filter(lambda x: x % 2 == 0)
    print('Filtered Sequence:', filtered_seq)

    taken_elements = seq_instance.take(3)
    print('Taken Sequence:', taken_elements)

    lazy_map = seq_instance.take(3).map(float)
    print('Lazy Filtered Sequence:', lazy_map)

    lazy_filter = seq_instance.take(3).filter(lambda x: x > 0)
    print('Lazy Filtered Sequence:', lazy_filter)


if __name__ == '__main__':
    main()
