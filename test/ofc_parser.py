#coding: utf-8
import sys
sys.path.insert(0, '../3rdparty')
sys.path.insert(0, '../lib')

from ofxtools.ofc_parser import OfcParser
from os.path import join, realpath, dirname
from pyparsing import ParseException

import unittest

FIXTURES_PATH = join(realpath(dirname(__file__)), 'fixtures')
bad_ofc_path = join(FIXTURES_PATH, 'bad.ofc')
no_bankinfo_ofc_path = join(FIXTURES_PATH, 'nobankinfo_and_trnrs.ofc')

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

    def test_parsing_ofc_without_bank_info_not_raise_Exception(self):
        self.ofc = open(no_bankinfo_ofc_path, 'r').read()
        assert_not_raises(self.parser.parse, self.ofc, Exception)


if __name__ == '__main__':
    unittest.main()
