"""
Level 9: Robot Room Cleaner

Problem:
Design an algorithm to clean the entire room using a robot API.
The robot has 4 API methods: move(), turnLeft(), turnRight(), clean().
Backtrack to clean all accessible cells and return to starting position.

Time Complexity: O(N - M) where N is number of cells and M is obstacles
Space Complexity: O(N - M) visited set and recursion stack
"""

class MockRobot:
    def __init__(self, room, start_r, start_c):
        self.room = room
        self.r = start_r
        self.c = start_c
        self.dir = 0  # 0: Up, 1: Right, 2: Down, 3: Left
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.cleaned = set()

    def move(self) -> bool:
        dr, dc = self.dirs[self.dir]
        nr, nc = self.r + dr, self.c + dc
        if 0 <= nr < len(self.room) and 0 <= nc < len(self.room[0]) and self.room[nr][nc] == 1:
            self.r, self.c = nr, nc
            return True
        return False

    def turnLeft(self):
        self.dir = (self.dir - 1) % 4

    def turnRight(self):
        self.dir = (self.dir + 1) % 4

    def clean(self):
        self.cleaned.add((self.r, self.c))


def clean_room(robot: MockRobot) -> None:
    visited = set()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left

    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(r, c, d):
        visited.add((r, c))
        robot.clean()

        for i in range(4):
            new_d = (d + i) % 4
            dr, dc = dirs[new_d]
            nr, nc = r + dr, c + dc

            if (nr, nc) not in visited and robot.move():
                backtrack(nr, nc, new_d)
                go_back()

            robot.turnRight()

    backtrack(0, 0, 0)


if __name__ == "__main__":
    room = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    robot = MockRobot(room, 0, 0)
    clean_room(robot)
    assert len(robot.cleaned) == 10  # 10 accessible cells
    print("[PASS] Level 9 Robot Room Cleaner tests passed!")
