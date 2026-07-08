# Scraper audit — per-company status

Single source of truth for the state of every source in `data/jobs.json` → `companies`. Updated as work progresses. Last full sync: 2026-05-16.

**Status legend**
- `working` — scraper runs cleanly and returns jobs (or 0 relevant today, which is fine)
- `working / 0 relevant` — scraper parses correctly but no current PhD-relevant postings
- `inactive` — flagged `"inactive": true` in companies.json; needs Playwright or has no public endpoint
- `dead` — URL is permanently gone (404, DNS); entry removed from companies.json
- `pending` — not yet audited in this round
- `blocked` — anti-bot blocks all requests-based access

**URL verified** = WebFetch confirmed the URL renders a real careers landing page (or correct URL substituted).

---

## Tier 1 — Danish orgs (complete 2026-05-16)

| Company | URL verified | Status | Approach | Notes |
|---|---|---|---|---|
| Danmarks Nationalbank | ✓ | working / 0 relevant | Workday | tenant=`nationalbanken` site=`Danmarks_Nationalbank` wd103. Only 3 jobs total |
| Nykredit | ✓ | working (8) | Custom (Talentsoft) | `scrape_nykredit` — `/api/talentsoft/getfilteredjoblist/` returns JSON; detail URL = `?reference=<ref>` |
| ATP | ✓ | working (2) | scrape_html_generic | path_fragment=`/karriere/`; title from nested heading |
| PFA | ✓ | working / 0 relevant | Custom | `scrape_pfa` — `<li.jobs-listing__list-item>` cards link to SAP SuccessFactors. 9 jobs visible, all admin/student |
| Jyske Bank | — | inactive | — | Cloudflare 403 even with full browser headers |
| SimCorp | ✓ | working (3) | Workday | tenant=`simcorp` site=`SimCorp_Jobs` |
| Saxo Bank | ✓ | working / 0 relevant | Workday | tenant=`saxobank` site=`CareeratSaxoBank`. 68 jobs total, none PhD-relevant currently |
| Lunar | — | inactive | — | No public careers page — LinkedIn only |
| Nordea | — | inactive | — | TLS fingerprint blocks requests-based access |
| VIVE | ✓ | working / 0 relevant | scrape_html_generic | path_fragment=`candidate.hr-manager.net`. 1 job total, not PhD-relevant |
| Kraka | — | inactive | — | No own ATS — open positions posted on jobindex.dk only |
| Rockwool Foundation Research Unit | ✓ | working (2) | scrape_html_generic | path_fragment=`/stillingsopslag/`; `stillingsopslag` prefix stripped in clean_title |
| Novo Nordisk | — | inactive | — | Fully SPA — SAP SuccessFactors search not server-rendered |
| Vestas | ✓ | working (1) | scrape_html_generic | URL updated to `/search`; path_fragment=`/job/` |
| Ørsted | — | inactive | — | Cloudflare 403 on `/api/jobs/jobList` POST |
| Maersk | — | inactive | — | `career.maersk.com` unreachable; no public ATS endpoint discovered |
| LEGO Group - DK | ✓ | working (38) | Workday | tenant=`lego` site=`LEGO_External` wd103 |

## Tier 2 — International banks / quant (complete 2026-05-16)

| Company | URL verified | Status | Approach | Notes |
|---|---|---|---|---|
| Goldman Sachs | — | inactive | — | Custom SPA at `higher.gs.com` — no public JSON endpoint |
| JP Morgan | — | inactive | — | TLS fingerprint blocks requests-based access (HTTP/2 stream reset) |
| Barclays | ✓ | working | Workday | tenant=`barclays` site=`External_Career_Site_Barclays`. 1163 jobs total |
| HSBC | — | inactive | — | Avature SPA at `hsbc.avature.net` — jobs not in static HTML |
| Citadel | — | inactive | — | Cloudflare 403 even with browser headers; old domain dead |
| Man Group | ✓ | working | Greenhouse | token=`mangroup`. 60 jobs total |
| Deutsche Bank | — | inactive | — | Custom SPA at `careers.db.com` — no API discoverable |
| Commerzbank | — | inactive | — | Custom SPA at `jobs.commerzbank.com` — no API discoverable |

## Tier 3 — Big tech (complete 2026-05-16)

| Company | URL verified | Status | Approach | Notes |
|---|---|---|---|---|
| QuantumBlack | — | inactive | — | mckinsey.com TLS issues; standalone quantumblack.com domain dead |
| Google | ✓ | working | Custom | `scrape_google` — server-rendered job slugs at `/about/careers/applications/jobs/results/?q=research&page=N`, title derived from URL slug |
| DeepMind | ✓ | working | Greenhouse | token=`deepmind`. 62 jobs total |

---

## Already working (baseline, not in this audit)

Optiver, Flow Traders, Squarepoint Capital, Danske Commodities, INCommodities, Nitor Energy, MFT Energy, Copenhagen Economics, ECB, Det Økonomiske Råd, Qube Research & Technologies, Danske Bank, Two Sigma, European Central Bank.
