"""This module tests function reverse_words
provided by module mod.py."""
import unittest
import mod

class ModTest(unittest.TestCase):

    def testNormalCaseWorks(self):
        self.assertEqual(
            'years seven and score four',
            mod.reverse_words('four score and seven years'))

    def testSingleWordIsNoop(self):
        self.assertEqual(
            'justoneword',
            mod.reverse_words('justoneword'))
            
    def testEmptyWorks(self):
        self.assertEqual('', mod.reverse_words(''))

    def testRedundantSpacingGetsRemoved(self):
        self.assertEqual(
            'spacing redundant with',
            mod.reverse_words('with   redundant   spacing'))
            
    def testUnicodeWorks(self):
        self.assertEqual('too right all is 𝒰𝓷𝓲𝓬𝓸𝓭𝓮',
            mod.reverse_words('𝒰𝓷𝓲𝓬𝓸𝓭𝓮 is all right too'))
            
    def testExactlyOneArgumentIsEnforced(self):
        with self.assertRaises(TypeError):
            mod.reverse_words('one', 'another')

    def testArgumentMustBeString(self):
        with self.assertRaises((AttributeError, TypeError)):
            mod.reverse_words(1)

if __name__=='__main__':
    unittest.main()