"""
Kiest elke dag 5 willekeurige konijnenweetjes uit een pool van 100
en werkt index.html bij. Geen externe API nodig.
"""

import json, random, re, sys
from datetime import date

POOL = [
    "Konijnen kunnen sprongen maken van meer dan een meter hoog en bijna drie meter ver.",
    "Een konijn heeft een 360\u00b0-gezichtsveld en kan zelfs achter zich kijken zonder zijn hoofd te draaien.",
    "Konijnen communiceren door te stampen: een harde stamp betekent \'gevaar in de buurt!\'",
    "Gelukkige konijnen maken een \'binky\': ze springen omhoog en draaien wild in de lucht.",
    "Konijnen kunnen tot 70 kilometer per uur rennen \u2014 sneller dan veel auto\'s in de stad.",
    "Konijnen hebben 28 tanden die hun hele leven blijven groeien. Kauwen houdt ze op de juiste lengte.",
    "Een konijn drinkt net zoveel water als een hond van hetzelfde gewicht.",
    "Konijnen zijn crepusculair: het actiefst bij zonsopgang en zonsondergang.",
    "Een groep konijnen heet een \'kolonie\'. In het wild leven ze in een uitgebreid gangenstelsel.",
    "Konijnen eten een deel van hun eigen keutels om extra voedingsstoffen op te nemen.",
    "Konijnen slapen gemiddeld 8 uur per dag, vaak met hun ogen half open.",
    "Het oor van een konijn kan tot 270 graden draaien om geluiden van alle kanten op te vangen.",
    "Konijnen herkennen hun naam en hun baasjes, net als honden.",
    "Het hart van een konijn klopt 120 tot 150 keer per minuut \u2014 drie keer zo snel als dat van een mens.",
    "Er zijn meer dan 50 erkende konijnenrassen, van het minikonijn (1 kg) tot de Vlaamse Reus (9 kg).",
    "Konijnen zijn strikte planteneters: gras, hooi, groenten en af en toe fruit als traktatie.",
    "De tanden van een konijn groeien wel 2 tot 3 millimeter per week.",
    "Konijnen kunnen niet overgeven \u2014 vandaar dat een gezond dieet extra belangrijk is.",
    "Een konijn dat zijn hoofd schudt en rondjes rent, is aan het spelen en voelt zich fantastisch.",
    "Konijnen zijn sociale dieren en worden verdrietig als ze alleen worden gehouden.",
    "Het konijn is \u00e9\u00e9n van de meest gehouden huisdieren ter wereld, na honden en katten.",
    "Wilde konijnen leven gemiddeld 1 tot 2 jaar; huiskonijnen kunnen wel 10 tot 12 jaar oud worden.",
    "Een vrouwelijk konijn heet een \'voedster\', een mannetje een \'ram\'.",
    "Baby-konijnen heten \'kittens\' en worden blind en kaal geboren.",
    "Een voedster kan al na 4 weken opnieuw drachtig worden na de geboorte.",
    "Konijnen hebben een uitstekend gehoor en kunnen geluiden horen tot 2 kilometer ver.",
    "De Angora-konijn heeft zo\'n lange vacht dat het regelmatig geschoren moet worden.",
    "Konijnen hebben zweetklieren alleen op hun voetzolen.",
    "Een konijn dat plat op de grond ligt met gestrekte poten is ontspannen en gelukkig.",
    "Konijnen kunnen hun oren onafhankelijk van elkaar bewegen.",
    "Het Hollands dwergkonijn weegt maar ongeveer 900 gram.",
    "Konijnen hebben een blinde vlek recht voor hun neus \u2014 ze zien hun eigen eten niet goed!",
    "Een konijn poetst zichzelf net als een kat, maar heeft hulp nodig voor zijn rug.",
    "Konijnen knabbelen graag op elektrische kabels \u2014 opletten in huis!",
    "De naam \'konijn\' komt van het Latijnse woord \'cuniculus\', wat tunnel betekent.",
    "Konijnen zijn oorspronkelijk afkomstig van het Iberisch Schiereiland.",
    "In Australi\u00eb is het konijn een invasieve soort die enorme schade aan de natuur aanricht.",
    "Een konijn kan in diepe slaap vallen en dan trillen of zijn pootjes bewegen \u2014 ze dromen!",
    "Konijnen communiceren via lichaamstaal: opgezette vacht betekent angst of agressie.",
    "Het neusje van een konijn beweegt tot 120 keer per minuut als het alert is.",
    "Konijnen kunnen een val van grote hoogte overleven dankzij hun soepele skelet.",
    "Het Rex-konijn heeft een bijzonder fluweelachtige vacht door kortere haarschachten.",
    "Wilde konijnen graven holen die wel 3 meter diep en 45 meter lang kunnen zijn.",
    "Een konijn dat je belikt, beschouwt jou als deel van zijn familie.",
    "Konijnen kunnen van stress overlijden \u2014 rustige omgevingen zijn essentieel.",
    "Het Lionhead-konijn heeft een manen-achtige vacht rond zijn hoofd, net als een leeuwtje.",
    "Konijnen hebben een aanbevolen minimumverblijf van 6 m\u00b2 \u2014 meer is altijd beter.",
    "Konijnen houden van structuur: vaste etenstijden en een vaste slaapplek maken hen gelukkig.",
    "Een konijn kan zijn ogen dicht houden terwijl het wakker is, en open terwijl het slaapt.",
    "Konijnen zijn gevoelig voor hitte; boven de 28\u00b0C kunnen ze oververhit raken.",
    "Het Vlaamse Reuzenkonijn kan zo groot worden als een kleine hond.",
    "Konijnen hebben geen kraagbeen \u2014 daardoor kunnen ze hun hoofd ver omdraaien.",
    "Een konijn dat je duwt met zijn neus wil aandacht of wil dat je opschuift.",
    "Konijnen herkennen hun spiegelbeeld niet \u2014 ze denken dat er een ander konijn is.",
    "Het konijn speelt een grote rol in de folklore als symbool van vruchtbaarheid.",
    "Konijnen kunnen tot 50 verschillende geluiden maken, van zacht piepen tot luid grommen.",
    "Een drachtige voedster is maar 28 tot 35 dagen drachtig.",
    "Konijnen hebben een speciaal deel van hun maag waar bacterien het voedsel fermenteren.",
    "Het minikonijn werd officieel erkend als ras in 1952 in Nederland.",
    "Konijnen hebben in totaal 6 snijharen boven en 2 onder \u2014 ideaal voor precies kauwen.",
    "Een konijn kan gemiddeld 80 tot 120 gram hooi per dag eten.",
    "Konijnen leven in het wild in grote familiegroepen met een duidelijke rangorde.",
    "Het lopen van een konijn lijkt op galopperen: beide achterpoten landen tegelijk voor de voorpoten.",
    "Konijnen hebben een unieke manier van slapen: ze doezelen vaak in korte dutjes van 6-8 minuten.",
    "Jonge konijnen verlaten het nest al na 3 tot 4 weken, hoewel ze nog maar klein zijn.",
    "Konijnen kunnen niet alleen leven: ze hebben minstens \u00e9\u00e9n soortgenoot nodig.",
    "Het konijn heeft vier klauwen per poot en geen scherpe nagels zoals katten.",
    "Konijnen ruiken graag aan nieuwe objecten voordat ze ze aanraken.",
    "Konijnen kunnen tot 30 keer per dag keutels produceren.",
    "Een konijn dat zijn oren plat houdt, voelt zich bedreigd of ongelukkig.",
    "Konijnen houden van routines \u2014 veranderingen in hun omgeving kunnen hen stressen.",
    "Het konijn heeft een enorm goed ruikvermogen: het ruikt gevaar al van ver.",
    "Konijnen hebben een dunne huid die makkelijk scheurt \u2014 wees dus voorzichtig met tillen.",
    "Een konijn dat op zijn zij valt en stil blijft liggen is zeer tevreden, niet ziek.",
    "Konijnen kunnen achterwaarts springen als ze schrikken.",
    "Konijnen zijn intelligente dieren die spelletjes kunnen leren, zoals doosjes omduwen.",
    "De ogen van een konijn zijn aan de zijkant van zijn hoofd geplaatst voor maximaal zicht.",
    "Konijnen eten ook hun eigen haar soms op, maar te veel kan gevaarlijk zijn.",
    "Konijnen kunnen goed springen maar minder goed landen \u2014 val voorkomen is belangrijk.",
    "Een konijn dat in een cirkel om je heen rent, is verliefd op je!",
    "Konijnen kunnen hoofdwonden oplopen als ze te hard met hun hoofd schudden.",
    "Konijnen zijn vegetarisch maar eten soms per ongeluk kleine insecten.",
    "Het Belgisch Reus-konijn kan wel 12 kilogram wegen.",
    "Konijnen die goed verzorgd worden leven gemiddeld langer dan wilde soortgenoten.",
    "Een konijn dat zijn tanden zachtjes op je klikt, zegt eigenlijk \'ik hou van je!\'",
    "Konijnen kunnen last krijgen van haarballenverstopping als ze te weinig vezels eten.",
    "Konijnen vermijden direct zonlicht en zoeken altijd schaduw op warme dagen.",
    "Het konijn heeft een speciale klier onder zijn kin waarmee het zijn territorium markeert.",
    "Konijnen hebben betere nachtzicht dan mensen, maar zien minder kleuren.",
    "Een konijn dat wiebelt met zijn staartje terwijl het eet, is erg blij met zijn eten.",
    "Konijnen zijn schone dieren: ze besteden dagelijks uren aan zelfverzorging.",
    "Konijnen kunnen meerdere talen begrijpen als ze goed getraind zijn.",
    "In Japan zijn konijnencaf\u00e9s enorm populair, waar je konijnen kunt aaien en voeren.",
    "Het oudste bekende huiskonijn leefde 18 jaar \u2014 een wereldrecord!",
    "Konijnen produceren twee soorten keutels: harde en zachte (cecotropen die ze opeten).",
    "Konijnen kunnen niet goed temperatuurwisselingen verdragen.",
    "Een gecastreerd of gesteriliseerd konijn leeft gemiddeld langer en is rustiger.",
    "Konijnen knabbelen niet voor niks: hun tanden moeten afgesleten worden, anders worden ze te lang.",
]

random.seed(date.today().toordinal())
nieuwe_weetjes = random.sample(POOL, 5)

print("Nieuwe weetjes voor vandaag:")
for i, w in enumerate(nieuwe_weetjes, 1):
    print(f"  {i}. {w}")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(r"(const alleWeetjes\s*=\s*\[)(.*?)(\];)", re.DOTALL)
match = pattern.search(html)
if not match:
    print("alleWeetjes array niet gevonden in index.html", file=sys.stderr)
    sys.exit(1)

items = ",\n        ".join(json.dumps(w, ensure_ascii=False) for w in nieuwe_weetjes)
nieuwe_groep = f"\n      // {date.today().isoformat()}\n      [\n        {items}\n      ]"
nieuwe_inhoud = nieuwe_groep + "," + match.group(2)
groepen = re.findall(r"\[[\s\S]*?\]", nieuwe_inhoud)
if len(groepen) > 30:
    nieuwe_inhoud = ",\n      ".join(groepen[:30])

html_updated = html[:match.start()] + match.group(1) + nieuwe_inhoud + "\n    " + match.group(3) + html[match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_updated)

print(f"index.html bijgewerkt op {date.today().isoformat()}")
