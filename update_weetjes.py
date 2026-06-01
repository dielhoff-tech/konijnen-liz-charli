"""
Genereert 5 nieuwe konijnenweetjes via de Anthropic API
en voegt ze toe aan het begin van de alleWeetjes-array in index.html.
"""

import anthropic
import json
import re
import sys
from datetime import date

# ── Genereer weetjes ──────────────────────────────────────────────────────────
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": (
                "Geef me precies 5 unieke, leuke en feitelijk correcte weetjes over konijnen. "
                "Schrijf ze in het Nederlands, leuk leesbaar voor kinderen en jongeren. "
                "Varieer het onderwerp: gedrag, biologie, geschiedenis, rassen, verzorging, etc. "
                "Geef ALLEEN een JSON-array terug met 5 strings, geen uitleg of opmaak eromheen. "
                "Voorbeeld: [\"Weetje 1.\", \"Weetje 2.\", ...]"
            ),
        }
    ],
)

raw = message.content[0].text.strip()

# Verwijder eventuele markdown code fences
raw = re.sub(r"^```[a-z]*\n?", "", raw)
raw = re.sub(r"\n?```$", "", raw)

try:
    nieuwe_weetjes = json.loads(raw)
    assert isinstance(nieuwe_weetjes, list) and len(nieuwe_weetjes) == 5
except Exception as e:
    print(f"Fout bij parsen van API-antwoord: {e}\nRaw: {raw}", file=sys.stderr)
    sys.exit(1)

print("Nieuwe weetjes gegenereerd:")
for i, w in enumerate(nieuwe_weetjes, 1):
    print(f"  {i}. {w}")

# ── Lees index.html ───────────────────────────────────────────────────────────
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── Zoek en vervang alleWeetjes array ────────────────────────────────────────
# Vind de hele alleWeetjes array in de JS
pattern = re.compile(
    r"(const alleWeetjes\s*=\s*\[)(.*?)(\];)",
    re.DOTALL
)

match = pattern.search(html)
if not match:
    print("alleWeetjes array niet gevonden in index.html", file=sys.stderr)
    sys.exit(1)

# Parse huidige groepen
bestaande_inhoud = match.group(2)

# Bouw de nieuwe groep als JSON-array string
nieuwe_groep_items = ",\n        ".join(json.dumps(w, ensure_ascii=False) for w in nieuwe_weetjes)
nieuwe_groep = f"""
      // {date.today().isoformat()}
      [
        {nieuwe_groep_items}
      ]"""

# Voeg de nieuwe groep toe aan het begin
nieuwe_inhoud = nieuwe_groep + "," + bestaande_inhoud

# Begrens op max 30 groepen (verwijder oudste als nodig)
groepen = re.findall(r"\[[\s\S]*?\]", nieuwe_inhoud)
if len(groepen) > 30:
    # Herbouw met alleen de eerste 30
    groepen = groepen[:30]
    nieuwe_inhoud = ",\n      ".join(groepen)

nieuwe_array = match.group(1) + nieuwe_inhoud + "\n    " + match.group(3)
html_updated = html[:match.start()] + nieuwe_array + html[match.end():]

# ── Schrijf terug ─────────────────────────────────────────────────────────────
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_updated)

print(f"index.html bijgewerkt op {date.today().isoformat()}")
