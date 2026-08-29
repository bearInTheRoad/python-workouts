from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.canFinish_dfs(numCourses, prerequisites)

    def findRepeat(self, course, tree, global_visited, local_visited):

        if global_visited[course]:
            return False
        if local_visited[course]:
            return True

        local_visited[course] = True

        for next_course in tree[course]:
            if self.findRepeat(next_course, tree, global_visited, local_visited):
                return True

        local_visited[course] = False
        global_visited[course] = True
        return False

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        tree = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            tree[pre].append(course)

        global_visited = [False] * numCourses
        local_visited = [False] * numCourses
        for course in range(numCourses):
            if self.findRepeat(course, tree, global_visited, local_visited):
                return False
        return True

    def canFinish_khan(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        nextTarget = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            nextTarget[pre].append(course)

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        nodeVisited = 0
        while queue:
            node = queue.popleft()
            nodeVisited += 1

            for nextCourse in nextTarget[node]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return nodeVisited == numCourses
