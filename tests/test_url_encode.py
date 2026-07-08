import importlib.util
from pathlib import Path
import unittest


class UrlEncodeToolTest(unittest.TestCase):
    def setUp(self):
        tool_path = Path(__file__).resolve().parents[1] / "tools" / "url_encode.py"
        spec = importlib.util.spec_from_file_location("url_encode", tool_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.run = module.run

    def test_encodes_text_for_url_query_values(self):
        self.assertEqual(self.run("hello world&foo"), "hello+world%26foo")
        self.assertEqual(self.run("a/b?c=d"), "a%2Fb%3Fc%3Dd")
        self.assertEqual(self.run("你好 世界"), "%E4%BD%A0%E5%A5%BD+%E4%B8%96%E7%95%8C")


if __name__ == "__main__":
    unittest.main()
