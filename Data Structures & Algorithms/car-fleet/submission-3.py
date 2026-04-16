class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = sorted(zip(position, speed), key=lambda x: -x[0])
        sorted_position, sorted_speed = zip(*sort)

        stack = []
        for i in range(len(sorted_position)):
            car_pos = sorted_position[i]
            car_speed = sorted_speed[i]

            time_to_target = (target - car_pos) / car_speed

            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)