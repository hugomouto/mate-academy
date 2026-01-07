import random
from typing import Generator


def dice_player(n_rounds: int) -> Generator[int, None, None]:
    for i in range(n_rounds):
        yield random.randint(1, 6)


def dice_game(n_rounds: int) -> str:
    player1 = dice_player(n_rounds)
    player2 = dice_player(n_rounds)
    final_score_list = []
    for r in range(n_rounds):
        next_p1 = next(player1)
        next_p2 = next(player2)
        print(f"{next_p1} {next_p2}")
        if next_p1 > next_p2:
            final_score_list.append("p1")
        elif next_p1 < next_p2:
            final_score_list.append("p2")
        else:
            final_score_list.append("draw")
    if final_score_list.count("p1") > final_score_list.count("p2"):
        return "First"
    elif final_score_list.count("p1") < final_score_list.count("p2"):
        return "Second"
    else:
        return "Draw"
