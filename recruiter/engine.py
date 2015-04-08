class NewCandidateEngine(object):

	def __init__(self):
		self.open_positions = []

	def getJobPositions(self, candidate):
		if self.is_front_end_developer(candidate):
			self.open_positions.append('front_end')
		if self.is_back_end_developer(candidate):
			self.open_positions.append('back_end')
		if self.is_mobile_developer(candidate):
			self.open_positions.append('mobile')
		return self.open_positions

	def is_front_end_developer(self, candidate):
		return (candidate.html >= 7) and (candidate.css >= 7) and (candidate.javascript >= 7)

	def is_back_end_developer(self, candidate):
		return (candidate.python >= 7) and (candidate.django >= 7)

	def is_mobile_developer(self, candidate):
		return (candidate.ios >= 7) and (candidate.android >= 7)
