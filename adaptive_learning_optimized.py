import heapq
from collections import defaultdict, deque

class CourseGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degrees = defaultdict(int)
        self.prereq_cache = {} 

    def add_course(self, course, prerequisites):
        for prereq in prerequisites:
            self.graph[prereq].append(course)
            self.in_degrees[course] += 1
        if course not in self.in_degrees:
            self.in_degrees[course] = 0

    def get_prerequisites(self, course):
        if course in self.prereq_cache:
            return self.prereq_cache[course]
        
        result = set()
        queue = deque([course])
        
        while queue:
            current = queue.popleft()
            for prereq in self.graph[current]:
                if prereq not in result:
                    result.add(prereq)
                    queue.append(prereq)
        
        self.prereq_cache[course] = result
        return result

    def resolve_dependencies(self):
        # Topological Sort
        sorted_courses = []
        zero_in_degree = deque([node for node, degree in self.in_degrees.items() if degree == 0])
        
        while zero_in_degree:
            current = zero_in_degree.popleft()
            sorted_courses.append(current)
            for neighbor in self.graph[current]:
                self.in_degrees[neighbor] -= 1
                if self.in_degrees[neighbor] == 0:
                    zero_in_degree.append(neighbor)

        if len(sorted_courses) != len(self.in_degrees):
            raise ValueError("Graph has a cycle.")
        return sorted_courses

class PriorityContentQueue:
    def __init__(self):
        self.heap = []

    def add_content(self, content_id, priority):
        heapq.heappush(self.heap, (-priority, content_id)) 

    def get_highest_priority(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]

    def peek_highest_priority(self):
        if not self.heap:
            return None
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

class StudentProfile:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.preferences = {}
        self.preference_cache = {} 

    def update_preference(self, category, weight):
        self.preferences[category] = weight
        self.preference_cache.pop(category, None) 

    def get_preference(self, category):
        if category in self.preference_cache:
            return self.preference_cache[category]
        
        result = self.preferences.get(category, 0)
        self.preference_cache[category] = result
        return result
