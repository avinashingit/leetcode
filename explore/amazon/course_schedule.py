from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = defaultdict(int)
        edges = defaultdict(list)

        for req in prerequisites:
            indegrees[req[0]] += 1
            edges[req[1]].append(req[0])

        q = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        total = 0
        while q:
            el = q.popleft()
            total += 1
            for i in edges[el]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    q.append(i)

        return total == numCourses
