from io import TextIOWrapper
from yaml import safe_load as load_yaml

from quiz.question import Question

class Quiz:
	def __init__(self, file: TextIOWrapper  = None) -> None:
		self.file = file
		self.yaml = load_yaml(file.read())
		self.name = self.yaml['name']
		self.questions = []
		for question in self.yaml['questions']:
			question = Question(question)
			self.questions.append(question)