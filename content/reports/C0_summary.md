# C0 — Company Universe: summary

## Files created
- `content/universe/`: U-IN-1 Pinlo (quick commerce), U-IN-2 Tarazu Credit (digital lender), U-IN-3 Aarambh Learning (test-prep edtech), U-IN-4 Kesari Naturals (family D2C personal care), U-GL-1 Ticketwise (B2B helpdesk SaaS), U-GL-2 Stridelab (subscription fitness), U-GL-3 Fixnest (home-services marketplace), U-GL-4 Northgate Home (e-commerce retailer).
- `tools/validate_universe.py`: checks structure (sections, 8–12 canon facts, 5–6 characters, context) and recomputes the arithmetic.

## Validation
`python tools/validate_universe.py content/universe`: 0 failures. Recomputed: U-IN-1 orders, GMV, revenue, cost per order, burn; U-IN-2 book, disbursals, funnel, P&L; U-IN-3 revenue and cost shares; U-IN-4 channel mix and orders; U-GL-1 ARR per customer and seat; U-GL-2 ARR and discount cohort; U-GL-3 bookings and take rate; U-GL-4 P&L.

## Resolved after review (26 Sep 2026)
- **Names:** a web search found real products called Nukkad (Nukkad Shops, nukkad.co), Sahaj (a lending platform) and Handyhive (home-services apps). Renamed to **Pinlo** (U-IN-1), **Tarazu Credit** (U-IN-2) and **Fixnest** (U-GL-3). The other five showed no direct match. Kesari Naturals is a common word with many similar brand names, so it stays flagged.
- **Wireframe data:** the mock-ups now follow canon (no "10-minute promise"; evening orders per hour 85 / 120 / 130 / 105 / 60; 40 riders on the evening roster; the ₹4.5 lakh figure is 15 riders at a guaranteed minimum of about ₹30,000 a month). Rebuilt from `design/_src/bodies_a.py`.
- **Day-1 micro-case:** decided that `DAY1` is the one allowed exception to "Universe companies only": a fictional one-person restaurant (Neha Rao) so a beginner meets a small, familiar business. Recorded in `BUILD_PLAN.md` (C7) and `kit/00_Build_Rules.md`.

## Still needs human review
1. Names are only web-checked, not legally cleared. A trademark search (IP India for the IN names) is still needed before public use `[VERIFY]`.
2. Real-world claims `[VERIFY]`: NBFC status and digital KYC rules (U-IN-2), marketplace commission range (U-IN-4), leakage estimate method (U-GL-3), marketing-claim rules (U-IN-3).
3. Choices made without asking: Bengaluru/Hyderabad/Pune and six tier-2 cities for U-IN-1; Toronto, Denver, Chicago and Columbus as GLOBAL headquarters; character names are generic, but check none matches a well-known person.

## New characters used elsewhere
Meera Iyer, Karthik Naidu, Divya Menon and Anil Shetty (U-IN-1) match the wireframe screens. Neha Rao (Day-1) is outside the Universe.

## Universe changes
All new (first version). "Used by" lists name only the planned capstones so far: CAP-PM (U-IN-1), CAP-BA and CAP-PD (U-IN-2), CAP-DA (U-GL-2).
