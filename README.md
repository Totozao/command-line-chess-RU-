[![Run on Repl.it](https://repl.it/badge/github/marcusbuffett/command-line-chess)](https://repl.it/github/marcusbuffett/command-line-chess)

# command-line-chess

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/marcusbuffett/command-line-chess/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI download month](https://img.shields.io/pypi/dm/cl-chess.svg)](https://pypi.python.org/project/cl-chess/)
[![PyPi version](https://badgen.net/pypi/v/cl-chess/)](https://pypi.org/project/cl-chess)
[![GitHub issues](https://img.shields.io/github/issues/marcusbuffett/command-line-chess.svg)](https://GitHub.com/marcusbuffett/command-line-chess/issues/)
[![GitHub watchers](https://img.shields.io/github/watchers/marcusbuffett/command-line-chess.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/marcusbuffett/command-line-chess)
[![GitHub stars](https://img.shields.io/github/stars/marcusbuffett/command-line-chess.svg?style=social&label=Star&maxAge=2592000)](https://github.com/marcusbuffett/command-line-chess)


Программа на языке python для игры в шахматы с искусственным интеллектом в терминале.

Также ознакомьтесь с другим моим проектом - [шахматным обучающим сайтом].(https://chessmadra.com/).

## Особенности

- Игра в шахматы против искусственного интеллекта в терминале
- Режим двух игроков (для входа выполните команду `chess --two`)
- возможные команды:
    * `a3`, `Nc3`, `Qxa` и т.д.: сделать ход
    * `l`: печатает каждый законный ход
    * `r`: сделать случайный ход
    * `u`: отменить последний ход
    * `quit`: выйти из текущей игры
    * `gm`: распечатывает ходы текущей игры в формате PGN
    * `?`: помощь, выводит все доступные команды

## Скриншоты
Исходное состояние:

![Initial](https://i.imgur.com/PSS7csc.png)

Первый ход:

![First move](https://i.imgur.com/AsXhhvC.png)

## Установка

### Установить из [PyPI](https://pypi.org/project/cl-chess/)
Просто выполните следующую команду:
```
pip install cl-chess
```

### Установка из исходного кода
- Сначала клонируйте репозиторий:
```
git clone https://github.com/Totozao/command-line-chess-RU-
```
- перейдите в только что созданный каталог `command-line-chess-RU-` и запустите его:
```
pip install .
```
## Использование

```sh
chess -h        # to see all possible options
```
```
usage: chess [-h] [-t] [-w W] [-b B] [-c]

Программа на языке python для игры в шахматы с искусственным интеллектом в терминале.

необязательные аргументы:
  -h, --help вывести справочное сообщение и выйти из игры
  -t, --two играть в игру для двух игроков (по умолчанию: False)
  -w W, --white W цвет для белого игрока (по умолчанию: белый)
  -b B, --black B цвет для черного игрока (по умолчанию: черный)
  -c, --checkered использовать клетчатую тему для шахматной доски (по умолчанию: False)

Приятной игры!

```

## Участие

Вклады всегда приветствуются!

О том, как начать работу, см. в разделе `CONTRIBUTING.md`.

Пожалуйста, соблюдайте `CODE-OF-CONDUCT.md` этого проекта.


## Лицензия
Take a look at the [LICENSE](https://github.com/marcusbuffett/command-line-chess/LICENSE) file

## Авторы

- [@marcusbuffett](https://www.github.com/marcusbuffett)
- [@ClasherKasten](https://www.github.com/ClasherKasten)


## Вопросы, ошибки и т.д.
Пожалуйста, создайте вопрос.

## Технические вопросы

ИИ представляет собой простой грубый ИИ без обрезки. Он оценивает заданную позицию, подсчитывая стоимость фигур для каждой стороны (пешка -> 1, конь/слон -> 3, ладья -> 5, ферзь -> 9). Он оценивает дерево ходов и выбирает тот путь, который дает наибольший выигрыш. Более подробную информацию можно найти в [моем посте о том, как это работает] (https://mbuffett.com/posts/chess-ai/).

## Примечание

Данный репозиторий создан исключительно в юмористических целях и приследует только желание перевести интерфейс шахмат в терминале на русском, все ссылки сохранены, за исключением инструкции по установке и клонированию оригинального материала
