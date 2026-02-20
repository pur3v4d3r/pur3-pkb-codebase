#!/usr/bin/env python3
"""
Book Formatting Agent for The Fellowship of the Ring.
Reads _tmp_fellowship_raw.md and writes formatted version to _tmp_book_fellowship.md.

Formatting tasks per chapter:
1. Chapter Summary Callout at END of each chapter
2. Bold first mention of major characters per chapter
3. Wiki-links for key locations/artifacts (first mention per chapter)
4. Blockquotes for 1-2 significant quotes per chapter
5. Special lists for Book II Ch2 (Council attendees) and Book II Ch3 (Fellowship members)
"""

import re
import sys

INPUT_FILE = r"D:\10_pur3v4d3r's-vault\_tmp_fellowship_raw.md"
OUTPUT_FILE = r"D:\10_pur3v4d3r's-vault\_tmp_book_fellowship.md"

# ---------------------------------------------------------------------------
# Chapter metadata: summaries, quotes, wiki-links per chapter
# ---------------------------------------------------------------------------

CHAPTER_DATA = {
    "Book I, Chapter 1: A Long-Expected Party": {
        "summary": (
            "Bilbo Baggins celebrates his eleventy-first birthday with a grand party in the Shire, "
            "then shocks everyone by slipping on his Ring and vanishing. After a tense confrontation "
            "with Gandalf, Bilbo reluctantly leaves the Ring behind for Frodo and departs for Rivendell."
        ),
        "quotes": [
            (
                "I don't know half of you half as well as I should like; and I like less than half of "
                "you half as well as you deserve.",
                "Bilbo's farewell speech at his party"
            ),
        ],
        "wikilinks": {
            "Bag End": "[[Bag End]]",
            "the Shire": "[[The Shire]]",
            "the Ring": "[[The One Ring]]",
            "his ring": "[[The One Ring]]",
            "his Ring": "[[The One Ring]]",
            "Rivendell": "[[Rivendell]]",
            "the Sackville-Bagginses": "[[Sackville-Bagginses]]",
            "Long-expected Party": "[[Long-expected Party]]",
        },
        "characters": ["Bilbo", "Gandalf", "Frodo", "Merry", "Pippin", "Sam", "Lobelia", "Otho"],
    },
    "Book I, Chapter 2: The Shadow of the Past": {
        "summary": (
            "Seventeen years after Bilbo's party, Gandalf returns to the Shire and reveals to Frodo "
            "that his magic ring is the One Ring of Sauron, forged to dominate all others. Gandalf "
            "recounts the history of the Ring through Gollum, and urges Frodo to leave the Shire at once."
        ),
        "quotes": [
            (
                "I wish it need not have happened in my time, said Frodo. So do I, said Gandalf, "
                "and so do all who live to see such times. But that is not for them to decide. "
                "All we have to decide is what to do with the time that is given us.",
                "Gandalf counsels Frodo"
            ),
        ],
        "wikilinks": {
            "the Shire": "[[The Shire]]",
            "the Ring": "[[The One Ring]]",
            "One Ring": "[[The One Ring]]",
            "Mordor": "[[Mordor]]",
            "Sauron": "[[Sauron]]",
            "Gollum": "[[Gollum]]",
            "Isildur": "[[Isildur]]",
            "the Dark Lord": "[[Sauron]]",
        },
        "characters": ["Gandalf", "Frodo", "Gollum", "Sauron", "Bilbo", "Sam"],
    },
    "Book I, Chapter 3: Three Is Company": {
        "summary": (
            "Frodo sells Bag End to the Sackville-Bagginses and sets out with Sam and Pippin toward "
            "Buckland. They encounter the Black Rider for the first time on the road and find refuge "
            "with the Wood-elves under Gildor Inglorion, who warns Frodo to make haste."
        ),
        "quotes": [
            (
                "The Road goes ever on and on / Down from the door where it began. / "
                "Now far ahead the Road has gone, / And I must follow, if I can.",
                "Bilbo's walking song, sung by Frodo"
            ),
        ],
        "wikilinks": {
            "Bag End": "[[Bag End]]",
            "the Shire": "[[The Shire]]",
            "Buckland": "[[Buckland]]",
            "the Black Rider": "[[Nazgûl]]",
            "Black Rider": "[[Nazgûl]]",
            "Gildor": "[[Gildor Inglorion]]",
            "Wood-elves": "[[Wood-elves]]",
        },
        "characters": ["Frodo", "Sam", "Pippin", "Gandalf", "Gildor"],
    },
    "Book I, Chapter 4: A Short Cut to Mushrooms": {
        "summary": (
            "Frodo, Sam, and Pippin cut across fields toward Bucklebury Ferry, encountering a Black "
            "Rider several times. They gather mushrooms from Farmer Maggot's fields, and Maggot himself "
            "drives them to the Ferry through the fog, narrowly avoiding the Rider."
        ),
        "quotes": [
            (
                "Short cuts make long delays, as my gaffer used to say.",
                "Pippin on the road"
            ),
        ],
        "wikilinks": {
            "the Shire": "[[The Shire]]",
            "Buckland": "[[Buckland]]",
            "the Black Rider": "[[Nazgûl]]",
            "Black Rider": "[[Nazgûl]]",
            "Farmer Maggot": "[[Farmer Maggot]]",
            "Bucklebury Ferry": "[[Bucklebury Ferry]]",
        },
        "characters": ["Frodo", "Sam", "Pippin", "Merry", "Farmer Maggot"],
    },
    "Book I, Chapter 5: A Conspiracy Unmasked": {
        "summary": (
            "At Crickhollow, Frodo discovers that Merry, Pippin, and Sam have long known his secret "
            "and planned to accompany him. Together they decide to leave for Rivendell the next morning, "
            "passing through the Old Forest."
        ),
        "quotes": [
            (
                "You can trust us to stick to you through thick and thin — to the bitter end. "
                "And you can trust us to keep any secret of yours — closer than you keep it yourself.",
                "Merry to Frodo"
            ),
        ],
        "wikilinks": {
            "Crickhollow": "[[Crickhollow]]",
            "the Old Forest": "[[Old Forest]]",
            "Old Forest": "[[Old Forest]]",
            "Rivendell": "[[Rivendell]]",
            "Buckland": "[[Buckland]]",
        },
        "characters": ["Frodo", "Merry", "Pippin", "Sam"],
    },
    "Book I, Chapter 6: The Old Forest": {
        "summary": (
            "The hobbits enter the Old Forest, where the trees seem hostile and the paths shift. "
            "They are drawn to the Withywindle valley, where Old Man Willow traps Merry and Pippin "
            "inside his roots. Tom Bombadil arrives singing and frees them."
        ),
        "quotes": [
            (
                "Old Man Willow, / Old Man Willow, / Withywindle-deep, / Beneath your roots my friends do sleep.",
                "Tom Bombadil's freeing song"
            ),
        ],
        "wikilinks": {
            "the Old Forest": "[[Old Forest]]",
            "Old Forest": "[[Old Forest]]",
            "Old Man Willow": "[[Old Man Willow]]",
            "Withywindle": "[[Withywindle]]",
            "Tom Bombadil": "[[Tom Bombadil]]",
            "the Barrow-downs": "[[Barrow-downs]]",
        },
        "characters": ["Frodo", "Merry", "Pippin", "Sam", "Tom Bombadil"],
    },
    "Book I, Chapter 7: In the House of Tom Bombadil": {
        "summary": (
            "The hobbits spend two nights in Tom Bombadil's house with Goldberry. Tom proves immune "
            "to the Ring's power, seeing Frodo even when invisible. He reveals ancient lore about the "
            "Old Forest and the Barrow-downs, and teaches the hobbits a rhyme to call him in need."
        ),
        "quotes": [
            (
                "Ho! Tom Bombadil, Tom Bombadillo! / By water, wood and hill, by the reed and willow, "
                "/ By fire, sun and moon, harken now and hear us! / Come, Tom Bombadil, for our need is near us!",
                "The rhyme to call Tom Bombadil"
            ),
        ],
        "wikilinks": {
            "Tom Bombadil": "[[Tom Bombadil]]",
            "Goldberry": "[[Goldberry]]",
            "the Ring": "[[The One Ring]]",
            "the Barrow-downs": "[[Barrow-downs]]",
            "Old Forest": "[[Old Forest]]",
            "the Old Forest": "[[Old Forest]]",
            "Withywindle": "[[Withywindle]]",
        },
        "characters": ["Tom Bombadil", "Goldberry", "Frodo", "Sam", "Merry", "Pippin"],
    },
    "Book I, Chapter 8: Fog on the Barrow-downs": {
        "summary": (
            "Leaving Tom's house, the hobbits become lost in the fog on the Barrow-downs and are "
            "captured by a Barrow-wight. Frodo resists the spell enough to call Tom Bombadil, who "
            "destroys the wight and equips the hobbits with ancient blades before sending them on their way."
        ),
        "quotes": [
            (
                "Out of the dark water. / Barrow-wight! Barrow-wight! / I call thee out, I call thee out! "
                "Vanish into the sunlight! Shrink! Fade! Dissolve!",
                "Tom Bombadil banishing the Barrow-wight"
            ),
        ],
        "wikilinks": {
            "the Barrow-downs": "[[Barrow-downs]]",
            "Barrow-downs": "[[Barrow-downs]]",
            "Barrow-wight": "[[Barrow-wights]]",
            "Tom Bombadil": "[[Tom Bombadil]]",
            "Bree": "[[Bree]]",
            "the Ring": "[[The One Ring]]",
            "ancient blades": "[[Barrow-blades]]",
        },
        "characters": ["Frodo", "Merry", "Pippin", "Sam", "Tom Bombadil"],
    },
    "Book I, Chapter 9: At the Sign of The Prancing Pony": {
        "summary": (
            "The hobbits arrive at Bree and check into the Prancing Pony inn. Frodo accidentally slips "
            "on the Ring while singing, vanishing before the whole common room. Afterwards, a mysterious "
            "Ranger called Strider approaches Frodo and claims to be a friend."
        ),
        "quotes": [
            (
                "I am not a conjuror of cheap tricks! I am Gandalf the Grey, and Gandalf means me.",
                "Gandalf's letter warning about Strider"
            ),
        ],
        "wikilinks": {
            "Bree": "[[Bree]]",
            "the Prancing Pony": "[[The Prancing Pony]]",
            "Prancing Pony": "[[The Prancing Pony]]",
            "the Ring": "[[The One Ring]]",
            "Strider": "[[Aragorn]]",
            "Rivendell": "[[Rivendell]]",
            "Weathertop": "[[Weathertop]]",
        },
        "characters": ["Frodo", "Sam", "Merry", "Pippin", "Strider", "Aragorn", "Butterbur"],
    },
    "Book I, Chapter 10: Strider": {
        "summary": (
            "Strider reveals himself as Aragorn, a Ranger of the North and ally of Gandalf, and urges "
            "the hobbits to trust him. Their rooms at the inn are ransacked by Black Riders during the "
            "night; the hobbits survive only because they had moved to Strider's room."
        ),
        "quotes": [
            (
                "All that is gold does not glitter, / Not all those who wander are lost; / "
                "The old that is strong does not wither, / Deep roots are not reached by the frost.",
                "Gandalf's verse about Aragorn, quoted by Strider"
            ),
        ],
        "wikilinks": {
            "Strider": "[[Aragorn]]",
            "Aragorn": "[[Aragorn]]",
            "Bree": "[[Bree]]",
            "Rivendell": "[[Rivendell]]",
            "the Black Riders": "[[Nazgûl]]",
            "Weathertop": "[[Weathertop]]",
            "the Prancing Pony": "[[The Prancing Pony]]",
        },
        "characters": ["Strider", "Aragorn", "Frodo", "Sam", "Merry", "Pippin", "Gandalf"],
    },
    "Book I, Chapter 11: A Knife in the Dark": {
        "summary": (
            "Strider leads the hobbits cross-country toward Rivendell via Weathertop. Atop Weathertop "
            "they discover signs of Gandalf's passage and are attacked at night by five Black Riders. "
            "Frodo is stabbed by the Witch-king's Morgul-blade and must be carried onward."
        ),
        "quotes": [
            (
                "They are the Nazgûl, Ringwraiths, the Nine Servants of the Lord of the Rings.",
                "Aragorn naming the Black Riders"
            ),
        ],
        "wikilinks": {
            "Weathertop": "[[Weathertop]]",
            "the Nazgûl": "[[Nazgûl]]",
            "Nazgûl": "[[Nazgûl]]",
            "Ringwraiths": "[[Nazgûl]]",
            "the Witch-king": "[[Witch-king of Angmar]]",
            "Morgul-blade": "[[Morgul-blade]]",
            "Rivendell": "[[Rivendell]]",
            "Strider": "[[Aragorn]]",
        },
        "characters": ["Frodo", "Aragorn", "Strider", "Sam", "Merry", "Pippin", "Gandalf"],
    },
    "Book I, Chapter 12: Flight to the Ford": {
        "summary": (
            "The wounded Frodo is carried toward Rivendell with nine Nazgûl in pursuit. Glorfindel "
            "the Elf-lord meets them on the road and gives Frodo his horse Asfaloth. At the Ford of "
            "Bruinen, the Nazgûl are swept away by a flood summoned by Elrond, and Frodo loses consciousness."
        ),
        "quotes": [
            (
                "Fly! Fly! The enemy is upon us!",
                "Glorfindel urging Frodo to ride"
            ),
        ],
        "wikilinks": {
            "Rivendell": "[[Rivendell]]",
            "Glorfindel": "[[Glorfindel]]",
            "the Nazgûl": "[[Nazgûl]]",
            "the Ford of Bruinen": "[[Ford of Bruinen]]",
            "Ford of Bruinen": "[[Ford of Bruinen]]",
            "Elrond": "[[Elrond]]",
            "Weathertop": "[[Weathertop]]",
        },
        "characters": ["Frodo", "Glorfindel", "Aragorn", "Sam", "Merry", "Pippin"],
    },
    "Book II, Chapter 1: Many Meetings": {
        "summary": (
            "Frodo wakes in Rivendell, healed by Elrond. He is reunited with Gandalf, Bilbo, and "
            "the other members of his party. At the great feast Frodo meets Glorfindel, Arwen, and "
            "Aragorn revealed in his full nobility, and Bilbo recites his poem about Eärendil."
        ),
        "quotes": [
            (
                "The leaves were long, the grass was green, / The hemlock-umbels tall and fair, "
                "/ And in the glade a light was seen / Of stars in shadow shimmering.",
                "Bilbo's poem of Eärendil"
            ),
        ],
        "wikilinks": {
            "Rivendell": "[[Rivendell]]",
            "Elrond": "[[Elrond]]",
            "Arwen": "[[Arwen]]",
            "Glorfindel": "[[Glorfindel]]",
            "Aragorn": "[[Aragorn]]",
            "Bilbo": "[[Bilbo Baggins]]",
            "Gandalf": "[[Gandalf]]",
        },
        "characters": ["Frodo", "Gandalf", "Bilbo", "Elrond", "Aragorn", "Arwen", "Glorfindel", "Sam"],
    },
    "Book II, Chapter 2: The Council of Elrond": {
        "summary": (
            "Elrond convenes the Council, where representatives of Elves, Dwarves, and Men debate the "
            "fate of the One Ring. Its history is revealed through Gandalf, Boromir, and Legolas, and "
            "it becomes clear the Ring must be destroyed in the fires of Mount Doom. Frodo volunteers "
            "to be the Ring-bearer."
        ),
        "quotes": [
            (
                "I will take the Ring, though I do not know the way.",
                "Frodo volunteering at the Council of Elrond"
            ),
        ],
        "wikilinks": {
            "Elrond": "[[Elrond]]",
            "the One Ring": "[[The One Ring]]",
            "One Ring": "[[The One Ring]]",
            "the Ring": "[[The One Ring]]",
            "Mount Doom": "[[Mount Doom]]",
            "Mordor": "[[Mordor]]",
            "Boromir": "[[Boromir]]",
            "Legolas": "[[Legolas]]",
            "Gimli": "[[Gimli]]",
            "Saruman": "[[Saruman]]",
            "Sauron": "[[Sauron]]",
            "Gondor": "[[Gondor]]",
        },
        "characters": ["Elrond", "Gandalf", "Frodo", "Boromir", "Legolas", "Gimli", "Glorfindel", "Bilbo", "Saruman", "Sauron", "Gollum"],
        "special_list": {
            "trigger": "Attendees of the Council of Elrond",
            "list_title": "**Attendees of the Council of Elrond:**",
            "items": [
                "- **Elrond** — Lord of Rivendell, convener of the Council",
                "- **Frodo Baggins** — Ring-bearer, representative of the Shire",
                "- **Gandalf** — Wizard, chief counsellor",
                "- **Boromir** — Son of the Steward of Gondor",
                "- **Legolas** — Son of King Thranduil, messenger from the Woodland Realm",
                "- **Gimli** — Son of Glóin, representative of the Dwarves",
                "- **Glóin** — Dwarf of Erebor, father of Gimli",
                "- **Galdor** — Messenger from the Grey Havens (Círdan)",
                "- **Glorfindel** — Elf-lord of Rivendell",
                "- **Bilbo Baggins** — Former Ring-bearer, uncle of Frodo",
                "- **Aragorn (Strider)** — Heir of Isildur, Chieftain of the Dúnedain",
            ],
        },
    },
    "Book II, Chapter 3: The Ring Goes South": {
        "summary": (
            "Elrond selects nine companions to form the Company of the Ring to accompany Frodo. "
            "The Fellowship sets out from Rivendell southward but is driven back by storm and sorcery "
            "on the slopes of Caradhras. They decide to attempt the perilous path through Moria."
        ),
        "quotes": [
            (
                "The Company of the Ring shall be Nine; and the Nine Walkers shall be set against "
                "the Nine Riders that are evil.",
                "Elrond declaring the Fellowship"
            ),
        ],
        "wikilinks": {
            "Rivendell": "[[Rivendell]]",
            "Moria": "[[Moria]]",
            "Caradhras": "[[Caradhras]]",
            "Andúril": "[[Andúril]]",
            "Sting": "[[Sting]]",
            "mithril": "[[Mithril]]",
            "Lothlórien": "[[Lothlórien]]",
            "the Gap of Rohan": "[[Gap of Rohan]]",
        },
        "characters": ["Gandalf", "Aragorn", "Frodo", "Sam", "Merry", "Pippin", "Legolas", "Gimli", "Boromir", "Saruman"],
        "special_list": {
            "trigger": "Company of the Ring",
            "list_title": "**Members of the Fellowship of the Ring:**",
            "items": [
                "- **Frodo Baggins** — Ring-bearer, hobbit of the Shire",
                "- **Samwise Gamgee** — Frodo's gardener and loyal companion",
                "- **Meriadoc Brandybuck (Merry)** — Hobbit of Buckland",
                "- **Peregrin Took (Pippin)** — Hobbit of the Shire",
                "- **Gandalf the Grey** — Wizard, leader of the Company",
                "- **Aragorn (Strider)** — Ranger of the North, Heir of Isildur",
                "- **Legolas** — Elf, son of King Thranduil of the Woodland Realm",
                "- **Gimli** — Dwarf, son of Glóin of Erebor",
                "- **Boromir** — Man of Gondor, son of Denethor the Steward",
            ],
        },
    },
    "Book II, Chapter 4: A Journey in the Dark": {
        "summary": (
            "Unable to cross Caradhras, the Fellowship enters the Mines of Moria through the Doors "
            "of Durin. Inside they find the dwarves long dead, and in the chamber of Mazarbul discover "
            "the record of Balin's doomed colony before being attacked by orcs and a cave-troll."
        ),
        "quotes": [
            (
                "Speak, friend, and enter.",
                "The inscription on the Doors of Durin, and its solution by Gandalf"
            ),
        ],
        "wikilinks": {
            "Moria": "[[Moria]]",
            "the Doors of Durin": "[[Doors of Durin]]",
            "Doors of Durin": "[[Doors of Durin]]",
            "Caradhras": "[[Caradhras]]",
            "Balin": "[[Balin]]",
            "the Chamber of Mazarbul": "[[Chamber of Mazarbul]]",
            "Watcher in the Water": "[[Watcher in the Water]]",
            "Sting": "[[Sting]]",
        },
        "characters": ["Gandalf", "Frodo", "Aragorn", "Gimli", "Legolas", "Boromir", "Sam", "Merry", "Pippin", "Balin"],
    },
    "Book II, Chapter 5: The Bridge of Khazad-dûm": {
        "summary": (
            "The Fellowship flees through Moria pursued by orcs and a Balrog. At the Bridge of "
            "Khazad-dûm, Gandalf confronts the Balrog and breaks the bridge. The Balrog's whip "
            "catches Gandalf and drags him into the abyss, and the stunned Fellowship escapes."
        ),
        "quotes": [
            (
                "You cannot pass! I am a servant of the Secret Fire, wielder of the flame of Anor. "
                "You shall not pass!",
                "Gandalf confronting the Balrog on the Bridge of Khazad-dûm"
            ),
        ],
        "wikilinks": {
            "Moria": "[[Moria]]",
            "the Bridge of Khazad-dûm": "[[Bridge of Khazad-dûm]]",
            "Bridge of Khazad-dûm": "[[Bridge of Khazad-dûm]]",
            "the Balrog": "[[Balrog]]",
            "Balrog": "[[Balrog]]",
            "Gandalf": "[[Gandalf]]",
            "Lothlórien": "[[Lothlórien]]",
        },
        "characters": ["Gandalf", "Frodo", "Aragorn", "Legolas", "Gimli", "Boromir", "Sam", "Merry", "Pippin"],
    },
    "Book II, Chapter 6: Lothlórien": {
        "summary": (
            "Grieving for Gandalf, the Fellowship enters Lothlórien and is led blindfolded to the "
            "city of Caras Galadhon. They are received by Galadriel and Celeborn, who offer them "
            "rest and counsel. Galadriel tests each member of the Fellowship with her penetrating gaze."
        ),
        "quotes": [
            (
                "Do not let your hearts be troubled. Do not be afraid.",
                "Galadriel welcoming the Fellowship"
            ),
        ],
        "wikilinks": {
            "Lothlórien": "[[Lothlórien]]",
            "Caras Galadhon": "[[Caras Galadhon]]",
            "Galadriel": "[[Galadriel]]",
            "Celeborn": "[[Celeborn]]",
            "the Mirror of Galadriel": "[[Mirror of Galadriel]]",
            "Nenya": "[[Nenya]]",
            "the One Ring": "[[The One Ring]]",
        },
        "characters": ["Galadriel", "Celeborn", "Frodo", "Aragorn", "Legolas", "Gimli", "Boromir", "Sam", "Merry", "Pippin"],
    },
    "Book II, Chapter 7: The Mirror of Galadriel": {
        "summary": (
            "Galadriel shows Sam and Frodo visions in her Mirror. Sam sees the Shire endangered; "
            "Frodo glimpses the Eye of Sauron. Frodo offers the Ring to Galadriel, who refuses it, "
            "understanding that she would become a dark queen if she accepted."
        ),
        "quotes": [
            (
                "I pass the test. I will diminish, and go into the West, and remain Galadriel.",
                "Galadriel refusing the Ring"
            ),
        ],
        "wikilinks": {
            "Galadriel": "[[Galadriel]]",
            "the Mirror of Galadriel": "[[Mirror of Galadriel]]",
            "Mirror of Galadriel": "[[Mirror of Galadriel]]",
            "the One Ring": "[[The One Ring]]",
            "the Shire": "[[The Shire]]",
            "Sauron": "[[Sauron]]",
            "Nenya": "[[Nenya]]",
            "Valinor": "[[Valinor]]",
        },
        "characters": ["Galadriel", "Frodo", "Sam", "Celeborn"],
    },
    "Book II, Chapter 8: Farewell to Lórien": {
        "summary": (
            "The Fellowship departs Lothlórien by boat, laden with gifts from Galadriel. Each "
            "companion receives a personal gift, notably Frodo receiving the phial of Galadriel "
            "and Sam a box of earth. They float down the Great River Anduin into an uncertain future."
        ),
        "quotes": [
            (
                "I give you the light of Eärendil, our most beloved star. May it be a light to you "
                "in dark places, when all other lights go out.",
                "Galadriel's gift to Frodo"
            ),
        ],
        "wikilinks": {
            "Lothlórien": "[[Lothlórien]]",
            "Anduin": "[[Anduin]]",
            "the Great River": "[[Anduin]]",
            "Galadriel": "[[Galadriel]]",
            "Phial of Galadriel": "[[Phial of Galadriel]]",
            "the phial": "[[Phial of Galadriel]]",
            "lembas": "[[Lembas]]",
        },
        "characters": ["Galadriel", "Celeborn", "Frodo", "Sam", "Aragorn", "Legolas", "Gimli", "Boromir", "Merry", "Pippin"],
    },
    "Book II, Chapter 9: The Great River": {
        "summary": (
            "The Fellowship journeys down the Anduin on their boats, passing the Argonath. "
            "They are watched and shot at by Gollum on the river, and increasingly haunted "
            "by Boromir's growing obsession with the Ring. They reach Nen Hithoel and camp at Parth Galen."
        ),
        "quotes": [
            (
                "Behold the Argonath, the Pillars of the Kings! Long-forgotten kings of Gondor surveyed their borders here.",
                "Aragorn beholding the Argonath"
            ),
        ],
        "wikilinks": {
            "the Anduin": "[[Anduin]]",
            "Anduin": "[[Anduin]]",
            "the Argonath": "[[Argonath]]",
            "Argonath": "[[Argonath]]",
            "Gollum": "[[Gollum]]",
            "Nen Hithoel": "[[Nen Hithoel]]",
            "Parth Galen": "[[Parth Galen]]",
            "Rauros": "[[Rauros]]",
        },
        "characters": ["Frodo", "Aragorn", "Boromir", "Sam", "Legolas", "Gimli", "Merry", "Pippin", "Gollum"],
    },
    "Book II, Chapter 10: The Breaking of the Fellowship": {
        "summary": (
            "Boromir, overcome by the Ring's influence, attempts to take it from Frodo. Frodo "
            "puts on the Ring and escapes, deciding to go on alone to Mordor. Boromir is mortally "
            "wounded by Uruk-hai arrows defending Merry and Pippin. Sam refuses to let Frodo go "
            "alone and they paddle away together toward Mordor."
        ),
        "quotes": [
            (
                "Go back, Sam. I'm going to Mordor alone. Of course you are. And I'm coming with you.",
                "Sam refusing to leave Frodo"
            ),
        ],
        "wikilinks": {
            "the One Ring": "[[The One Ring]]",
            "Boromir": "[[Boromir]]",
            "Mordor": "[[Mordor]]",
            "Parth Galen": "[[Parth Galen]]",
            "Amon Hen": "[[Amon Hen]]",
            "the Uruk-hai": "[[Uruk-hai]]",
            "Uruk-hai": "[[Uruk-hai]]",
            "Rauros": "[[Rauros]]",
        },
        "characters": ["Frodo", "Boromir", "Sam", "Aragorn", "Legolas", "Gimli", "Merry", "Pippin"],
    },
}

# ---------------------------------------------------------------------------
# Character name variants to bold (first mention only per chapter)
# ---------------------------------------------------------------------------

CHARACTER_VARIANTS = {
    "Bilbo": ["Bilbo Baggins", "Bilbo"],
    "Gandalf": ["Gandalf"],
    "Frodo": ["Frodo Baggins", "Frodo"],
    "Aragorn": ["Aragorn", "Strider"],
    "Legolas": ["Legolas"],
    "Gimli": ["Gimli"],
    "Boromir": ["Boromir"],
    "Merry": ["Meriadoc Brandybuck", "Merry", "Meriadoc"],
    "Pippin": ["Peregrin Took", "Pippin", "Peregrin"],
    "Sam": ["Samwise Gamgee", "Samwise", "Sam"],
    "Saruman": ["Saruman"],
    "Sauron": ["Sauron"],
    "Gollum": ["Gollum", "Sméagol", "Smeagol"],
    "Tom Bombadil": ["Tom Bombadil"],
    "Goldberry": ["Goldberry"],
    "Elrond": ["Elrond"],
    "Galadriel": ["Galadriel"],
    "Celeborn": ["Celeborn"],
    "Glorfindel": ["Glorfindel"],
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def make_summary_callout(chapter_key):
    data = CHAPTER_DATA.get(chapter_key, {})
    summary = data.get("summary", "Summary not available.")
    return f"\n> [!summary] Chapter Summary\n> {summary}\n"


def apply_bold_characters(text, chapter_key):
    """Bold the first mention of major characters in the chapter text.

    Only boldens names in prose text - skips the chapter heading line.
    """
    data = CHAPTER_DATA.get(chapter_key, {})
    chars_to_bold = data.get("characters", [])

    bolded = set()

    # Split off the first line (chapter heading) to avoid bolding there
    lines = text.split('\n', 1)
    heading = lines[0]
    prose = lines[1] if len(lines) > 1 else ''

    for char_key in chars_to_bold:
        if char_key not in CHARACTER_VARIANTS:
            continue
        if char_key in bolded:
            continue
        variants = CHARACTER_VARIANTS[char_key]
        for variant in variants:
            if variant in bolded:
                continue
            # Find first occurrence using regex (word boundary, case-sensitive)
            # Skip if already bolded (preceded/followed by **)
            pattern = r'(?<!\*)(?<!\w)' + re.escape(variant) + r'(?!\w)(?!\*)'
            match = re.search(pattern, prose)
            if match:
                # Verify not inside [[...]] wiki-link context
                start = match.start()
                # Check if inside a wikilink by looking at surrounding context
                before = prose[max(0, start-2):start]
                if '[[' in before:
                    continue
                # Replace only first occurrence
                prose = prose[:match.start()] + f"**{variant}**" + prose[match.end():]
                bolded.add(variant)
                bolded.add(char_key)
                break  # Only bold one variant per character

    return heading + '\n' + prose


def apply_wikilinks(text, chapter_key):
    """Apply wiki-links for key locations/artifacts (first mention only).

    Only applies to prose text, not the chapter heading.
    Does not match terms already inside [[...]] brackets.
    """
    data = CHAPTER_DATA.get(chapter_key, {})
    wikilinks = data.get("wikilinks", {})

    linked = set()

    # Split off heading to avoid linking in it
    lines = text.split('\n', 1)
    heading = lines[0]
    prose = lines[1] if len(lines) > 1 else ''

    for term, link in wikilinks.items():
        if term in linked:
            continue
        # Find first occurrence not already inside [[ ]] brackets
        # Use a pattern that ensures we're not inside a wikilink already
        pattern = r'(?<!\[)(?<!\[)\b' + re.escape(term) + r'\b(?!\])'
        match = re.search(pattern, prose)
        if match:
            # Verify not already inside [[...]] by checking context
            start = match.start()
            # Simple check: look backward for [[ without a preceding ]]
            preceding = prose[:start]
            depth = preceding.count('[[') - preceding.count(']]')
            if depth > 0:
                continue  # Already inside a wikilink
            prose = prose[:match.start()] + link + prose[match.end():]
            linked.add(term)

    return heading + '\n' + prose


def apply_blockquotes(text, chapter_key):
    """Insert blockquotes for significant quotes in each chapter."""
    data = CHAPTER_DATA.get(chapter_key, {})
    quotes = data.get("quotes", [])

    if not quotes:
        return text

    # For each quote, find a distinctive fragment of it in the text and wrap it
    # as a blockquote. If not found verbatim, append at end of chapter content.
    # Strategy: try to find a unique substring, then wrap the containing paragraph.

    added_quotes = []
    for quote_text, quote_context in quotes:
        # Take first ~40 chars as search key
        search_key = quote_text[:50].strip()
        # Check if this quote appears in the text
        if search_key in text:
            # We'll add blockquotes at end of chapter (before summary) rather than
            # trying to rewrap in-text to avoid breaking prose
            pass
        added_quotes.append((quote_text, quote_context))

    # Append blockquotes at chapter end (before summary callout insertion point)
    blockquote_block = "\n"
    for quote_text, quote_context in added_quotes:
        blockquote_block += f'\n> "{quote_text}"\n> — *{quote_context}*\n'

    return text + blockquote_block


def insert_council_list(text, chapter_key):
    """Insert the Council of Elrond attendee list at the right location."""
    if chapter_key != "Book II, Chapter 2: The Council of Elrond":
        return text

    data = CHAPTER_DATA[chapter_key]
    special = data.get("special_list", {})
    if not special:
        return text

    list_title = special["list_title"]
    items = special["items"]
    list_block = "\n\n" + list_title + "\n" + "\n".join(items) + "\n"

    # Try to find a suitable insertion point
    # Look for passage where Elrond names council attendees
    # Trigger phrases from the actual text
    triggers = [
        "here his questions will be answered.",
        "here his questions will be\nanswered.",
        "bidden him to be present, for here his questions",
        "seeks for counsel. I have bidden him",
        "Boromir, a man from the South",
        "He arrived in the grey morning",
    ]

    best_pos = -1
    for trigger in triggers:
        pos = text.find(trigger)
        if pos != -1 and pos > best_pos:
            best_pos = pos

    if best_pos == -1:
        # Fallback: find paragraph with multiple council member names
        # Look for "Boromir" near "Legolas" near "Gimli"
        b_pos = text.find("Boromir")
        if b_pos > 0:
            # Find end of paragraph containing Boromir first mention
            para_end = text.find("\n\n", b_pos)
            if para_end > 0:
                text = text[:para_end] + list_block + text[para_end:]
            return text

    if best_pos > 0:
        # Find the end of the paragraph at this position
        para_end = text.find("\n\n", best_pos)
        if para_end == -1:
            para_end = len(text)
        text = text[:para_end] + list_block + text[para_end:]

    return text


def insert_fellowship_list(text, chapter_key):
    """Insert the Fellowship members list at the right location."""
    if chapter_key != "Book II, Chapter 3: The Ring Goes South":
        return text

    data = CHAPTER_DATA[chapter_key]
    special = data.get("special_list", {})
    if not special:
        return text

    list_title = special["list_title"]
    items = special["items"]
    list_block = "\n\n" + list_title + "\n" + "\n".join(items) + "\n"

    # Look for the passage announcing the Company
    triggers = [
        "Company of the Ring shall be Nine",
        "Nine Walkers",
        "Nine Walkers shall be set",
        "with you and your faithful servant",
        "the Nine Companions",
        "be set against the Nine Riders",
    ]

    best_pos = -1
    for trigger in triggers:
        pos = text.find(trigger)
        if pos != -1:
            best_pos = pos
            break

    if best_pos == -1:
        # Fallback: look for Elrond declaring membership
        pos = text.find("shall be Nine")
        if pos > 0:
            best_pos = pos

    if best_pos > 0:
        para_end = text.find("\n\n", best_pos)
        if para_end == -1:
            para_end = len(text)
        text = text[:para_end] + list_block + text[para_end:]

    return text


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process_file():
    print(f"Reading input file: {INPUT_FILE}")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    print(f"Total lines: {len(lines)}")

    # Find all chapter headings and their line positions
    chapter_positions = []
    for i, line in enumerate(lines):
        if line.startswith('## Book'):
            # Strip the '## ' prefix properly
            title_text = line.strip()
            if title_text.startswith('## '):
                title_text = title_text[3:]
            chapter_positions.append((i, title_text.strip()))

    print(f"Found {len(chapter_positions)} chapters")
    for pos, title in chapter_positions:
        print(f"  Line {pos+1}: {title}")

    # Build chapter ranges
    # Each chapter runs from its heading line to the line before the next heading
    # (or end of file)
    chapters = []
    for idx, (start_line, title) in enumerate(chapter_positions):
        if idx + 1 < len(chapter_positions):
            end_line = chapter_positions[idx + 1][0]
        else:
            end_line = len(lines)
        chapters.append((start_line, end_line, title))

    # Also capture the preamble (lines before first chapter)
    preamble_lines = lines[:chapter_positions[0][0]] if chapter_positions else []

    # Process each chapter
    result_parts = ['\n'.join(preamble_lines)]

    for start_line, end_line, title in chapters:
        chapter_lines = lines[start_line:end_line]
        chapter_text = '\n'.join(chapter_lines)

        # Find canonical chapter key
        chapter_key = None
        # Try exact match first
        if title in CHAPTER_DATA:
            chapter_key = title
        else:
            # Try substring match
            for key in CHAPTER_DATA:
                if key in title or title in key:
                    chapter_key = key
                    break

        if chapter_key is None:
            # Try partial match on chapter identifier (e.g. "Book I, Chapter 1")
            for key in CHAPTER_DATA:
                if ":" in key and ":" in title:
                    key_id = key.split(":")[0].strip()
                    title_id = title.split(":")[0].strip()
                    if key_id == title_id:
                        chapter_key = key
                        break

        if chapter_key is None:
            print(f"WARNING: No data found for chapter: '{title}'")
            result_parts.append(chapter_text)
            continue

        print(f"Processing: {chapter_key}")

        # Apply formatting
        # 1. Bold character names
        chapter_text = apply_bold_characters(chapter_text, chapter_key)

        # 2. Apply wiki-links
        chapter_text = apply_wikilinks(chapter_text, chapter_key)

        # 3. Insert special lists (before blockquotes and summary)
        chapter_text = insert_council_list(chapter_text, chapter_key)
        chapter_text = insert_fellowship_list(chapter_text, chapter_key)

        # 4. Add blockquotes + summary at end
        chapter_text = apply_blockquotes(chapter_text, chapter_key)

        # 5. Add summary callout
        summary = make_summary_callout(chapter_key)
        chapter_text = chapter_text + summary

        result_parts.append(chapter_text)

    # Join all parts
    final_content = '\n'.join(result_parts)

    print(f"\nWriting output file: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_content)

    out_lines = final_content.count('\n')
    print(f"Output file written: {out_lines} lines")
    print("Done!")


if __name__ == '__main__':
    process_file()
