import unittest
from app.models import Pitch  
Pitch = Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(133,'killed by excellence')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))