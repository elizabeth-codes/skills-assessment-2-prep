# Create your classes here
class Student:
    """A student"""
    def __init__(self,first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:
    """a question"""
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def make_questions():
        """returns a list of all questions"""
        all_questions = []
        capital_of_alberta = Question[capital_of_alberta, "What is the capital of Alberta?", "Edmonton"]
        author_of_python = Question[author_of_python, "Who is the author of Python?", "Guido Van Rossum"]

class Exam:
    """an exam"""
    def __init__(self, name, questions):
        self.question = questions
        self.name = name

    def make_exam():
        """creates an exam"""
        all_exams = []
        midterm = Exam[midterm, "Midterm", []]