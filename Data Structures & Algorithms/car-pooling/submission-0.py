class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for pas, s, e in trips:
            events.append((s, pas))
            events.append((e, -pas))

        events.sort(key = lambda events: events[0])
        totalPas = 0
        for pos, pas in events:
            totalPas +=pas
            if totalPas>capacity:
                return False

        return True