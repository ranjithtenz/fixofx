#coding: utf-8
import sys
sys.path.insert(0, '../3rdparty')
sys.path.insert(0, '../lib')

from ofxtools.ofc_parser import OfcParser
from os.path import join, realpath, dirname
from pyparsing import ParseException

import unittest


bad_ofc_path = join(realpath(dirname(__file__)), 'fixtures', 'bad.ofc')

def assert_not_raises(function, param, exception):
    try:
      function(param)
    except exception:
      raise AssertionError, "Exception %s raised" %exception


class OFCParserTestCase(unittest.TestCase):
    def setUp(self):
        self.ofc = open(bad_ofc_path, 'r').read()
        self.parser = OfcParser()

    def test_parsing_bad_ofc_should_not_raise_exception(self):
        assert_not_raises(self.parser.parse, self.ofc, ParseException)

if __name__ == '__main__':
    unittest.main()
