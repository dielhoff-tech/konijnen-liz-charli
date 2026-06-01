"""
Kiest elke dag 5 willekeurige konijnenweetjes uit een vaste pool
en voegt ze toe aan het begin van de alleWeetjes-array in index.html.
Geen externe API nodig.
"""

import json
import random
import re
import sys
from datetime import date

# ── Pool van konijnenweetjes ──────────────────────────────────────────────────
POOL = [
    "Konijnen kunnen sprongen maken van meer dan een meter hoog en bijna drie meter ver.",
    "Een konijn heeft een 360°-gezichtsveld en kan zelfs achter zich kijken zonder zijn hoofd te draaien.",
    "Konijnen communiceren door te stampen: een harde stamp betekent 'gevaar in de buurt!'",
    "Gelukkige konijnen maken een 'binky': ze springen omhoog en draaien wild in de lucht. Pure vreugde!",
    "Konijnen kunnen tot 70 kilometer per uur rennen — sneller dan veel auto's in de stad.",
    "Konijnen hebben 28 tanden die hun hele leven blijven groeien. Kauwen houdt ze op de juiste lengte.",
    "Een konijn drinkt net zoveel water als een hond van hetzelfde gewicht.",
    "Konijnen zijn crepusculair: het actiefst bij zonsopgang en zonsondergang.",
    "Een groep konijnen heet een 'kolonie'. In het wild leven ze samen in een uitgebreid gangenstelsel.",
    "Konijnen eten een deel van hun eigen keutels ('cecotropen') om extra voedingsstoffen op te nemen.",
    "Konijnen slapen gemiddeld 8 uur per dag — maar vaak met hun ogen half open. Altijd op wacht!",
    "Het oor van een konijn kan tot 270 graden draaien om geluiden van alle kanten op te vangen.",
    "Konijnen herkennen hun naam en hun baasjes, net als honden.",
    "Het hart van een konijn klopt 120 tot 150 keer per minuut — drie keer zo snel als dat van een mens.",
    "Er zijn meer dan 50 erkende konijnenrassen, van het minikonijn (1 kg) tot de Vlaamse Reus (9 kg).",
    "Konijnen zijn strikte planteneters. Ze eten gras, hooi, groenten en af en toe fruit als traktatie.",
    "De tanden van een konijn groeien wel 2 tot 3 millimeter per week.",
    "Konijnen kunnen niet overgeven — vandaar dat een gezond dieet extra belangrijk is.",
    "Een konijn dat zijn hoofd schudt en rondjes rent, is aan het spelen en voelt zich fantastisch.",
    "Konijnen zijn sociale dieren en worden verdrietig als ze alleen worden gehouden.",
    "Het konijn is een van de meest gehouden huisdieren ter wereld, na honden en katten.",
    "Wilde konijnen leven gemiddeld 1 tot 2 jaar; huiskonijnen kunnen wel 10 tot 12 jaar oud worden.",
    "Een vrouwelijk konijn heet een 'voedster', een mannetje een 'ram'.",
    "Baby-konijnen heten 'kittens' of 'kuikens' en worden blind en kaal geboren.",
    "Een voedster kan al na 4 weken opnieuw drachtig worden na de geboorte.",
    "Konijnen hebben een uitstekend gehoor en kunnen geluiden horen tot 2 kilometer ver.",
    "De Angora-konijn heeft zo'n lange vacht dat het regelmatig geschoren moet worden.",
    "Konijnen hebben zweetklieren alleen op hun voetzolen.",
    "Een konijn dat plat op de grond ligt met gestrekte poten is ontspannen en gelukkig.",
    "Konijnen kunnen hun oren onafhankelijk van elkaar bewegen.",
    "Het Hollands dwergkonijn is één van de kleinste rassen en weegt maar 900 gram.",
    "Konijnen hebben een blinde vlek recht voor hun neus — ze zien hun eigen eten niet goed!",
    "Een konijn poetst zichzelf net als een kat, maar heeft een helper nodig voor zijn rug.",
    "Konijnen knabbelen graag op elektrische kabels — opletten dus in huis!",
    "De naam 'konijn' komt van het Latijnse woord 'cuniculus', wat tunnel betekent.",
    "Konijnen zijn oorspronkelijk afkomstig van het Iberisch Schiereiland (Spanje en Portugal).",
    "In Australië is het konijn een invasieve soort die enorme schade aan de natuur aanricht.",
    "Een konijn kan in diepe slaap vallen en dan trillen of pootjes bewegen — ze dromen!",
    "Konijnen communiceren ook via lichaamstaal: opgezette vacht betekent angst of agressie.",
    "Het neusje van een konijn beweegt tot 120 keer per minuut als het alert is.",
    "Konijnen zijn niet geschikt om in te slapen bij kleine kinderen — ze zijn 's nachts wakker.",
    "Een konijn dat tanden knarst (luid) heeft pijn; zacht tandenknarsen betekent tevreden zijn.",
    "Konijnen kunnen een val van grote hoogte overleven dankzij hun soepele skelet.",
    "Het Rex-konijn heeft een bijzonder fluweelachtige vacht door kortere haarschachten.",
    "Konijnen in het wild graven holen die wel 3 meter diep en 45 meter lang kunnen zijn.",
    "Een konijn dat je belikt, beschouwt jou als deel van zijn familie.",
    "Konijnen kunnen van stress sterven — rustige omgevingen zijn essentieel voor hun welzijn.",
    "Het Lionhead-konijn heeft een manen-achtige vacht rond zijn hoofd, net als een leeuwtje.",
    "Konijnen hebben een aanbevolen minimumverblijf van 6 m² — meer is altijd beter.",
    "Konijnen houden van structuur: vaste etenstijden en een vaste slaapplek maken hen gelukkig.",
    "Een konijn kan zijn ogen dicht houden terwijl het wakker is, en open terwijl het slaapt.",
    "Konijnen zijn gevoelig voor hitte; boven de 28°C kunnen ze oververhit raken.",
    "Het Vlaamse Reuzenkonijn kan zo groot worden als een kleine hond.",
    "Konijnen hebben geen kraagbeen — daardoor kunnen ze hun hoofd bijna volledig omdraaien.",
    "Een konijn dat je duwt met zijn neus wil aandacht of wil dat je opschuift.",
    "Konijnen herkennen hun spiegelbeeld niet — ze denken dat er een ander konijn is.",
    "Het konijn speelt een grote rol in de folklore van veel culturen als symbool van vruchtbaarheid.",
    "Konijnen kunnen tot 50 verschillende geluiden maken, van zacht piepen tot luid grommen.",
    "Een drachtige voedster is maar 28 tot 35 dagen drachtig — een van de kortste draagtijden bij zoogdieren.",
    "Konijnen hebben een speciaal deel van hun maag waar vezelrijke bacteriën het voedsel fermenteren.",
    "Het minikonijn werd officieel erkend als ras in 1952 in Nederland.",
]

# ── Kies 5 willekeurige weetjes ───────────────────────────────────────────────
# Gebruik de dag als seed zodat dezelfde dag altijd dezelfde 5 geeft
random.seed(date.today().toordinal())
nieuwe_weetjes = random.sample(POOL, 5)

print("Nieuwe weetjes voor vandaag:")
for i, w in enumerate(nieuwe_weetjes, 1):
    print(f"  {i}. {w}")

# ── Lees index.html ───────────────────────────────────────────────────────────
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── Zoek alleWeetjes array ────────────────────────────────────────────────────
pattern = re.compile(r"(const alleWeetjes\s*=\s*\[)(.*?)(\];)", re.DOTALL)
match = pattern.search(html)
if not match:
    print("alleWeetjes array niet gevonden in index.html", file=sys.stderr)
    sys.exit(1)

# Bouw nieuwe groep
items = ",\n        ".join(json.dumps(w, ensure_ascii=False) for w in nieuwe_weetjes)
nieuwe_groep = f"\n      // {date.today().isoformat()}\n      [\n        {items}\n      ]"

# Voeg toe aan het begin, begrens op 30 groepen
nieuwe_inhoud = nieuwe_groep + "," + match.group(2)
groepen = re.findall(r"\[[\s\S]*?\]", nieuwe_inhoud)
if len(groepen) > 30:
    nieuwe_inhoud = ",\n      ".join(groepen[:30])

html_updated = html[:match.start()] + match.group(1) + nieuwe_inhoud + "\n    " + match.group(3) + html[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_updated)

print(f"index.html bijgewerkt op {date.today().isoformat()}")
