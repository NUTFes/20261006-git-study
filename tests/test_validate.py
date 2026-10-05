import unittest

from scripts.validate import validate_html, validate_pr_body


TEMPLATE = """<!doctype html>
<html lang="ja">
  <head><title>CHANGE_ME_TITLE</title></head>
  <body>
    <h1 id="workshop-heading">CHANGE_ME_HEADING</h1>
    <p id="workshop-message">CHANGE_ME_MESSAGE</p>
  </body>
</html>
"""
VALID_HTML = (
    TEMPLATE.replace("CHANGE_ME_TITLE", "私のページ")
    .replace("CHANGE_ME_HEADING", "こんにちは")
    .replace("CHANGE_ME_MESSAGE", "技大祭の開発を楽しみにしています。")
)
VALID_BODY = """## 変更したこと

ページの見出しと本文を変更しました。

## 表示確認

- [x] 自分のブラウザで index.html を開き、変更を確認した

## スクリーンショット

![表示結果](https://github.com/user-attachments/assets/example)
"""


class ValidateHTMLTests(unittest.TestCase):
    def test_completed_page_passes(self):
        self.assertEqual(validate_html(VALID_HTML), [])

    def test_template_and_short_message_fail(self):
        self.assertGreaterEqual(len(validate_html(TEMPLATE)), 3)
        short = VALID_HTML.replace("技大祭の開発を楽しみにしています。", "短い")
        self.assertTrue(any("10文字以上" in error for error in validate_html(short)))

    def test_removed_heading_fails(self):
        page = VALID_HTML.replace('id="workshop-heading"', 'id="other"')
        self.assertTrue(any("見出し" in error for error in validate_html(page)))


class ValidatePRBodyTests(unittest.TestCase):
    def test_complete_pr_passes(self):
        self.assertEqual(validate_pr_body(VALID_BODY), [])

    def test_missing_screenshot_and_unchecked_box_fail(self):
        body = VALID_BODY.replace("- [x]", "- [ ]").replace("![表示結果](https://github.com/user-attachments/assets/example)", "")
        errors = validate_pr_body(body)
        self.assertTrue(any("チェック" in error for error in errors))
        self.assertTrue(any("スクリーンショット" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
