"""
Kiest elke dag 5 willekeurige konijnenweetjes en schrijft ze naar weetjes.json.
Wordt uitgevoerd door GitHub Actions elke ochtend om 07:30.
"""
import json, random
from datetime import date

POOL = [
    "Konijnen kunnen sprongen maken van meer dan een meter hoog en bijna drie meter ver.",
    "Een konijn heeft een 360°-gezichtsveld en kan zelfs achter zich kijken zonder zijn hoofd te draaien.",
    "Konijnen communiceren door te stampen: een harde stamp betekent 'gevaar in de buurt!'",
    "Gelukkige konijnen maken een 'binky': ze springen omhoog en draaien wild in de lucht.",
    "Konijnen kunnen tot 70 kilometer per uur rennen — sneller dan veel auto's in de stad.",
    "Konijnen hebben 28 tanden die hun hele leven blijven groeien. Kauwen houdt ze op de juiste lengte.",
    "Een konijn drinkt net zoveel water als een hond van hetzelfde gewicht.",
    "Konijnen zijn crepusculair: het actiefst bij zonsopgang en zonsondergang.",
    "Een groep konijnen heet een 'kolonie'. Ze leven in het wild samen in een gangenstelsel.",
    "Konijnen eten een deel van hun eigen keutels om extra voedingsstoffen op te nemen.",
    "Konijnen slapen gemiddeld 8 uur per dag, vaak met hun ogen half open.",
    "Het oor van een konijn kan tot 270 graden draaien om geluiden van alle kanten op te vangen.",
    "Konijnen herkennen hun naam en hun baasjes, net als honden.",
    "Het hart van een konijn klopt 120 tot 150 keer per minuut — drie keer zo snel als bij een mens.",
    "Er zijn meer dan 50 erkende konijnenrassen, van minikonijn (1 kg) tot Vlaamse Reus (9 kg).",
    "Konijnen zijn strikte planteneters: gras, hooi, groenten en af en toe fruit als traktatie.",
    "De tanden van een konijn groeien wel 2 tot 3 millimeter per week.",
    "Konijnen kunnen niet overgeven — vandaar dat een gezond dieet extra belangrijk is.",
    "Een konijn dat zijn hoofd schudt en rondjes rent, is aan het spelen en voelt zich fantastisch.",
    "Konijnen zijn sociale dieren en worden verdrietig als ze alleen worden gehouden.",
    "Het konijn is één van de meest gehouden huisdieren ter wereld, na honden en katten.",
    "Wilde konijnen leven gemiddeld 1 tot 2 jaar; huiskonijnen kunnen wel 10 tot 12 jaar oud worden.",
    "Een vrouwelijk konijn heet een 'voedster', een mannetje een 'ram'.",
    "Baby-konijnen heten 'kittens' en worden blind en kaal geboren.",
    "Een voedster kan al na 4 weken opnieuw drachtig worden na de geboorte.",
    "Konijnen hebben een uitstekend gehoor en kunnen geluiden horen tot 2 kilometer ver.",
    "De Angora-konijn heeft zo'n lange vacht dat het regelmatig geschoren moet worden.",
    "Konijnen hebben zweetklieren alleen op hun voetzolen.",
    "Een konijn dat plat op de grond ligt met gestrekte poten is ontspannen en gelukkig.",
    "Konijnen kunnen hun oren onafhankelijk van elkaar bewegen.",
    "Het Hollands dwergkonijn weegt maar ongeveer 900 gram.",
    "Konijnen hebben een blinde vlek recht voor hun neus — ze zien hun eigen eten niet goed!",
    "Een konijn poetst zichzelf net als een kat, maar heeft hulp nodig voor zijn rug.",
    "Konijnen knabbelen graag op elektrische kabels — opletten in huis!",
    "De naam 'konijn' komt van het Latijnse woord 'cuniculus', wat tunnel betekent.",
    "Konijnen zijn oorspronkelijk afkomstig van het Iberisch Schiereiland.",
    "In Australië is het konijn een invasieve soort die enorme schade aan de natuur aanricht.",
    "Een konijn kan in diepe slaap vallen en dan trillen of zijn pootjes bewegen — ze dromen!",
    "Konijnen communiceren via lichaamstaal: opgezette vacht betekent angst of agressie.",
    "Het neusje van een konijn beweegt tot 120 keer per minuut als het alert is.",
    "Het Rex-konijn heeft een bijzonder fluweelachtige vacht door kortere haarschachten.",
    "Wilde konijnen graven holen die wel 3 meter diep en 45 meter lang kunnen zijn.",
    "Een konijn dat je belikt, beschouwt jou als deel van zijn familie.",
    "Konijnen kunnen van stress overlijden — rustige omgevingen zijn essentieel.",
    "Het Lionhead-konijn heeft een manen-achtige vacht rond zijn hoofd, net als een leeuwtje.",
    "Konijnen houden van structuur: vaste etenstijden en een vaste slaapplek maken hen gelukkig.",
    "Konijnen zijn gevoelig voor hitte; boven de 28°C kunnen ze oververhit raken.",
    "Het Vlaamse Reuzenkonijn kan zo groot worden als een kleine hond.",
    "Een konijn dat je duwt met zijn neus wil aandacht of wil dat je opschuift.",
    "Het konijn speelt een grote rol in de folklore als symbool van vruchtbaarheid.",
    "Konijnen kunnen tot 50 verschillende geluiden maken, van zacht piepen tot luid grommen.",
    "Een drachtige voedster is maar 28 tot 35 dagen drachtig.",
    "Een konijn dat in een cirkel om je heen rent, is verliefd op je!",
    "Het Belgisch Reus-konijn kan wel 12 kilogram wegen.",
    "Een konijn dat zijn tanden zachtjes op je klikt, zegt 'ik hou van je!'",
    "Konijnen vermijden direct zonlicht en zoeken altijd schaduw op warme dagen.",
    "Het konijn heeft een speciale klier onder zijn kin waarmee het zijn territorium markeert.",
    "Konijnen hebben betere nachtzicht dan mensen, maar zien minder kleuren.",
    "Konijnen zijn schone dieren: ze besteden dagelijks uren aan zelfverzorging.",
    "In Japan zijn konijnencafés enorm populair, waar je konijnen kunt aaien en voeren.",
    "Het oudste bekende huiskonijn leefde 18 jaar — een wereldrecord!",
    "Een gecastreerd konijn leeft gemiddeld langer en is rustiger.",
    "Konijnen knabbelen niet voor niks: hun tanden moeten afgesleten worden, anders worden ze te lang.",
    "Konijnen leven in het wild in grote familiegroepen met een duidelijke rangorde.",
    "Het lopen van een konijn lijkt op galopperen: beide achterpoten landen vóór de voorpoten.",
    "Jonge konijnen verlaten het nest al na 3 tot 4 weken.",
    "Konijnen kunnen niet alleen leven: ze hebben minstens één soortgenoot nodig.",
    "Konijnen ruiken graag aan nieuwe objecten voordat ze ze aanraken.",
    "Een konijn dat zijn oren plat houdt, voelt zich bedreigd of ongelukkig.",
    "Konijnen houden van routines — veranderingen in hun omgeving kunnen hen stressen.",
    "Konijnen hebben een dunne huid die makkelijk scheurt — wees voorzichtig met tillen.",
    "Een konijn dat op zijn zij valt en stil blijft liggen is zeer tevreden, niet ziek.",
    "Konijnen kunnen achterwaarts springen als ze schrikken.",
    "Konijnen zijn intelligente dieren die spelletjes kunnen leren, zoals doosjes omduwen.",
    "De ogen van een konijn zijn aan de zijkant van zijn hoofd voor maximaal zicht.",
    "Konijnen kunnen goed springen maar minder goed landen — val voorkomen is belangrijk.",
    "Konijnen kunnen hoofdwonden oplopen als ze te hard met hun hoofd schudden.",
    "Het minikonijn werd officieel erkend als ras in 1952 in Nederland.",
    "Konijnen hebben in totaal 6 snijharen boven en 2 onder — ideaal voor precies kauwen.",
    "Een konijn kan gemiddeld 80 tot 120 gram hooi per dag eten.",
    "Konijnen hebben een speciaal deel van hun maag waar bacteriën het voedsel fermenteren.",
    "Konijnen produceren twee soorten keutels: harde en zachte (cecotropen die ze opeten).",
    "Konijnen kunnen niet goed temperatuurwisselingen verdragen.",
    "Een konijn dat wiebelt met zijn staartje terwijl het eet, is erg blij met zijn eten.",
    "Konijnen kunnen meerdere commando's begrijpen als ze goed getraind zijn.",
    "Konijnen hebben een speciaal bot in hun nek waardoor ze snel kunnen reageren op gevaar.",
    "Een moederkonijn bezoekt haar jongen maar 2 keer per dag om ze te voeden.",
    "Konijnen gebruiken hun staartje als signaal: omhoog betekent gevaar!",
    "Konijnen zijn kleurenblind voor rood en groen, maar zien blauw en geel heel goed.",
    "Het neusje van een konijn heeft 100 miljoen reukzintuigcellen — 20x meer dan een mens.",
    "Konijnen kunnen tot 3 jaar oud worden voordat ze als 'volwassen' worden beschouwd.",
    "Een konijn dat zijn voet stampt in huis, geeft aan dat het iets niet fijn vindt.",
    "Konijnen hebben 18 spieren in elk oor — zo kunnen ze ze zo goed bewegen.",
    "Konijnen kauwen gemiddeld 120 keer per minuut — echte kauwmachines!",
    "Het Hotot-konijn heeft een wit lichaam met een zwarte ring om elk oog — uniek in de wereld.",
    "Konijnen in het wild zijn echte kuddedieren: ze verdedigen elkaar tegen roofdieren.",
    "Een konijn kan zijn eigen vacht zo goed poetsen dat het nooit een bad nodig heeft.",
]

# Zelfde dag = zelfde 5 weetjes (reproduceerbaar)
random.seed(date.today().toordinal())
gekozen = random.sample(POOL, 5)

data = {
    "datum": date.today().isoformat(),
    "weetjes": gekozen
}

with open("weetjes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ weetjes.json bijgewerkt voor {date.today().isoformat()}")
for i, w in enumerate(gekozen, 1):
    print(f"  {i}. {w}")
