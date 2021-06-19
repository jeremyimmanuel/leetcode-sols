from enum import Enum


class Instructions(Enum):
    G = 'G'
    L = 'L'
    R = 'R'


def isRobotBounded(instructions: str) -> bool:
    direction = (0, 1)
    pos = (0, 0)
    for _ in range(4):
        for ch in instructions:
            if ch is 'G':
                pos = tuple(map(sum, zip(pos, direction)))
            elif ch is 'L':
                direction = (-direction[1], direction[0])
            elif ch is 'R':
                direction = (direction[1], -direction[0])
    return pos == (0,0)
