"""Render the public GitHub contribution calendar as a self-hosted SVG."""

import json
import os
import urllib.request
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape


USERNAME = "krishnaChandak044"
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "contributions.svg"
QUERY = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""


def calendar():
    token = os.environ["GH_TOKEN"]
    payload = json.dumps({"query": QUERY, "variables": {"login": USERNAME}}).encode()
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-contribution-renderer",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors"):
        raise RuntimeError(result["errors"])
    return result["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def level(count):
    if count == 0:
        return 0
    if count < 3:
        return 1
    if count < 6:
        return 2
    if count < 10:
        return 3
    return 4


def render(data):
    weeks = data["weeks"]
    colors = ["#1c2a36", "#174d58", "#1b7d82", "#32b1aa", "#72e1c5"]
    left, top, step, square = 118, 89, 17, 13
    width = left + len(weeks) * step + 55
    height = 248
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Krishna Chandak contribution graph</title>',
        f'<desc id="desc">{data["totalContributions"]:,} contributions in the last year, shown by day.</desc>',
        '<rect width="100%" height="100%" rx="18" fill="#0d1724"/>',
        '<rect x="1" y="1" width="99.8%" height="99.2%" rx="17" fill="none" stroke="#284354"/>',
        '<text x="32" y="45" fill="#edf6fb" font-family="Arial,Helvetica,sans-serif" font-size="23" font-weight="700">Consistency in code</text>',
        f'<text x="{width-32}" y="45" fill="#71dfc5" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="18" font-weight="700">{data["totalContributions"]:,} contributions</text>',
    ]
    for row, label in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        parts.append(f'<text x="75" y="{top + row * step + 11}" fill="#8ea8b8" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="12">{label}</text>')
    prev_month = None
    for col, week in enumerate(weeks):
        for day in week["contributionDays"]:
            day_date = date.fromisoformat(day["date"])
            if day_date.day <= 7 and day_date.month != prev_month:
                parts.append(f'<text x="{left + col * step}" y="76" fill="#8ea8b8" font-family="Arial,Helvetica,sans-serif" font-size="12">{day_date.strftime("%b")}</text>')
                prev_month = day_date.month
            row = (day_date.weekday() + 1) % 7
            count = day["contributionCount"]
            label = escape(f'{day["date"]}: {count} contribution' + ("" if count == 1 else "s"))
            parts.append(f'<rect x="{left + col * step}" y="{top + row * step}" width="{square}" height="{square}" rx="3" fill="{colors[level(count)]}"><title>{label}</title></rect>')
    parts.append(f'<text x="{width-187}" y="{height-24}" fill="#8ea8b8" font-family="Arial,Helvetica,sans-serif" font-size="12">Less</text>')
    for index, color in enumerate(colors):
        parts.append(f'<rect x="{width-153 + index*20}" y="{height-35}" width="13" height="13" rx="3" fill="{color}"/>')
    parts.append(f'<text x="{width-36}" y="{height-24}" fill="#8ea8b8" font-family="Arial,Helvetica,sans-serif" font-size="12">More</text>')
    parts.append('</svg>')
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text("\n".join(parts) + "\n", encoding="utf-8")


if __name__ == "__main__":
    render(calendar())
