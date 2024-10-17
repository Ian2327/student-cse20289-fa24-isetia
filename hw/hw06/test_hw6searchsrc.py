import unittest

from hw6searchsrc import *

class TestHW6SearchSrc(unittest.TestCase):
    def test_countLines(self):
        self.assertEqual(countLines("./tests/data/fmnc_manager.cc"), 2310)
        self.assertEqual(countLines("./tests/data/ParamDictionary.cc"), 379)
        self.assertEqual(countLines("./tests/data/PktQueue.cc"), 42)
        self.assertEqual(countLines("./tests/data/RIPPS_PktPair.cc"), 607)
        self.assertEqual(countLines("./tests/data/Thread_IO.cc"), 149)
    def test_countInclude(self):
        self.assertEqual(countInclude("./tests/data/fmnc_manager.cc"), 18)
        self.assertEqual(countInclude("./tests/data/ParamDictionary.cc"), 3)
        self.assertEqual(countInclude("./tests/data/PktQueue.cc"), 1)
        self.assertEqual(countInclude("./tests/data/RIPPS_PktPair.cc"), 5)
        self.assertEqual(countInclude("./tests/data/Thread_IO.cc"), 7)
    def test_countIncludeLocal(self):
        self.assertEqual(countIncludeLocal("./tests/data/fmnc_manager.cc"), 11)
        self.assertEqual(countIncludeLocal("./tests/data/ParamDictionary.cc"), 1)
        self.assertEqual(countIncludeLocal("./tests/data/PktQueue.cc"), 1)
        self.assertEqual(countIncludeLocal("./tests/data/RIPPS_PktPair.cc"), 3)
        self.assertEqual(countIncludeLocal("./tests/data/Thread_IO.cc"), 5)
    def test_countMemberFuncs(self):
        self.assertEqual(countMemberFuncs("./tests/data/fmnc_manager.cc"), 77)
        self.assertEqual(countMemberFuncs("./tests/data/ParamDictionary.cc"), 26)
        self.assertEqual(countMemberFuncs("./tests/data/PktQueue.cc"), 4)
        self.assertEqual(countMemberFuncs("./tests/data/RIPPS_PktPair.cc"), 50)
        self.assertEqual(countMemberFuncs("./tests/data/Thread_IO.cc"), 0)
    def test_countOneLineFuncs(self):
        self.assertEqual(countOneLineFuncs("./tests/data/fmnc_manager.cc"), 36)
        self.assertEqual(countOneLineFuncs("./tests/data/ParamDictionary.cc"), 10)
        self.assertEqual(countOneLineFuncs("./tests/data/PktQueue.cc"), 4)
        self.assertEqual(countOneLineFuncs("./tests/data/RIPPS_PktPair.cc"), 23)
        self.assertEqual(countOneLineFuncs("./tests/data/Thread_IO.cc"), 0)
    def test_extract_filename_filepath(self):
        self.assertEqual(extract_filename_filepath("./tests/data/fmnc_manager.cc"), ("./tests/data/", "fmnc_manager.cc"))
        self.assertEqual(extract_filename_filepath("./tests/data/ParamDictionary.cc"), ("./tests/data/", "ParamDictionary.cc"))
        self.assertEqual(extract_filename_filepath("./tests/data/PktQueue.cc"), ("./tests/data/", "PktQueue.cc"))
        self.assertEqual(extract_filename_filepath("./tests/data/RIPPS_PktPair.cc"), ("./tests/data/", "RIPPS_PktPair.cc"))
        self.assertEqual(extract_filename_filepath("./tests/data/Thread_IO.cc"), ("./tests/data/", "Thread_IO.cc"))
        #Random other files to test the function 
        self.assertEqual(extract_filename_filepath("./../../../somedir/subdir/note.jpeg"), ("./../../../somedir/subdir/", "note.jpeg"))
        self.assertEqual(extract_filename_filepath("/home/user/documents/project/file.txt"), ("/home/user/documents/project/", "file.txt"))

