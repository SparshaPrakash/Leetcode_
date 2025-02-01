class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0] # since we are visiting room 0 at first for sure

        while stack:
            room = stack.pop() # current room visiting
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)
        