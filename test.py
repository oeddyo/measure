__author__ = 'exie'

import unittest
import measure
import logging

class testMeasure(unittest.TestCase):
    def setUp(self):
        self.m = measure.Measure('prediction', 'label')
        self.log= logging.getLogger( "Debug info: " )

    def test_confusion(self):
        self.log.debug(self.m._confusion_matrix())
        self.assertTrue(self.m._confusion_matrix() == [[5, 3, 0], [2, 3, 1], [0, 2, 11]])

    def test_precision(self):
        self.log.debug(self.m.precision())
        self.assertTrue([5.0/7, 3.0/8, 11.0/12] == self.m.precision())


    def test_recall(self):
        self.log.debug(self.m.recall())
        self.assertTrue([5.0/8, 3.0/6, 11.0/13] == self.m.recall())