class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = sorted(zip(position, speed), key=lambda x: -x[0])
        sorted_position, sorted_speed = zip(*sort)

        stack = []
        for i in range(len(sorted_position)):
            car_position = sorted_position[i]
            car_speed = sorted_speed[i]

            # how many iterations will it need to reach the end?
            iterations = (target - car_position) / car_speed
            
            # if it will need more iterations to reach the target than the car in front
            # then it will not catch up and we append it to the stack
            if not stack or iterations > stack[-1]:
                stack.append(iterations)

        # by doing so the length of the stack will represent the number of individual car fleets
        return len(stack)