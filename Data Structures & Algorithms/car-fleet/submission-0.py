class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append([position[i], speed[i], ((target - position[i])/speed[i])])

        cars.sort(reverse=True)
        for trip in cars:
            time = trip[2]
            if stack and (stack[-1] >= time):
                continue
            stack.append(time)
        
        return len(stack)