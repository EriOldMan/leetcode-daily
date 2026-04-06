from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        current_point = [0, 0]
        furthest_point = [0, 0]
        direction_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        obstacle_set = {(x, y ) for x, y in obstacles}

        for command in commands:
            if command == -1:
                current_direction = (current_direction + 1) % 4       
            elif command == -2:
                current_direction = (current_direction - 1) % 4
            else:
                for _ in range(command):
                    next_point = (current_point[0] + direction_map[current_direction][0], current_point[1] + direction_map[current_direction][1])
                    if next_point in obstacle_set:
                        break
                    else:
                        current_point[0] = next_point[0]
                        current_point[1] = next_point[1]
                        if current_point[0] * current_point[0] + current_point[1] * current_point[1] > furthest_point[0] * furthest_point[0] + furthest_point[1] * furthest_point[1]:
                            furthest_point = current_point[:]

        return furthest_point[0] * furthest_point[0] + furthest_point[1] * furthest_point[1]
