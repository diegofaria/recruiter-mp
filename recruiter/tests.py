from django.test import TestCase
from .engine import NewCandidateEngine
from .models import Candidate

# Create your tests here.
class NewCandidateEngineTest(TestCase):

	def setUp(self):
		self.candidate = Candidate(name="Jon Doe", email="jon.doe@email.com", 
			html=0, 
			css=0, 
			javascript=0, 
			python=0, 
			django=0, 
			ios=0, 
			android=0
		)
		self.new_candidate_engine = NewCandidateEngine()

	def test_new_candidate_engine_no_job(self):
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) == 0)

	def test_new_candidate_engine_front_end_job(self):
		self.candidate.html = 7
		self.candidate.css = 7
		self.candidate.javascript = 7
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) > 0)

	def test_new_candidate_engine_back_end_job(self):
		self.candidate.python = 7
		self.candidate.django = 7
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) > 0)
