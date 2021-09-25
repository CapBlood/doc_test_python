# https://docs.python.org/3/library/doctest.html

# TODO:
# 1. рассказать про стили документирования (Google и Numpy) и как это менять в pycharm
# 2. pandas как пример
# 3. https://docs.python.org/3/library/doctest.html
# 4. https://habr.com/ru/post/448782/
# 5. https://docs.pytest.org/en/6.2.x/doctest.html
# 6. https://stackoverflow.com/questions/49028611/pytest-cannot-find-module - как решить проблему если не видит package и его моудли
# 7. пример google style - https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
# 8. пример numpy style - https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
# 9. задание - задокументировать и сделать тесты для решения из ООП? а если не сделали? сделать заготовку?
# 10. добавить sphinx и doxygen
# 11. You can switch docstring style in Settings | Tools | Python Integrated Tools | Docstring format, you are looking for NumPy style I believe.
# 12. что значат проценты в pytest?
# 13. если аргумент может быть нескольких типов - https://stackoverflow.com/questions/53389169/python-google-docstring-format-more-than-one-type-for-argument
# 14. записать последовательно действий sphinx (как там менять rst, про директивы и прочее)
# 15. что значит maxdepth в sphinx
# 16. https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
# 17. что делают genindex, modindex и тд

# 18. сделать ещё примеры + doxygen
# 19. в дз добавить что надо всё залить на github? + залить доки куда-то? куда?
# 20. Module index выглядит хреново. что делать?
# 21. задание: задокументировать всё + написать тесты + выложить на github + выложить доки (сгенерированниые через sphinx)?
# 22. подробнее разобраться в pytest
# 23. сделать презентацию по типам тестирования?
# 24. сделать хорошие примеры для типов тестирования (типа восходящее тестирование)?
# 25. кто расскажет про git?
# 26. что писать в описании функции/класса? (загуглить)

# 27. СДЕЛАТЬ ПОДСЕКЦИИ В ДОКАХ????
# 28. сделать правильное версиционрование в readthedocs???
# 29. написать инструкцию к pytest в readme???
# 30. сделать сниппеты для git???
# 31. сделать примеры на google style???
# 32. сделать примеры на другие assert?
# 33. сделать ещё примеры для mock?
# 34. DOXYGEN!!!!
# 35. добавить https://setuptools.pypa.io/en/stable/userguide/datafiles.html???
# 36. разобрать __init__.py???
# 37. по поводу что такое wheel - https://packaging.python.org/discussions/wheel-vs-egg/
# 38. в доке было написано что чтобы пользовваться pip install --editable нужно делать setup.py, так ли это?
# ибо и без него работает
# 40. перечитать https://setuptools.pypa.io/en/stable/userguide/quickstart.html#setuptools-quickstart
# 41. можно ли устанавливвать несколько пакетов? подпакеты ставятся автоматически?
# 42. посмотреть как работает гит (индексы и прочее)
# 43. написать инструкцию к rst и sphinx???
# 44. как организовать именование тестов???
# 45. зачем начальные строки в conf.py???


def func_1(a, b):
    """Функция суммы двух аргументов.

    Parameters
    ----------
    a : Union[float, int]
        Первый операнд для суммирования.
    b : Union[float, int]
        Второй операнд для суммирования.

    Returns
    -------
    Union[float, int]
        Результат сложения двух операндов.

    Examples
    --------
    >>> func_1(1, 2)
    3
    >>> func_1(9, 9)
    18
    """

    return a + b


def func_2(a, b):
    """Функция умножения двух аргументов.

    Parameters
    ----------
    a : Union[float, int]
        Первый операнд для умножения.
    b : Union[float, int]
        Второй операнд для умножения.

    Returns
    -------
    Union[float, int]
        Результат умножения двух операндов.

    Examples
    --------
    >>> func_2(3, 3)
    9
    >>> func_2(2, 3)
    6
    """

    return a * b
