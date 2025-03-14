import unittest
from src.llm_query_correction import correct_query_with_llm

class TestLLMQueryCorrection(unittest.TestCase):
    def test_llm_correction(self):
        query = "plae colplay yelow song"
        corrected_query = correct_query_with_llm(query)
        self.assertIsInstance(corrected_query, str)
        self.assertNotEqual(corrected_query, query)
        self.assertIn("Coldplay", corrected_query)

if __name__ == "__main__":
    unittest.main()
