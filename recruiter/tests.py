from django.test import TestCase
from .engine import NewCandidateEngine
from .models import Candidate

# Create your tests here.
class NewCandidateEngineTest(TestCase):

	def test_new_candidate_engine_no_job(self):
		candidate = Candidate(name="Jon Doe", email="jon.doe@email.com", 
			html=0, 
			css=0, 
			javascript=0, 
			python=0, 
			django=0, 
			ios=0, 
			android=0
		)
		new_candidate_engine = NewCandidateEngine()
		possible_positions = new_candidate_engine.getJobPositions(candidate)
		self.assertTrue(len(possible_positions) == 0)

	def test_new_candidate_engine_front_end_job(self):
		candidate = Candidate(name="Jon Doe", email="jon.doe@email.com", 
			html=7, 
			css=7, 
			javascript=7, 
			python=0, 
			django=0, 
			ios=0, 
			android=0
		)
		new_candidate_engine = NewCandidateEngine()
		possible_positions = new_candidate_engine.getJobPositions(candidate)
		self.assertTrue(len(possible_positions) > 0)

