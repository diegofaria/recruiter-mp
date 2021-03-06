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
		self.assertTrue("front_end" in possible_positions)

	def test_new_candidate_engine_back_end_job(self):
		self.candidate.python = 7
		self.candidate.django = 7
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) > 0)
		self.assertTrue("back_end" in possible_positions)

	def test_new_candidate_engine_mobile_job(self):
		self.candidate.ios = 7
		self.candidate.android = 7
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) > 0)
		self.assertTrue("mobile" in possible_positions)

	def test_new_candidate_engine_all_jobs(self):
		self.candidate.html = 7
		self.candidate.css = 7
		self.candidate.javascript = 7
		self.candidate.python = 7
		self.candidate.django = 7
		self.candidate.ios = 7
		self.candidate.android = 7
		possible_positions = self.new_candidate_engine.getJobPositions(self.candidate)
		self.assertTrue(len(possible_positions) == 3)		
		self.assertTrue("mobile" in possible_positions)
		self.assertTrue("back_end" in possible_positions)
		self.assertTrue("front_end" in possible_positions)

	def test_create_candidate_all_jobs(self):
		self.candidate.html = 7
		self.candidate.css = 7
		self.candidate.javascript = 7
		self.candidate.python = 7
		self.candidate.django = 7
		self.candidate.ios = 7
		self.candidate.android = 7
		candidate = self.new_candidate_engine.create(self.candidate)
		self.assertTrue(candidate.pk > 0)

	def test_create_candidate_front_end(self):
		self.candidate.html = 7
		self.candidate.css = 7
		self.candidate.javascript = 7
		candidate = self.new_candidate_engine.create(self.candidate)
		self.assertTrue(candidate.pk > 0)

	def test_create_candidate_front_end(self):
		self.candidate.html = 7
		self.candidate.css = 7
		self.candidate.javascript = 7
		candidate = self.new_candidate_engine.create(self.candidate)
		self.assertTrue(candidate.pk > 0)

	def test_create_candidate_back_end(self):
		self.candidate.python = 7
		self.candidate.django = 7
		candidate = self.new_candidate_engine.create(self.candidate)
		self.assertTrue(candidate.pk > 0)

	def test_create_candidate_mobile(self):
		self.candidate.ios = 7
		self.candidate.android = 7
		candidate = self.new_candidate_engine.create(self.candidate)
		self.assertTrue(candidate.pk > 0)