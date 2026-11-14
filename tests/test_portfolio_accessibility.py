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
        self._card_link = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "article" and "project-card" in classes:
            self._card = {"title": "", "text": "", "links": []}
            self.project_cards.append(self._card)
        if tag == "h3" and self._card:
            self._heading = True
        if tag == "a":
            href = attrs.get("href", "")
            if self._card is not None:
                self._card_link = {"href": href, "text": ""}
                self._card["links"].append(self._card_link)
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
            self._card_link = None
        if tag == "article":
            self._card = None

    def handle_data(self, data):
        if self._card is not None:
            self._card["text"] += data
            if self._heading:
                self._card["title"] += data
            if self._card_link is not None:
                self._card_link["text"] += data


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

    def test_core_demo_cards_link_to_run_guides_and_limits(self):
        expected_guides = {
            "FlowOps": "https://github.com/KhangTran69/flowops/blob/main/docs/portfolio-demo.md",
            "Garbage Route Optimizer": "https://github.com/KhangTran69/angeles-city-garbage-optimizer/blob/main/README.md#reproduce-the-optimizer-sensitivity-report",
            "IT Help Desk & Asset Management System": "https://github.com/KhangTran69/it-help-desk/blob/main/README.md#local-demo-walkthrough",
            "PoPify": "https://github.com/KhangTran69/popify/blob/main/README.md#isolated-interface-preview-without-docker",
            "Philippine SMS Spam Detector": "https://github.com/KhangTran69/sms-spam-detector/blob/main/README.md#quickstart",
        }
        cards_by_title = {card["title"].strip(): card for card in self.parser.project_cards}

        for title, href in expected_guides.items():
            with self.subTest(project=title):
                self.assertIn(title, cards_by_title)
                guides = [link for link in cards_by_title[title]["links"] if link["href"] == href]
                self.assertEqual(len(guides), 1)
                self.assertIn("Run", guides[0]["text"])
                self.assertIn("evidence", guides[0]["text"].lower())
                self.assertIn("limits", guides[0]["text"].lower())

    def test_core_demo_cards_show_verification_counts_and_limits(self):
        required_evidence = {
            "FlowOps": ["461 tests passed", "20 skipped", "synthetic tickets"],
            "Garbage Route Optimizer": ["74 tests passed", "nine synthetic benchmark runs", "no live road graph"],
            "IT Help Desk & Asset Management System": ["107 tests passed", "5 docker/opt-in selenium checks skipped", "seeded synthetic ticket"],
            "PoPify": ["113 tests passed", "synthetic preview", "PostgreSQL and n8n runtime remain unverified"],
            "Philippine SMS Spam Detector": ["526 tests passed", "3 skipped", "real-world Philippine accuracy"],
        }
        cards_by_title = {card["title"].strip(): card for card in self.parser.project_cards}

        for title, phrases in required_evidence.items():
            with self.subTest(project=title):
                card_text = cards_by_title[title]["text"].lower()
                for phrase in phrases:
                    self.assertIn(phrase.lower(), card_text)

    def test_bid_trace_is_listed_as_a_synthetic_reserve_demo(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="project-reserve"', page)
        self.assertIn('href="https://github.com/KhangTran69/bid-trace"', page)
        self.assertIn("Bid Trace", page)
        self.assertIn("reserve synthetic local demo", page.lower())


if __name__ == "__main__":
    unittest.main()
