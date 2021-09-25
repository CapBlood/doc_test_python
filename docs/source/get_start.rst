Getting started
========================
Данный пакет предоставляет функционал для арифметических операций, работы со строками,
а также дополнительные контейнерные типы.

Класс Table позволяет хранить табличные данные:

.. code-block:: python

    >>> from package import classes_2
    >>> table = Table(2)
    >>> table.add_row([1, 2])
    >>> table.add_row([3, 4])
    >>> formatter = TableFormatter(table)
    >>> print(formatter.to_csv())
    1,2
    3,4

Класс ComparedStr позволяет создавать строки сравнимые по длине:

.. code-block:: python

    >>> word = ComparedStr("word")
    >>> another_word = ComparedStr("anotherWord")
    >>> word == another_word
    False

Арифметические функции func_1 и func_2 позволяют складывать и умножать числа.

.. code-block:: python

    >>> func_1(1, 2)
    3
    >>> func_1(9, 9)
    18

    >>> func_2(3, 3)
    9
    >>> func_2(2, 3)
    6