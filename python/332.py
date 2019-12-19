from collections import defaultdict
class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        connections = defaultdict(list)
        for ticket in tickets:
            connections[ticket[0]].append(ticket[1])
        print(connections)
        for key in connections.keys():
            connections[key] = sorted(connections[key], reverse=True)

        stack, result = [], []
        stack.append("JFK")

        while stack:
            top_element = stack[-1]
            if top_element in connections and len(connections.get(top_element, [])) > 0:
                stack.append(connections[top_element].pop())
            else:
                result.append(stack.pop())
        return result[::-1]
