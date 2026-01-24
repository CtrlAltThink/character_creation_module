# Константы тоже нужно проаннотировать
BONUS: float = 1.1
ANTIBONUS: float = 1.1

# Тестовые данные (список кортежей)
# Подсказка: для аннотации списка кортежей в
# Python 3.9+ используй list[tuple[...]]
TEST_DATA = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """Добавляет очки репутации. Если есть buf_effect, умножает на BONUS."""
    # ТВОЙ КОД ТУТ
    current_rep += rep_points  # type float::
    if buf_effect:
        current_rep *= BONUS
    return current_rep  # type float:


def remove_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """Вычитает очки репутации.
       Если есть debuf_effect, умножает на ANTIBONUS."""
    # ТВОЙ КОД ТУТ
    current_rep -= rep_points  # type float:
    if buf_effect:
        current_rep *= ANTIBONUS
    return current_rep  # type float:


def main(duel_res: list[tuple[int, str, bool]]) -> str:
    """
    Проходит циклом по duel_res, вызывает нужные функции
    и возвращает итоговую строку.
    """
    current_rep: float = 0.0
    # ТВОЙ КОД ТУТ (цикл и вызов функций выше)
    for rep, res, effect in duel_res:
        if res == 'success':
            current_rep = add_rep(current_rep, rep, effect)  # type float:
        elif res == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)  # type float:
    return (f'После {len(duel_res)} поединков, репутация персонажа —'
            f'{current_rep:.3f} очков.')


# Тестовый вызов
if __name__ == '__main__':
    print(main(TEST_DATA))
