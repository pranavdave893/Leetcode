class Solution(object):
    def cleanRoom(self, robot, move = [(-1, 0), (0, -1), (1, 0), (0, 1)]):
        def dfs(i, j, cleaned, ind):
            robot.clean()
            cleaned.add((i, j))
            for k in range(4):
                x, y = move[(ind + k) % 4]
                if (i + x, j + y) not in cleaned and robot.move():
                    dfs(i + x, j + y, cleaned, (ind + k) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnLeft()
        dfs(0, 0, set(), 0)

abc = Solution()    