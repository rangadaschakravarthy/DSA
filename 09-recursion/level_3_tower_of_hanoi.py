"""
Level 3: Tower of Hanoi

Problem:
The Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, C) and N disks.
Move all N disks from source rod A to target rod C using auxiliary rod B such that:
1. Only one disk can be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.

Time Complexity: O(2^N)
Space Complexity: O(N) recursion stack
"""

def solve_tower_of_hanoi(n: int, source: str, target: str, aux: str, moves: list) -> None:
    if n == 1:
        moves.append((source, target))
        return
    solve_tower_of_hanoi(n - 1, source, aux, target, moves)
    moves.append((source, target))
    solve_tower_of_hanoi(n - 1, aux, target, source, moves)


def tower_of_hanoi(n: int) -> list[tuple[str, str]]:
    moves = []
    solve_tower_of_hanoi(n, 'A', 'C', 'B', moves)
    return moves


if __name__ == "__main__":
    moves_3 = tower_of_hanoi(3)
    assert len(moves_3) == 7  # 2^3 - 1 = 7 moves
    assert moves_3[0] == ('A', 'C')
    assert moves_3[-1] == ('A', 'C')
    print("[PASS] Level 3 Tower of Hanoi tests passed!")
