class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left = [n for n in moves if n == 'L']
        right = [n for n in moves if n == 'R']
        up = [n for n in moves if n == 'U']
        down = [n for n in moves if n == 'D']
        return len(left) == len(right) and len(up) == len(down)