class Student():
    def __init__(self, first, last, address):
        self.first_name = first
        self.last_name = last
        self.address = address

class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    

    def ask_and_evaluate(self):
        user_input = input(f'{self.question} > ')
        return user_input == self.answer

class Exam():
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.score = 0


    def add_question(self, question):
        self.questions.append(question)

    
    def administer(self):
        number_correct = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                self.score += 1
        return (self.score/len(self.questions))*100

class StudentExam():
    def __init__(self, student, exam):
        self.exam = exam
        self.student = student
        self.score = exam.score

    def take_test(self):
        self.score = self.exam.administer()
        print(self.score)

class Quiz(Exam):
    def administer(self):
        if super().administer() >= 50:
            return 1
        else:
            return 0
      
def example(name, first, last, address):
    exam = Exam(name)
    set_q = Question('What is the method for adding an element to a set?','.add()')
    exam.add_question(set_q)
    pwd_q = Question('What does pwd stand for?', 'print working directory')
    exam.add_question(pwd_q)
    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    exam.add_question(list_q)
    student = Student(first, last, address)
    studentexam = StudentExam(student, exam)
    studentexam.take_test()
        