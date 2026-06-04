import abc
import os
import unittest
import tempfile



class StudyTestCase(unittest.TestCase, abc.ABC):

    @abc.abstractmethod
    def create_study(self, *args, **kwargs):
        pass

    def test_study_creation(self):
        study = self.create_study()
        self.assertIsNotNone(study)

    def test_study_save_and_load(self):
        study = self.create_study()
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file_path = tmp_file.name
        try:
            study.save(tmp_file_path)
            loaded_study = self.create_study()
            loaded_study.load(tmp_file_path)
            self.assertEqual(study, loaded_study)
        finally:
            os.remove(tmp_file_path)