from django.core.mail import send_mail

class JobPositionSender(object):

	def __init__(self, job_positions, email):
		self.job_positions = job_positions
		self.email = email

	def send(self):
		if len(self.job_positions) > 0:
			if "front_end" in self.job_positions:
				self.send_front_end_email()
			if "back_end" in self.job_positions:
				self.send_front_end_email()
			if "mobile" in self.job_positions:
				self.send_mobile_email()
		else:
			self.send_generic_email()


	def send_front_end_email(self, email):
		print("envia email")
#		send_mail('Obrigado por se candidatar', 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato.', 'contato@empresa.com', [self.email], fail_silently=False)

	def send_back_end_email(self):
		print("envia email")
#		send_mail('Obrigado por se candidatar', 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato.', 'contato@empresa.com', [self.email], fail_silently=False)

	def send_mobile_email(self):
		print("envia email")
#		send_mail('Obrigado por se candidatar', 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato.', 'contato@empresa.com', [self.email], fail_silently=False)

	def send_generic_email(self):
		print("envia email")
#		send_mail('Obrigado por se candidatar', 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato.', 'contato@empresa.com', [self.email], fail_silently=False)

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
		sender = JobPositionSender(job_positions, candidate.email)
		sender.send()
		return candidate
