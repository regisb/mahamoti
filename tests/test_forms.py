import unittest

import mahamoti.forms

class FormTest(unittest.TestCase):

    def test_classes(self):
        self.assertIn(mahamoti.forms.RunningForm,
                      mahamoti.forms.classes())
        self.assertIn(mahamoti.forms.TrumpetPlayingForm,
                      mahamoti.forms.classes())
