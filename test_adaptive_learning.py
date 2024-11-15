from adaptive_learning import StudentProfile, CourseGraph, PriorityContentQueue


class TestAdaptiveLearningPlatform:
    def __init__(self):
        self.student_profile = StudentProfile(student_id=1)
        self.course_graph = CourseGraph()
        self.priority_content_queue = PriorityContentQueue()

    def test_student_profile(self):
        print("Running StudentProfile Tests...")

        self.student_profile.add_score("Statistics", 85)
        self.student_profile.add_score("Calculus", 70)
        
        assert self.student_profile.get_all_scores() == {"Statistics": 85, "Calculus": 70}, "Test Failed: get_all_scores()"
        

        #positive test case
        assert self.student_profile.get_score("Statistics") == 85, "Test Failed: get_score() for Statistics"
        #negative test case
        assert self.student_profile.get_score("Algebra") == "No score available for this topic", "Test Failed: get_score() for Calculus"
        

        self.student_profile.update_preference("learning_style", "visual")
        assert self.student_profile.preferences["learning_style"] == "visual", "Test Failed: update_preference()"
        print("StudentProfile Tests Passed!\n")

    def test_course_graph(self):
        print("Running CourseGraph Tests...")

        self.course_graph.add_topic("Calculus")
        self.course_graph.add_prerequisite("Calculus", "Algebra")
        self.course_graph.add_prerequisite("Physics", "Mathematics")
        
        
        assert self.course_graph.get_prerequisites("Calculus") == ["Algebra"], "Test Failed: get_prerequisites() for Calculus"
        assert self.course_graph.get_prerequisites("Physics") == ["Mathematics"], "Test Failed: get_prerequisites() for Physics"
        
        expected_graph = {
            "Calculus": ["Algebra"],
            "Physics": ["Mathematics"],
            "Algebra": [],
            "Mathematics": []
        }
        assert self.course_graph.get_all_topics() == expected_graph, "Test Failed: get_all_topics()"
        print("CourseGraph Tests Passed!\n")

    def test_priority_content_queue(self):
        print("Running PriorityContentQueue Tests...")

        self.priority_content_queue.add_content(2, "Quiz on Algebra")
        self.priority_content_queue.add_content(1, "Introductory Video on Calculus")
        self.priority_content_queue.add_content(3, "Assignment on Geometry")
            
        assert self.priority_content_queue.get_top_content() == "Introductory Video on Calculus", "Test Failed: get_top_content() first retrieval"
        assert self.priority_content_queue.get_top_content() == "Quiz on Algebra", "Test Failed: get_top_content() second retrieval"
        
        assert self.priority_content_queue.view_all_content() == ["Assignment on Geometry"], "Test Failed: view_all_content()"
        print("PriorityContentQueue Tests Passed!\n")

    def run_all_tests(self):
        self.test_student_profile()
        self.test_course_graph()
        self.test_priority_content_queue()
        print("All Tests Completed!")


if __name__ == "__main__":
    test_suite = TestAdaptiveLearningPlatform()
    test_suite.run_all_tests()