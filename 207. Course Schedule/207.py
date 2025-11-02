"""
Author: Samuel Jaden García Muñoz
Date: 20/08/2025
Revised: 02/11/2025
Note:-

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Depth-first Search navigation through a given course and all its prerequisites.
        def dfs(course):
            # If a course has been visited already in the current trip, it means a cycle
            # has been detected. Return false.
            if course in visited:
                return False
            # If there are no prerequisites for the current course, return true.
            if not prereqMap[course]:
                return True
            
            # Add the current course to the visited set.
            visited.add(course)
            # Iterate through every prerequisite.
            for prereq in prereqMap[course]:
                # And if any recursive search returns False, we know it's impossible to
                # schedule this course.
                if not dfs(prereq):
                    return False
                
            # Otherwise, remove this course from the cycle, clear it's prerequisites
            # for future checks on other courses, and return True.
            visited.remove(course)
            prereqMap[course] = []
            return True

        # Map for storing all courses and their prerequisites.
        prereqMap = {i:[] for i in range(numCourses)}

        # Iterate through every prerequisite provided and add it to the prerequisite map.
        for (a, b) in prerequisites:
            prereqMap[a].append(b)

        # Set for detecting cycles in prerequisite trees.
        visited = set()

        # Iterate through every course to see whether it is possible to schedule or not.
        # Note: We do this in the case of isolated/separate nodes.
        for i in range(numCourses):
            # If a single course cannot be scheduled, return False.
            if not dfs(i):
                return False
        # Otherwise, return true.
        return True

"""
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""