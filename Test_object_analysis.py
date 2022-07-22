import unittest
import object_analysis
import json

class TestObject_analysis(unittest.TestCase):
    
    
    def test_get_most_common_object(self): # method must start with 'test'

        test_data_single_highest = """
    [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 0
        },
        {
            "type": "star",
            "name": "sirius",
            "redshift": 0
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 0
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 1
        }
    ]
    """

    # the case where highest count returns more than one answer
        test_data_multiple_highest = """
    [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 0
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 0
        },
        {
            "type": "galaxy",
            "name": "pinwheel",
            "redshift": 0
        },
        {
            "type": "supernovae",
            "name": "1987A",
            "redshift": 0
        },
        {
            "type": "frb",
            "name": "fast",
            "redshift": 0
        }
    ]
    """
    
        result_simple_test = object_analysis.get_most_common_object(json.loads(test_data_single_highest))
        result_multiple_highest = object_analysis.get_most_common_object(json.loads(test_data_multiple_highest))
        
        self.assertEqual(result_simple_test,['star'])
        self.assertEqual(result_multiple_highest, ['star', 'galaxy', 'supernovae', 'frb']) 
    
    
    def test_get_furthest_object(self):
        
        test_data_one_redshift = """
    [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 0
        },
        {
            "type": "star",
            "name": "sirius",
            "redshift": 0.1
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 0.2
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 0.3
        }
    ]
    """

        test_data_multiple_redshifts = """
    [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 1
        },
        {
            "type": "star",
            "name": "sirius",
            "redshift": 2.0
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 3
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 3
        }
    ]
    """
    
        result_single_redshift_test = object_analysis.get_furthest_object(json.loads(test_data_one_redshift))
        result_multiple_redshift_test = object_analysis.get_furthest_object(json.loads(test_data_multiple_redshifts))
        
        self.assertEqual(result_single_redshift_test, [{'type': 'galaxy', 'name': 'sombrero', 'redshift': 0.3}])
        self.assertEqual(result_multiple_redshift_test, [{'type': 'nebula', 'name': 'crab', 'redshift': 3},{'type': 'galaxy', 'name': 'sombrero', 'redshift': 3}])
        
        
if __name__ == '__main__':
    unittest.main()
    
