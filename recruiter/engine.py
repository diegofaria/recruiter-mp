class NewCandidateEngine(object):

	def __init__(self):
		self.open_positions = []

	def getJobPositions(self, candidate):
		if (candidate.html >= 7) and (candidate.css >= 7) and (candidate.javascript >= 7):
			self.open_positions.append('front_end')
		if (candidate.python >= 7) and (candidate.django >= 7):
			self.open_positions.append('back_end')
		return self.open_positions
