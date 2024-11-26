import time
import random

from adaptive_learning_optimized import CourseGraph, PriorityContentQueue, StudentProfile

class TestOptimizedClasses:
    def __init__(self):
        self.course_graph = CourseGraph()
        self.priority_queue = PriorityContentQueue()
        self.student_profile = StudentProfile(student_id=1, name="John Doe")

    def test_course_graph(self):
        print("\nRunning CourseGraph Tests...")
        
        # Test basic functionality
        self.course_graph.add_course("Math", ["Algebra"])
        self.course_graph.add_course("Physics", ["Math"])
        self.course_graph.add_course("Computer Science", ["Math", "Physics"])

        try:
            resolved_courses = self.course_graph.resolve_dependencies()
            print("Resolved Order of Courses:", resolved_courses)
        except ValueError as e:
            print("Dependency Resolution Error:", e)

        math_prereqs = self.course_graph.get_prerequisites("Math")
        print("Prerequisites of Math:", math_prereqs)
        assert math_prereqs == {"Computer Science", "Physics"}, "Failed test for Math prerequisites"

    def test_priority_queue(self):
        print("\nRunning PriorityContentQueue Tests...")
        
        self.priority_queue.add_content("Item1", 5)
        self.priority_queue.add_content("Item2", 10)
        self.priority_queue.add_content("Item3", 1)
        
        highest_priority = self.priority_queue.get_highest_priority()
        print("Highest Priority Content:", highest_priority)
        assert highest_priority == "Item2", "Failed test for highest priority content"

        peeked_content = self.priority_queue.peek_highest_priority()
        print("Peek Next Content:", peeked_content)
        assert peeked_content == "Item1", "Failed test for peek functionality"

        self.priority_queue.get_highest_priority()
        self.priority_queue.get_highest_priority()
        self.priority_queue.get_highest_priority()
        assert self.priority_queue.is_empty(), "PriorityQueue should be empty after removals"

    def test_student_profile(self):
        print("\nRunning StudentProfile Tests...")
        
        self.student_profile.update_preference("Math", 4)
        self.student_profile.update_preference("Science", 3)

        math_preference = self.student_profile.get_preference("Math")
        print("Math Preference Weight:", math_preference)
        assert math_preference == 4, "Failed test for Math preference"

        science_preference = self.student_profile.get_preference("Science")
        print("Science Preference Weight:", science_preference)
        assert science_preference == 3, "Failed test for Science preference"

        self.student_profile.update_preference("Math", 5)
        updated_math_preference = self.student_profile.get_preference("Math")
        print("Updated Math Preference Weight:", updated_math_preference)
        assert updated_math_preference == 5, "Failed test for updating Math preference"



    def performance_test_priority_queue(self):
        print("\nRunning Performance Test for PriorityContentQueue...")

        num_items = 10000
        for i in range(num_items):
            priority = random.randint(1, 100)
            content_id = f"Item{random.randint(1, 10000)}"
            self.priority_queue.add_content(content_id, priority)
        
        start_time = time.time()
        while not self.priority_queue.is_empty():
            self.priority_queue.get_highest_priority()
        print(f"Processed {num_items} items in {time.time() - start_time:.4f} seconds")
        

    def run_tests(self):
        self.test_course_graph()
        self.test_priority_queue()
        self.test_student_profile()
        # self.stress_test_course_graph()
        self.performance_test_priority_queue()


# Run tests
if __name__ == "__main__":
    tester = TestOptimizedClasses()
    tester.run_tests()
