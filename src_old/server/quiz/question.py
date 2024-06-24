class Question:
	def __init__(self, question: dict = {}) -> None:
		self.title = question['title']
		self.type = question['type']
		self.correct = question['correct']
		if self.type != 'BOOL':
			self.answers = question['answers']