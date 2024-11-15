from collections import defaultdict
import heapq


class StudentProfile:
    def __init__(self, student_id):
        self.student_id = student_id
        self.scores = {}        # Dictionary to store scores for each topic
        self.preferences = {}    # Dictionary to store preferences

    def add_score(self, topic, score):
        self.scores[topic] = score

    def update_preference(self, key, value):
        self.preferences[key] = value

    def get_score(self, topic):
        return self.scores.get(topic, "No score available for this topic")

    def get_all_scores(self):
        return self.scores



class CourseGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_topic(self, topic):
        if topic not in self.graph:
            self.graph[topic] = []

    def add_prerequisite(self, topic, prerequisite):
        if prerequisite not in self.graph:
            self.add_topic(prerequisite)
        if topic not in self.graph:
            self.add_topic(topic)
        self.graph[topic].append(prerequisite)

    def get_prerequisites(self, topic):
        return self.graph.get(topic, "Topic not found")

    def get_all_topics(self):
        return dict(self.graph)



class PriorityContentQueue:
    def __init__(self):
        self.queue = []

    def add_content(self, priority, content):
        heapq.heappush(self.queue, (priority, content))

    def get_top_content(self):
        if not self.queue:
            return "Queue is empty"
        return heapq.heappop(self.queue)[1]

    def view_all_content(self):
        return [item[1] for item in sorted(self.queue)]
