---
name: company-facts
description: Extract structured, sourced facts about a company from web pages, filings and reports. Use when building a company profile, an account brief or a readiness assessment, after web search has found the relevant pages. Produces a fact table where every fact has a value, a year, a source URL and an evidence tag.
---

# Company fact extraction

Turn page text into a fact table. Never fill a field from memory.

## Fields to extract

| Group | Fields |
| --- | --- |
| Identity | Legal name, sector, activity in one sentence, headquarters, sites in Belgium or Luxembourg |
| Scale | Employees (group and local), turnover, other financials (profit, equity, investment, grants), each with year |
| Ownership | Owner or parent, listed or private, leadership names and titles (CEO, CIO, CTO, CDO, COO, head of IT or data) |
| Strategy | Stated strategy, recent moves (acquisitions, new sites, investments), regulation that applies (DORA, NIS2, CSSF, EU AI Act, sector rules) |
| Technology | ERP and core systems, cloud or hosting, data platforms, AI or automation use, open technology or data job postings |

## Helper script

To spot figures in long text before reading it closely:

```
python3 scripts/extract_figures.py page.txt
```

or pipe text in: `... | python3 scripts/extract_figures.py -`

It lists sentences containing money amounts, headcounts, percentages and years, labelled by type. They are candidates: confirm each in context before using it.

## Evidence tags

- **Confirmed**: stated by the company itself or an official filing or register.
- **Research**: stated by a reliable third party (press, analyst, database).
- **Inferred**: your deduction. Say what it is deduced from.

## Rules

- One fact per row: field, value, year, source URL, tag.
- Figures keep their unit and year: "EUR 135m turnover, FY2016/17", never "about 135m".
- If sources disagree, keep the most recent primary source and note the other.
- If a field is not found, write "not found". Do not estimate.
- A job posting is evidence of an intention or a gap, not of a system in production.

## Output

```
| Field | Value | Year | Source | Tag |
| --- | --- | --- | --- | --- |
| Employees, Luxembourg | ~550 | 2025 | https://... | Research |
```

Then a list headed "Not found" with every field that returned nothing.
