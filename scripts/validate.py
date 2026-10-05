"""Validate a workshop pull request with only the Python standard library."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys
from html.parser import HTMLParser


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDERS = {
    "title": "CHANGE_ME_TITLE",
    "heading": "CHANGE_ME_HEADING",
    "message": "CHANGE_ME_MESSAGE",
}
HEADINGS = ("変更したこと", "表示確認", "スクリーンショット")
IMAGE_RE = re.compile(r"!\[[^\]\n]*\]\(\s*https://[^)\s]+\s*\)", re.IGNORECASE)


class WorkshopHTMLParser(HTMLParser):
    """Extract the three fields that learners are asked to change."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: dict[str, list[str]] = {key: [] for key in PLACEHOLDERS}
        self.counts: dict[str, int] = {key: 0 for key in PLACEHOLDERS}
        self.current: str | None = None
        self.depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.current is not None:
            self.depth += 1
            return
        attributes = dict(attrs)
        key = None
        if tag == "title":
            key = "title"
        elif tag == "h1" and attributes.get("id") == "workshop-heading":
            key = "heading"
        elif tag == "p" and attributes.get("id") == "workshop-message":
            key = "message"
        if key is not None:
            self.counts[key] += 1
            self.current = key
            self.depth = 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # A self-closing element does not enclose workshop text.
        pass

    def handle_data(self, data: str) -> None:
        if self.current is not None:
            self.values[self.current].append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.current is not None:
            self.depth -= 1
            if self.depth == 0:
                self.current = None


def validate_html(source: str) -> list[str]:
    errors: list[str] = []
    parser = WorkshopHTMLParser()
    parser.feed(source)
    parser.close()

    labels = {"title": "<title>", "heading": "見出し <h1>", "message": "本文 <p>"}
    for key, placeholder in PLACEHOLDERS.items():
        if parser.counts[key] != 1:
            errors.append(f"{labels[key]} が見つからないか、複数あります。元のタグと id を残してください。")
            continue
        value = "".join(parser.values[key]).strip()
        if placeholder in value or not value:
            errors.append(f"{labels[key]} の {placeholder} を自分の言葉に置き換えてください。")
        elif key == "message" and len(value) < 10:
            errors.append("本文 <p> は10文字以上のメッセージにしてください。")

    if "CHANGE_ME_" in source and not any("CHANGE_ME_" in error for error in errors):
        errors.append("index.html に CHANGE_ME_ の目印が残っています。すべて置き換えてください。")
    return errors


def section(body: str, name: str) -> str | None:
    headings = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", body))
    for index, match in enumerate(headings):
        if match.group(1).strip() == name:
            end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
            return re.sub(r"<!--.*?-->", "", body[match.end() : end], flags=re.DOTALL).strip()
    return None


def validate_pr_body(body: str) -> list[str]:
    errors: list[str] = []
    for name in HEADINGS:
        if section(body, name) is None:
            errors.append(f"PR 本文に『## {name}』の欄を残してください。")
    change = section(body, "変更したこと")
    if change is not None and not change:
        errors.append("PR 本文の『変更したこと』に、編集内容を一文で書いてください。")
    checked = section(body, "表示確認")
    if checked is not None and not re.search(r"(?m)^\s*-\s*\[[xX]\]", checked):
        errors.append("PR 本文の『表示確認』にチェックを入れてください。")
    screenshot = section(body, "スクリーンショット")
    if screenshot is not None and not IMAGE_RE.search(screenshot):
        errors.append("PR 本文の『スクリーンショット』に画像をドラッグ＆ドロップしてください。")
    return errors


def changed_files(base_sha: str, head_sha: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_sha}...{head_sha}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def emit_error(message: str, file: str | None = None) -> None:
    location = f" file={file}," if file else " "
    print(f"::error{location}title=ハンズオンの確認::{message}")
    print(f"NG: {message}")


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("GITHUB_EVENT_PATH がありません。PR の GitHub Actions で実行してください。", file=sys.stderr)
        return 2
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    pull_request = event.get("pull_request")
    if not pull_request:
        print("PR のイベント情報がありません。", file=sys.stderr)
        return 2

    errors: list[tuple[str | None, str]] = []
    files = changed_files(pull_request["base"]["sha"], pull_request["head"]["sha"])
    if files != ["index.html"]:
        errors.append((None, f"変更するファイルは index.html だけにしてください。現在の変更: {', '.join(files) or 'なし'}"))
    index_path = ROOT / "index.html"
    if index_path.exists():
        errors.extend(("index.html", message) for message in validate_html(index_path.read_text(encoding="utf-8")))
    else:
        errors.append(("index.html", "index.html がありません。削除せずに編集してください。"))
    errors.extend((None, message) for message in validate_pr_body(pull_request.get("body") or ""))

    if errors:
        for file, message in errors:
            emit_error(message, file)
        return 1
    print("OK: HTML の編集、PR 本文、スクリーンショットの添付を確認しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
