class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = {}
        if timestamp not in self.timeMap[key]:
            self.timeMap[key][timestamp] = []
        self.timeMap[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        seen = 0

        for time in self.timeMap[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.timeMap[key][seen][-1]
        
