from discord import Colour

ZONE_INFO = {
    "Blood Moor and Den of Evil": {
        "name": "Blood Moor and Den of Evil",
        "immunities": ["f", "c"],
        "boss_packs": [7, 9],
        "uniques": ["Corpsefire"],
        "chests": 0,
    },
    "Cold Plains and The Cave": {
        "name": "Cold Plains and The Cave",
        "immunities": ["l", "c", "f"],
        "boss_packs": [13, 16],
        "uniques": ["Bishibosh", "Coldcrow"],
        "chests": 1,
    },
    "Burial Grounds, The Crypt, and The Mausoleum": {
        "name": "Burial Grounds, The Crypt, and The Mausoleum",
        "immunities": ["l"],
        "boss_packs": [8, 10],
        "uniques": ["Blood Raven", "Bonebreaker"],
        "chests": 2,
    },
    "Stony Field": {
        "name": "Stony Field",
        "immunities": ["f", "c", "l", "p"],
        "boss_packs": [7, 9],
        "uniques": ["Rakanishu"],
        "chests": 0,
    },
    "Dark Wood": {
        "name": "Dark Wood",
        "immunities": ["f", "c", "p"],
        "boss_packs": [7, 9],
        "uniques": ["Treehead Woodfist"],
        "chests": 0,
    },
    "The Forgotten Tower": {
        "name": "The Forgotten Tower",
        "immunities": ["f", "l", "ph"],
        "boss_packs": [15, 20],
        "uniques": ["The Countess"],
        "chests": 0,
    },
    "Jail": {
        "name": "Jail",
        "immunities": ["f", "c", "p", "ph"],
        "boss_packs": [18, 24],
        "uniques": ["Pitspawn Fouldog"],
        "chests": 0,
    },
    "Cathedral and Catacombs": {
        "name": "Cathedral and Catacombs",
        "immunities": ["f", "l", "ph", "c"],
        "boss_packs": [27, 35],
        "uniques": ["Bone Ash", "Andariel"],
        "chests": 0,
    },
    "The Pit": {
        "name": "The Pit",
        "immunities": ["f", "c"],
        "boss_packs": [8, 11],
        "uniques": [],
        "chests": 1,
    },
    "Tristram": {
        "name": "Tristram",
        "immunities": ["f", "l", "p"],
        "boss_packs": [5, 6],
        "uniques": ["Griswold"],
        "chests": 0,
    },
    "Moo Moo Farm": {
        "name": "Moo Moo Farm",
        "immunities": [],
        "boss_packs": [6, 8],
        "uniques": ["The Cow King"],
        "chests": 0,
    },
    "Sewers": {
        "name": "Sewers",
        "immunities": ["f", "c", "p", "m"],
        "boss_packs": [18, 24],
        "uniques": ["Radament"],
        "chests": 0,
    },
    "Rocky Waste and Stony Tomb": {
        "name": "Rocky Waste and Stony Tomb",
        "immunities": ["f", "c", "l", "m", "p"],
        "boss_packs": [17, 23],
        "uniques": ["Creeping Feature"],
        "chests": 1,
    },
    "Dry Hills and Halls of the Dead": {
        "name": "Dry Hills and Halls of the Dead",
        "immunities": ["l", "p", "f", "c"],
        "boss_packs": [20, 27],
        "uniques": ["Bloodwitch the Wild"],
        "chests": 0,
    },
    "Far Oasis": {
        "name": "Far Oasis",
        "immunities": ["l", "p", "ph"],
        "boss_packs": [7, 9],
        "uniques": ["Beetleburst"],
        "chests": 0,
    },
    "Lost City, Valley of Snakes, and Claw Viper Temple": {
        "name": "Lost City, Valley of Snakes, and Claw Viper Temple",
        "immunities": ["f", "c", "l", "p", "m"],
        "boss_packs": [21, 28],
        "uniques": ["Dark Elder", "Fangskin"],
        "chests": 0,
    },
    "Arcane Sanctuary": {
        "name": "Arcane Sanctuary",
        "immunities": ["f", "c", "l", "p", "ph"],
        "boss_packs": [7, 9],
        "uniques": ["The Summoner"],
        "chests": 0,
    },
    "Tal Rasha's Tombs and Tal Rasha's Chamber": {
        "name": "Tal Rasha's Tombs and Tal Rasha's Chamber",
        "immunities": ["f", "c", "l", "p", "m"],
        "boss_packs": [49, 63],
        "uniques": ["Ancient Kaa The Soulless", "Duriel"],
        "chests": 6,
    },
    "Spider Forest and Spider Cavern": {
        "name": "Spider Forest and Spider Cavern",
        "immunities": ["c", "l", "p", "f"],
        "boss_packs": [14, 20],
        "uniques": ["Sszark The Burning"],
        "chests": 0,
    },
    "Flayer Jungle and Flayer Dungeon": {
        "name": "Flayer Jungle and Flayer Dungeon",
        "immunities": ["f", "c", "l", "p", "m", "ph"],
        "boss_packs": [22, 29],
        "uniques": ["Stormtree", "Witch Doctor Endugu"],
        "chests": 0,
    },
    "Kurast Bazaar, Ruined Temple, and Disused Fane": {
        "name": "Kurast Bazaar, Ruined Temple, and Disused Fane",
        "immunities": ["f", "c", "ph", "m", "l", "p"],
        "boss_packs": [15, 17],
        "uniques": ["Battlemaid Sarina"],
        "chests": 0,
    },
    "Kurast Sewers": {
        "name": "Kurast Sewers",
        "immunities": ["c", "l", "p", "m"],
        "boss_packs": [12, 14],
        "uniques": ["Icehawk Riftwing"],
        "chests": 1,
    },
    "Travincal": {
        "name": "Travincal",
        "immunities": ["c", "f", "l", "p"],
        "boss_packs": [6, 8],
        "uniques": ["Ismail Vilehand", "Toorc Icefist", "Geleb Flamefinger"],
        "chests": 0,
    },
    "Durance of Hate": {
        "name": "Durance of Hate",
        "immunities": ["c", "f", "l", "p"],
        "boss_packs": [15, 21],
        "uniques": [
            "Wyand Voidbringer",
            "Maffer Dragonhand",
            "Bremm Sparkfist",
            "Mephisto",
        ],
        "chests": 0,
    },
    "Outer Steppes and Plains of Despair": {
        "name": "Outer Steppes and Plains of Despair",
        "immunities": ["f", "c", "l", "p"],
        "boss_packs": [16, 20],
        "uniques": ["Izual"],
        "chests": 0,
    },
    "River of Flame and City of the Damned": {
        "name": "River of Flame and City of the Damned",
        "immunities": ["f", "c", "l", "p"],
        "boss_packs": [14, 17],
        "uniques": ["Hephasto The Armorer"],
        "chests": 0,
    },
    "Chaos Sanctuary": {
        "name": "Chaos Sanctuary",
        "immunities": ["f", "c", "l"],
        "boss_packs": [6, 7],
        "uniques": [
            "Grand Vizier of Chaos",
            "Infector of Souls",
            "Lord De Seis",
            "Diablo",
        ],
        "chests": 0,
    },
    "Bloody Foothills": {
        "name": "Bloody Foothills",
        "immunities": ["f", "c", "l", "p"],
        "boss_packs": [4, 6],
        "uniques": ["Dac Farren", "Shenk The Overseer"],
        "chests": 0,
    },
    "Frigid Highlands": {
        "name": "Frigid Highlands",
        "immunities": ["f", "c", "l", "p", "ph", "m"],
        "boss_packs": [9, 11],
        "uniques": [
            "Eldritch the Rectifier",
            "Sharptooth Slayer",
            "Eyeback the Unleashed",
        ],
        "chests": 0,
    },
    "Glacial Trail": {
        "name": "Glacial Trail",
        "immunities": ["f", "c", "l", "p", "ph"],
        "boss_packs": [7, 9],
        "uniques": ["Bonesaw Breaker"],
        "chests": 0,
    },
    "Crystalline Passage and Frozen River": {
        "name": "Crystalline Passage and Frozen River",
        "immunities": ["f", "c", "p", "ph", "l", "m"],
        "boss_packs": [13, 17],
        "uniques": ["Frozenstein"],
        "chests": 0,
    },
    "Arreat Plateau": {
        "name": "Arreat Plateau",
        "immunities": ["f", "c", "l", "p"],
        "boss_packs": [9, 11],
        "uniques": ["Thresh Socket"],
        "chests": 0,
    },
    "Nihlathak's Temple, Halls of Anguish, Halls of Pain, and Halls of Vaught": {
        "name": "Nihlathak's Temple and Temple Halls",
        "immunities": ["c", "f", "l", "p", "ph", "m"],
        "boss_packs": [12, 14],
        "uniques": ["Pindleskin", "Nihlathak"],
        "chests": 0,
    },
    "Ancient's Way and Icy Cellar": {
        "name": "Ancient's Way and Icy Cellar",
        "immunities": ["c", "l", "p", "ph"],
        "boss_packs": [6, 8],
        "uniques": ["Snapchip Shatter"],
        "chests": 1,
    },
    "Worldstone Keep, Throne of Destruction, and Worldstone Chamber": {
        "name": "Worldstone Keep, Throne of Destruction, and Worldstone Chamber",
        "immunities": ["f", "c", "l", "p", "ph", "m"],
        "boss_packs": [22, 29],
        "uniques": [
            "Colenzo The Annihilator",
            "Achmel The Cursed",
            "Bartuc The Bloody",
            "Ventar The Unholy",
            "Lister The Tormentor",
            "Baal",
        ],
        "chests": 0,
    },
}

ACT_COLORS = {
    "act1": Colour(0x789055),
    "act2": Colour(0xCBB386),
    "act3": Colour(0x3E5926),
    "act4": Colour(0x8C310E),
    "act5": Colour(0xD8D8D5),
}
