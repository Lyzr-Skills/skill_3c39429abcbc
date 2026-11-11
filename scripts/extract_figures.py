#!/usr/bin/env python3
"""List candidate figures (money, headcount, percentages, years) in a text. Standard library only.
Usage: extract_figures.py FILE   (use - for stdin)"""
import re, sys

MONEY = re.compile(r"(€|EUR|USD|\$|£)\s?\d[\d.,\s]*\s?(bn|billion|m|million|mio|k|thousand)?|\d[\d.,]*\s?(bn|billion|million|mio|m)\s?(€|EUR|euros?|USD|\$)", re.I)
HEAD = re.compile(r"\d[\d.,\s]*\+?\s?(employees|staff|people|FTEs?|workers|collaborateurs|salariés|Mitarbeiter)", re.I)
PCT = re.compile(r"\d[\d.,]*\s?%")
YEAR = re.compile(r"\b(19[89]\d|20[0-3]\d)(/\d{2})?\b")
KEYS = re.compile(r"turnover|revenue|chiffre d'affaires|sales|profit|EBITDA|equity|investment|grant|subsid", re.I)

def main():
    src = sys.stdin if len(sys.argv) < 2 or sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8", errors="replace")
    text = re.sub(r"\s+", " ", src.read())
    sentences = re.split(r"(?<=[.!?])\s+", text)
    found = 0
    for s in sentences:
        kinds = []
        if MONEY.search(s): kinds.append("money")
        if HEAD.search(s): kinds.append("headcount")
        if PCT.search(s): kinds.append("percent")
        if not kinds: continue
        if KEYS.search(s): kinds.append("financial-keyword")
        years = sorted(set(m.group(0) for m in YEAR.finditer(s)))
        print(f"[{', '.join(kinds)}]{' years: ' + ', '.join(years) if years else ''}\n  {s.strip()[:400]}")
        found += 1
    if not found:
        print("No figures found.")

if __name__ == "__main__":
    main()
