from __future__ import annotations

import argparse
import random
import sys

from src.AI import AI
from src.Board import Board
from src.InputParser import InputParser
from src.Move import Move
from src.Piece import Piece

WHITE = True
BLACK = False


def askForPlayerSide() -> bool:
    playerChoiceInput = input(
        'За какую сторону Вы хотели бы играть [wB]? ',
    ).lower()
    if 'w' in playerChoiceInput:
        print('Вы будете играть за белых')
        return WHITE
    else:
        print('Вы будете играть за черных')
        return BLACK


def askForDepthOfAI() -> int:
    depthInput = 2
    try:
        depthInput = int(
            input(
                'Насколько глубокий поиск ходов должен осуществлять ИИ?\n'
                'Предупреждение: при значениях выше 3 будет работать очень медленно.'
                ' [2]? ',
            ),
        )
        while depthInput <= 0:
            depthInput = int(
                input(
                'Насколько глубокий поиск ходов должен осуществлять ИИ?\n'
                'Предупреждение: при значениях выше 3 будет работать очень медленно.'
                    'Ваши входные данные должны быть больше 0.'
                    ' [2]? ',
                ),
            )

    except KeyboardInterrupt:
        sys.exit()
    except Exception:
        print('Неверный ввод, по умолчанию 2')
    return depthInput


def printCommandOptions() -> None:
    undoOption = 'u : отменить последний шаг'
    printLegalMovesOption = 'l : показать все возможные ходы'
    randomMoveOption = 'r : сделать случайный ход'
    printGameMoves = 'gm: ходы текущей партии в формате PGN'
    quitOption = 'quit : в отставку'
    moveOption = 'a3, Nc3, Qxa2, и т.д. : сделать ход'
    options = [
        undoOption,
        printLegalMovesOption,
        randomMoveOption,
        printGameMoves,
        quitOption,
        moveOption,
        '',
    ]
    print('\n'.join(options))


def printAllLegalMoves(board: Board, parser: InputParser) -> None:
    for move in parser.getLegalMovesWithNotation(
        board.currentSide, short=True,
    ):
        print(move.notation)


def getRandomMove(board: Board, parser: InputParser) -> Move:
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove


def makeMove(move: Move, board: Board) -> None:
    print('Перемещение : ' + move.notation)
    board.makeMove(move)


def undoLastTwoMoves(board: Board) -> None:
    if len(board.history) >= 2:
        board.undoLastMove()
        board.undoLastMove()


def printBoard(board: Board) -> None:
    print()
    print(board)
    print()


def printGameMoves(history: list[tuple[Move, Piece | None]]) -> None:
    counter = 0
    for num, mv in enumerate(history):
        if num % 2 == 0:
            if counter % 6 == 0:
                print()
            print(f'{counter + 1}.', end=' ')
            counter += 1

        print(mv[0].notation, end=' ')
    print()


def startGame(board: Board, playerSide: bool, ai: AI) -> None:
    parser = InputParser(board, playerSide)
    while True:
        if board.isCheckmate():
            if board.currentSide == playerSide:
                print('Шах и мат, вы проиграли')
            else:
                print('Шах и мат! Вы победили!')
            printGameMoves(board.history)
            return

        if board.isStalemate():
            print('Патовая ситуация')
            printGameMoves(board.history)
            return

        if board.noMatingMaterial():
            print('Ничья из-за отсутствия сопрягаемого материала')
            printGameMoves(board.history)
            return

        if board.currentSide == playerSide:
            # printPointAdvantage(board)
            move = None
            command = input("Ваш ход." " Введите '?' для просмотра действий. ? ")
            if command.lower() == 'u':
                undoLastTwoMoves(board)
                printBoard(board)
                continue
            elif command.lower() == '?':
                printCommandOptions()
                continue
            elif command.lower() == 'l':
                printAllLegalMoves(board, parser)
                continue
            elif command.lower() == 'gm':
                printGameMoves(board.history)
            elif command.lower() == 'r':
                move = getRandomMove(board, parser)
            elif command.lower() == 'exit' or command.lower() == 'quit':
                return
            try:
                if move is None:
                    move = parser.parse(command)
            except ValueError as error:
                print('%s' % error)
                continue
            makeMove(move, board)
            printBoard(board)

        else:
            print('ИИ думает...')
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)
            printBoard(board)


def twoPlayerGame(board: Board) -> None:
    parserWhite = InputParser(board, WHITE)
    parserBlack = InputParser(board, BLACK)
    while True:
        printBoard(board)
        if board.isCheckmate():
            print('Шах и мат')
            printGameMoves(board.history)
            return

        if board.isStalemate():
            print('Патовая ситуация')
            printGameMoves(board.history)
            return

        if board.noMatingMaterial():
            print('Ничья из-за отсутствия сопрягаемого материала')
            printGameMoves(board.history)
            return

        # printPointAdvantage(board)
        if board.currentSide == WHITE:
            parser = parserWhite
        else:
            parser = parserBlack
        command = input(
            f"Ваш ход, {board.currentSideRep()}."
            + " Введите '?' для просмотра действий. ? ",
        )
        if command.lower() == 'u':
            undoLastTwoMoves(board)
            continue
        elif command.lower() == '?':
            printCommandOptions()
            continue
        elif command.lower() == 'l':
            printAllLegalMoves(board, parser)
            continue
        elif command.lower() == 'gm':
            printGameMoves(board.history)
        elif command.lower() == 'r':
            move = getRandomMove(board, parser)
        elif command.lower() == 'exit' or command.lower() == 'quit':
            return
        try:
            move = parser.parse(command)
        except ValueError as error:
            print('%s' % error)
            continue
        makeMove(move, board)


board = Board()


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='chess',
        description='Программа для игры в шахматы на языке python '
        'против искусственного интеллекта в терминале.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='Приятной игры!',
    )
    parser.add_argument(
        '-t',
        '--two',
        action='store_true',
        default=False,
        help='для игры на двоих',
    )
    parser.add_argument(
        '-w',
        '--white',
        action='store',
        default='white',
        metavar='W',
        help='цвет для белого игрока ',
    )
    parser.add_argument(
        '-b',
        '--black',
        action='store',
        default='black',
        metavar='B',
        help='цвет для черного игрока ',
    )
    parser.add_argument(
        '-c',
        '--checkered',
        action='store_true',
        default=False,
        help='использовать клетчатую тематику для шахматной доски',
    )

    args = parser.parse_args()
    board.whiteColor = args.white
    board.blackColor = args.black
    board.isCheckered = args.checkered
    try:
        if args.two:
            twoPlayerGame(board)
        else:
            playerSide = askForPlayerSide()
            board.currentSide = WHITE
            print()
            aiDepth = askForDepthOfAI()
            opponentAI = AI(board, not playerSide, aiDepth)
            printBoard(board)
            startGame(board, playerSide, opponentAI)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
