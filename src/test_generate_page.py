
import unittest

from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Title\nThis is a test content."
        title, content = extract_title(markdown)
        self.assertEqual(title, "Title")
        self.assertEqual(content, "This is a test content.")
    def test_extract_title_no_heading(self):
        markdown = "This is a test content without a heading."
        with self.assertRaises(ValueError):
            extract_title(markdown)