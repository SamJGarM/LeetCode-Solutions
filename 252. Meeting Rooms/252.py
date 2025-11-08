"""
Author: Samuel Jaden García Muñoz
Date: 25/10/2025
Revised: 08/11/2025
Note:-

"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort the list by starting values.
        intervals.sort(key = lambda i : i.start)

        # Iterate through every object in the list (except the last)
        for i in range(len(intervals) - 1):
            # If the ending of the first meeting ends after the proposed start time of the following meeting, the schedule is impossible.
            if intervals[i].end > intervals[i+1].start:
                # Return False
                return False

        # If after passing through all meetings we haven't returned False we know we have a possible meeting schedule.
        return True

"""
Time Complexity: O(n logn)
Space Complexity: O(1)
"""