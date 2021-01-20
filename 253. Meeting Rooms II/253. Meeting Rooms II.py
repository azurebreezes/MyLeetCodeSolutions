class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        free_rooms = []
        
        # Sort the meetings in increasing order of their start time
        intervals.sort(key = lambda x: x[0])
        
        # Add the first meeting. 
        heapq.heappush(free_rooms, intervals[0][1])
        
        
        for i in range(1,len(intervals)):
            if intervals[i][0] >= free_rooms[0]:
                # Replace the old meeting with a new one
                heapq.heappushpop(free_rooms, intervals[i][1])
            else:
                # Adding a new meeting
                heapq.heappush(free_rooms, intervals[i][1])
        
        return len(free_rooms)