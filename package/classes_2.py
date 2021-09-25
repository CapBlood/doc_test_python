class Table:
    """Хранилище для табличных данных.

    Attributes
    ----------
    rows : list
        Строки таблицы.
    n_cols : int
        Количество столбцов.

    Examples
    --------
    >>> table = Table(2)
    >>> table.add_row([1, 2])
    >>> table.add_row([3, 4])
    >>> table.get_table()
    [[1, 2], [3, 4]]
    >>> table.shape()
    (2, 2)
    """

    def __init__(self, n_cols):
        self.rows = []
        self.n_cols = n_cols

    def shape(self):
        return len(self.rows), self.n_cols

    def get_table(self):
        return self.rows

    def add_row(self, item):
        if len(item) != self.n_cols:
            raise Exception("Некорректная длина")
        self.rows.append(item)


class TableFormatter:
    """Класс для форматирования таблицы.

    Attributes
    ----------
    _table : Table
        Таблица с данными для форматирования.

    Examples
    --------
    >>> table = Table(2)
    >>> table.add_row([1, 2])
    >>> table.add_row([3, 4])
    >>> formatter = TableFormatter(table)
    >>> print(formatter.to_csv())
    1,2
    3,4
    """

    def __init__(self, table):
        self._table = table

    def to_csv(self):
        """Форматирование таблицы в csv-формат.

        Returns
        -------
        str
            Таблица в строковом представлении в формате csv.
        """

        return "\n".join(
            ",".join(map(str, row)) for row in self._table.get_table())


if __name__ == "__main__":
    table = Table(3)
    table.add_row([1, 2, 3])
    table.add_row([4, 5, 6])
    formatter = TableFormatter(table)
    result = formatter.to_csv()
    print(result)
