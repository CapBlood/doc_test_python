class ComparedStr(str):
    """Класс строки, поддерживающий сравнение по длине.

    Examples
    --------
    >>> word = ComparedStr("word")
    >>> another_word = ComparedStr("anotherWord")
    >>> word == another_word
    False
    """

    def __eq__(self, other):
        return len(self) == len(other)
