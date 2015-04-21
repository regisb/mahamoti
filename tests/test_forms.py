import unittest

from mahamoti import forms

class FormTest(unittest.TestCase):

    def test_classes(self):
        self.assertIn(forms.RunningForm,
                      forms.classes())
        self.assertIn(forms.TrumpetPlayingForm,
                      forms.classes())

    def test_fields(self):
        form = forms.RunningForm()
        form_dict = form.to_dict()
        self.assertEqual("Running", form_dict["name"])
        self.assertEqual(None, form_dict["distance"])
        self.assertTrue(isinstance(form_dict["time"], str),
                        "{} is not an instance of str".format(type(form_dict["time"])))
