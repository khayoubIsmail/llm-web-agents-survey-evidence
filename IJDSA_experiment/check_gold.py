"""Check all four gold files for AMBIGUOUS price nodes (node contains multiple currency amounts)."""
import json, lxml.html, re

for s in ["site_01","site_02","site_03","site_04"]:
    g = json.load(open(f"gold/{s}.json"))
    recs = g.get("records", g)
    root = lxml.html.parse(f"snapshots/{s}/index.html").getroot()
    found = False
    for i, r in enumerate(recs[:10]):
        ev = r.get("evidence", {})
        price_ev = ev.get("price") or {}
        xp = price_ev.get("xpath", "")
        n = root.xpath(xp) if xp else []
        txt = n[0].text_content() if n else ""
        try:
            txt = txt.encode("latin-1").decode("utf-8")
        except Exception:
            pass
        amounts = re.findall(r"\d+[.,]\d{2}", txt)
        if len(set(amounts)) > 1:
            found = True
            gold_amount = r["price"]["amount"]
            print(f"{s} rec{i}: AMBIGUOUS -- node holds {sorted(set(amounts))}, gold={gold_amount}")
    if not found:
        print(f"{s}: OK -- no ambiguous price nodes")

print("\nCheck complete.")
