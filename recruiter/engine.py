class NewCandidateEngine(object):

	def getJobPositions(self, candidate):
		if (candidate.html >= 7) and (candidate.css >= 7) and (candidate.javascript >= 7):
			return ['front_end']
		else:
			return []
