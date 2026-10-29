from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.project_cards = []
        self.media_links = []
        self.github_profile_links = []
        self._card = None
        self._heading = False
        self._link = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "article" and "project-card" in classes:
            self._card = {"title": "", "text": ""}
            self.project_cards.append(self._card)
        if tag == "h3" and self._card:
            self._heading = True
        if tag == "a":
            href = attrs.get("href", "")
            if "project-media" in classes:
                self._link = {"attrs": attrs, "image_alts": []}
                self.media_links.append(self._link)
            if href.startswith("https://github.com/"):
                self.github_profile_links.append(href)
        if tag == "img" and self._link is not None:
            self._link["image_alts"].append(attrs.get("alt", ""))

    def handle_endtag(self, tag):
        if tag == "h3":
            self._heading = False
        if tag == "a":
            self._link = None
        if tag == "article":
            self._card = None

    def handle_data(self, data):
        if self._card is not None:
            self._card["text"] += data
            if self._heading:
                self._card["title"] += data


class PortfolioAccessibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = PortfolioParser()
        parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
        cls.parser = parser

    def test_flowops_is_the_lead_project_with_simulated_demo_boundary(self):
        first = self.parser.project_cards[0]
        self.assertEqual(first["title"].strip(), "FlowOps")
        self.assertIn("synthetic", first["text"].lower())
        self.assertIn("not exercised", first["text"].lower())

    def test_project_media_links_are_keyboard_and_screen_reader_accessible(self):
        self.assertTrue(self.parser.media_links)
        for link in self.parser.media_links:
            attrs = link["attrs"]
            self.assertNotIn("aria-hidden", attrs)
            self.assertNotEqual(attrs.get("tabindex"), "-1")
            accessible_name = attrs.get("aria-label", "").strip()
            self.assertTrue(
                accessible_name or any(alt.strip() for alt in link["image_alts"]),
                f"Project image link needs an accessible name: {attrs.get('href')}",
            )

    def test_github_profile_links_use_khangtran69(self):
        self.assertTrue(self.parser.github_profile_links)
        self.assertTrue(
            all(
                url == "https://github.com/KhangTran69"
                or url.startswith("https://github.com/KhangTran69/")
                for url in self.parser.github_profile_links
            ),
            self.parser.github_profile_links,
        )


if __name__ == "__main__":
    unittest.main()
