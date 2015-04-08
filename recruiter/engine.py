class NewCandidateEngine(object):

	def __init__(self):
		self.open_positions = []

	def getJobPositions(self, candidate):
		if (candidate.html >= 7) and (candidate.css >= 7) and (candidate.javascript >= 7):
			self.open_positions.append('front_end')
		if (candidate.python >= 7) and (candidate.django >= 7):
			self.open_positions.append('back_end')
		if (candidate.ios >= 7) and (candidate.android >= 7):
			self.open_positions.append('mobile')
		return self.open_positions
