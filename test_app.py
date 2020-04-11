import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        self.error_docs = [{"type": "insurance", "number": "10006"}]
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_add_new_shelf(self):
        app.add_new_shelf('4')
        self.assertEqual(len(self.dirs), 4)

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf('123', '3')
        self.assertTrue(self.dirs['3'] == ['123'])

    def test_remove_doc_from_shelf(self):
        dir_len_before = len(self.dirs['1'])
        docs_len_before = len(self.docs)
        app.remove_doc_from_shelf('11-2')
        self.assertLess(len(self.dirs['1']), dir_len_before)
        self.assertEqual(len(self.docs), docs_len_before)

    def test_check_documents_existance(self):
        self.assertTrue(app.check_document_existance('11-2'))

    def test_get_all_doc_owners_names(self):
        self.assertEqual(len(app.get_all_doc_owners_names()), 3)

    def test_get_doc_shelf(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual(app.get_doc_shelf(), '2')