"""
Author: Samuel Jaden García Muñoz
Date: 26/08/2025
Note:-
Little bit of modification on the structure for 207.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Conduct a depth-first search through every course
        def dfs(course):
            # If the course has already been visited (forming a cycle), return False.
            if course in visited:
                return False
            # If a course has already been added to the result, return True.
            if course in resSet:
                return True
            
            # Otherwise, add the current course to the cycle.
            visited.add(course)
            # Iterate through every prerequisite of the given course.
            for prereq in prereqMap[course]:
                # If any prerequisite leads to a cycle, we know that this schedule is impossible, so we return False.
                if not dfs(prereq):
                    return False
            # After this, remove it from the visited set.
            visited.remove(course)
            # Add it to the result list and set (set for O(1) lookup time)
            res.append(course)
            resSet.add(course)

            # And since we've navigated this entire section of the course, return True.
            return True

        # Set for storing all items of the result list (res), but conserving time complexity.
        resSet = set()
        # List for result.
        res = []
        # Set for detecting trail of courses visited.
        visited = set()

        # Create the prerequisite map with an empty list for each course.
        prereqMap = {i:[] for i in range(numCourses)}
        # Iterate through the prerequisites list and append all edges to the list in the map.
        for (course, prereq) in prerequisites:
            prereqMap[course].append(prereq)

        # Iterate through every course and call the dfs (for the cases where separate graphs may exist within a schedule)
        for course in range(numCourses):
            # If any search is unsuccessful, we know that the schedule as a whole is inadequate.
            if not dfs(course):
                return []

        # If successful, we return the resulting order of visiting for scheduling the course.
        return res

"""
Time Complexity: O(V + E)
Space Complexity: O(V)
"""