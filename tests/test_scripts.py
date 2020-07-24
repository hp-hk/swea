import sys
import unittest
from swea.scripts import main

class ScriptTests(unittest.TestCase):
    def test_parse_args(self):
        stream = os.popen('swea')
        output = stream.read()
        print(output)
        self.assertEqaul(output, 'happy hacking')

if __name__ == '__main__':
    unittest.main()