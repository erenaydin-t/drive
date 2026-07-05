import unittest

from drive.api.list import resolve_sort_field


class TestResolveSortField(unittest.TestCase):
    def test_frontend_tokens_map_to_real_columns(self):
        # The tokens DriveToolBar.vue actually sends for each sort option.
        self.assertEqual(resolve_sort_field("title"), "file_name")  # Name
        self.assertEqual(resolve_sort_field("mime_type"), "mime_type")  # Type
        self.assertEqual(resolve_sort_field("file_size"), "file_size")  # Size
        self.assertEqual(resolve_sort_field("owner"), "owner")
        self.assertEqual(resolve_sort_field("modified"), "modified")

    def test_unknown_key_defaults_to_modified(self):
        # Guards issue #643: an unknown or hostile key must never reach the query.
        self.assertEqual(resolve_sort_field("name; DROP TABLE tabFile"), "modified")
        self.assertEqual(resolve_sort_field("last_interaction"), "modified")
        self.assertEqual(resolve_sort_field(""), "modified")
