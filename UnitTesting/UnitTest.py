import unittest # Test Module 

def add(a,b): # defining the function to test
    return a + b

class TestCalc(unittest.TestCase): # Defines the unit test
    def test_add(self):
        a = 12
        b = 13
        result = add(a,b)
        self.assertEqual(result,25) # asserting that the add function works 
        
if __name__ == "__main__":
    unittest.main()