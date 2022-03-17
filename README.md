# Оглавление
1. [Github](#github)
2. [Readthedocs](#readthedocs)
3. [Дистрибуция пакета](#setup)
4. [Запуск тестов](#test)
5. [Генерация документации](#gen_doc)
6. [Примеры документирования](#doc_examples)
7. [Популярные команды Git](#github_commands)
8. [Полезные ссылки](#references)

<a name="github"></a>
## Создание репозитория Github
1. `git init` в корневой директории проекта.
2. Затем создать там же файл `.gitignore`, куда необходимо вписать пути файлов/директорий,
которые не будут отслеживаться в Git и, следовательно, не будут отправляться в репозиторий.
3. `git add .` для добавления всех файлов/директорий (кроме тех, что написаны .gitignore) в Git для
отслеживания.
4. Создать репозиторий непосредственно на Github.
5. `git remote add origin path-to-git-repo` (путь отобразится после создания репозитория).
6. `git push -u origin name-branch`
(указывается имя ветки, которую необходимо загрузить в репозиторий).

### Пример .gitignore
```gitignore
__pycache__
venv
.pytest_cache
docs/build
```

<a name="readthedocs"></a>
## Создание документации на Readthedocs
1. В корне репозитория необходимо создать директорию docs.
И [сгенерировать](#gen_doc) в ней исходники sphinx.
2. Создать файл requirements.txt в docs для указания зависимостей для sphinx (например, расширения).
3. Создать конфигурационный файл .readthedocs.yaml в корне для Readthedocs,
указав пути к conf.py для sphinx и requirements.txt.
4. Сделать коммит и загрузить в репозиторий на Github.
5. Зарегистрироваться на Readthedocs, связать аккаунт с аккаунтом на Github
и импортировать с Github проект с документацией.
6. Документация автоматически соберется и
будет через некоторое время доступна по ссылке, указанной в настройках проекта на Readthedocs. 

Далее документация будет обновляться при каждом обновлении ветки,
которая указана в настройках проекта в Readthedocs. 

[Туториал](https://docs.readthedocs.io/en/stable/tutorial/) \
[Конфигурация Readthedocs](https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html#using-a-configuration-file) \
[Пример документации этого репозитория](https://doc-test-python.readthedocs.io/en/latest/)

### Пример requirements.txt
```requirements.txt
sphinx==3.4.3
sphinx_rtd_theme==0.5.1
sphinxcontrib-napoleon
```

### Пример конфигурационного файла Readthedocs
```yaml
# File: .readthedocs.yaml

version: 2

sphinx:
  configuration: docs/source/conf.py

python:
  version: 3.7
  install:
    - requirements: docs/requirements.txt
```

<a name="setup"></a>
## Дистрибуция пакета
Для дистрибуции далее
будет использоваться библиотека [setuptools](https://pypi.org/project/setuptools/).

1. Создать в корне проекта [pyproject.toml](#pyproject_example)
с указанием инструментов, необходимых для установки проекта (setuptools в данном случае).
2. Создать в корне и настроить [setup.py](#setup_example_2) для проекта
или создать и настроить [setup.cfg](#setup_example). 
3. Теперь пакет готов для инсталляции с помощью команды `pip install .` из корня проекта.

Также можно установить проект в режиме [разработки](https://setuptools.pypa.io/en/stable/userguide/quickstart.html#development-mode)
(для тестирования). В таком случае pip создаст ярлык в директории с другими установленными пакетами
с ссылкой на исходный код. Тогда при редактировании кода изменения вступают в силу без
переустановки. Выполняется это следующей командой: `pip install --editable .`.

Можно собрать одиночный файл формата whl, в котором будет содержаться проект для установки с помощью pip.
Такой файл можно собрать при помощи утилиты `build` (`pip install build`).
Далее в корне вызвать команду `python -m build`. Файл появится в директории dist.
Далее этот файл можно опубликовать в репозиторий PyPI
(откуда устанавливается большая часть библиотек/утилит с помощью pip)
через утилиту [twine](https://pypi.org/project/twine/).
Откуда он уже будет доступен для установки через pip.
Сам файл также можно установить локально командой `pip install some-package.whl`.
Перед выкладыванием проекта на PyPI рекомендуется указать дополнительную информацию
(имя разработчика/мейнтейнера, почта для связи, ссылка на исходный код и т.д.). 

<a name="setup_example"></a>
### Пример setup.cfg
```buildoutcfg
;setup.cfg

[metadata]
;Название проекта
name = example-package
;Версия
version = 1.0

[options]
;Пакеты, входящий в проект
packages =
    package
;    package2
;    package3

;Зависимости
;install_requires =
;    requests
;    importlib; python_version == "2.6"
```

<a name="setup_example_2"></a>
### Пример setup.py
```python
from setuptools import setup

setup(name="example-package",
      description="Python example project",
      author="CapBlood",
      packages=["package"])
```

<a name="pyproject_example"></a>
### Пример pyproject.toml
```ini
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

[Более подробная настройка setup.cfg](https://setuptools.pypa.io/en/stable/userguide/quickstart.html) \
[Настройка setup.py](https://docs.python.org/3/distutils/setupscript.html) \
[Загрузка на PyPi](https://pypi.org/project/twine/)

<a name="test"></a>
## Запуск тестов
Примеры запускаются из корня проекта.

### Пример unittest:
```shell script
python -m unittest unit_tests.test_module 
```

### Пример doctest
```shell script
python -m doctest -v package/module.py   
```

### Пример pytest
```shell script
pytest
```

<a name="gen_doc"></a>
## Генерация документации
### Sphinx
1. `mkdir docs`
2. `cd docs`
3. `sphinx-quickstart`

Для возможности автоматического извлечения докстрок классов и функций
(например, `.. automodule:: <module_name>`),
которые написаны в стиле Numpy и Google, необходимо расширение для sphinx
[sphinx.ext.napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html). 

[Тема для HTML](https://github.com/readthedocs/sphinx_rtd_theme) \
[Источник](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) \
[Ещё один гайд по Sphinx](https://dinhanhthi.com/sphinx-restructuredtext/)

<a name="doc_examples"></a>
## Примеры документирования
### Numpy style
Пример:
```python
def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : :obj:`str`, optional
        The second parameter.
    *args
        Variable length argument list.
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    bool
        True if successful, False otherwise.

        The return type is not optional. The ``Returns`` section may span
        multiple lines and paragraphs. Following lines should be indented to
        match the first line of the description.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError
        If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True
```
[Больше примеров](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)

### Google style
```python
def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True
```
[Больше примеров](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

<a name="github_commands"></a>
## Популярные команды Git
- `git rebase -i [branch]` - удаление, редактирование, объединение и т.п. коммитов текушей ветки
или указанной
(также можно добавить флаг `--root` для возможности указанных операций надо самым первым коммитом);
- `git stash` - спрятать последние локальные изменения в стэк;
- `git log` - вывод лога коммитов;
- `git reflog` - журнал истории изменений HEAD;
- `git diff` - команда, показывающая изменения между коммитами в проекте.

<a name="references"></a>
## Полезные ссылки
### Примеры проектов с открытым исходным кодом
- [Django](https://github.com/django/django)
- [Nose](https://github.com/nose-devs/nose)

### Документации
- [Git](https://git-scm.com/)
- [RestructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [Setuptools](https://setuptools.pypa.io/en/latest/)