class JobPositionSender(object):

	def __init__(self, job_positions):
		self.job_positions = job_positions

	def send(self):
		if len(self.job_positions) > 0:
			if "front_end" in self.job_positions:
				print("FRONT_END EMAIL")
			if "back_end" in self.job_positions:
				print("BACK_END EMAIL")
			if "mobile" in self.job_positions:
				print("MOBILE EMAIL")
		else:
			self.send_generic_email()

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

	def create(self, candidate):
		candidate.save()
		job_positions = self.getJobPositions(candidate)
		sender = JobPositionSender(job_positions)
		sender.send()
		return candidate
