import random
import os
from .pelts import (
    black_colours,
    brown_colours,
    ginger_colours,
    white_colours,
    cream_colours,
    grey_colours,
    blue_colours,
    yellow_colours,
    green_colours,
    purple_colours,
    pride_colours,
    albino_sprites,
    melanistic_sprites,
    wings,
    sphynx,
    magic_kitty,
    tabbies,
    spotted,
    exotic,
    torties,
    )

class Name():
  special_suffixes: {
    "kitten": "kit",
    "apprentice": "paw",
    "medicine cat apprentice": "paw",
    "mediator apprentice": "paw",
	"leader": "star",
    "kittypet": "",
    "loner": "",
    "rogue": ""
    },

  normal_suffixes : ["fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "pelt", "pelt", "pelt", "pelt", 
        "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "face", "face", "face", "face", "face", "face", "face",
        "face", "face", "face", "shine", "shine", "shine", "cloud", "cloud", "cloud", "cloud", "cloud", "field", "field", "field", "field", 
        "field", "pet", "pet", "pet", "bull", "bull", "bull", "bull", "bull", "heart", "heart", "heart", "heart", 
        "heart", "heart", "flower", "flower", "flower", "flower", "flower", "flight", "flight", "flight", "flight", "flight",
        "pool", "pool", "pool", "bunny", "bunny", "bunny", "bunny", "bunny", "storm", "storm", "storm", "storm", 
        "storm", "kudzu", "kudzu", "kudzu", "roar", "roar", "roar", "roar", "bark", "bark", "bark", "path", "path", 
        "path", "claw", "claw", "claw", "claw", "claw", "claw", "claw", "claw", "foot", "foot", "foot", "foot", "foot", 
        "foot", "foot", "foot", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "nose", "nose", 
        "nose", "nose", "nose", "nose", "nose", "nose", "whisker", "whisker", "whisker", "whisker", "whisker", 
        "whisker", "whisker", "whisker", "leaf", "leaf", "leaf", "leaf", "leaf", "leaf", "feather", "feather", 
        "feather", "feather", "feather", "feather", "throat", "throat", "throat", "throat", "throat", "throat", "root", 
        "root", "root", "root", "root", "dig", "dig", "dig", "dig", "dig", "stream", "stream", "stream", "stream", 
        "stream", "flame", "flame", "flame", "leg", "leg", "leg", "leg", "fang", "fang", "fang", "fang", "eye", 
        "eye", "eye", "eye", "ear", "ear", "ear", "ear", "wing", "wing", "wing", "wing", "tree", "tree", "tree", "tree", "berry", 
        "berry", "berry", "berry", "fall", "fall", "step", "step", "splash", "splash", "moon", "sun", "earth"],

  tabby_suffixes: ["stripe", "stripe", "stripe", "stripe"],
  spotted_suffixes: ["spot", "spot", "spot", "spot"],
  exotic_suffixes: ["stripe", "stripe", "stripe", "stripe", "spot", "spot", "spot", "spot", "patch", "patch", "patch"],
  tortie_suffixes: ["spot", "spot", "spot", "spot", "patch", "patch", "patch"],
  sphynx_suffixes: ["skin", "skin", "skin", "skin", "skin", "skin", "skin", "skin", "skin", "skin", "coat", "coat", 
		"coat", "coat", "coat", "coat", "coat", "coat", "coat", "coat", "shine", "shine", "shine", "spirit"],
  magic_suffixes: ["shine", "shine", "shine", "magic", "magic", "magic", "moon", "moon", "sun", "sun", "earth", 
		"earth", "spirt"],

  normal_prefixes: ["Fluff", "Plume", "Down", "Shag", "Mop", "Fuzz", "Fan", "Little", "Small", "Tiny", "Runt", "Big", "Boney",
			"Spike", "Ribbon", "Cotton", "Clear", "Silk", "Wool", "Bare", "Show", "Sparkle", "Single", "One", "Two", 
			"Three", "Four", "Five", "Six", "Ichi", "Ni", "San", "Yon", "Go", "Roku", "Nana", "Hatchi", "Kyu", "Kit",
			"Tiger", "Leopard", "Lion", "Hyena", "Wolf", "Fox", "Blank", "Autumn", "Bayou", "Bay", "Desert", "Cliff",
			"Bird", "Bog", "Bough", "Breeze", "Brook", "Bug", "Burr", "Coast", "Crag", "Creek", "Cress", "Damp", 
			"Drift", "Drought", "Dry", "Dune", "Frost", "Thunder", "Wind", "Shadow", "Hub", "Fallow", "Fidget", 
			"Fierce", "Fin", "Fish", "Flail", "Fleet", "Flood", "Flurry", "Flutter", "Freeze", "Frozen", "Gem", "Giant", 
			"Gorge", "Gust", "Harvest", "Hatch", "Heath", "Heavy", "Hill", "Hoarse", "Hoot", "Hop", "Hope", "Jet",
			"Jump", "Lake", "Leap", "Long", "Loud", "Low", "Flip", "Marsh", "Meadow", "Mellow", "Merry", "Lost",
			"Mock", "Moor", "Mumble", "Peak", "Peat", "Perch", "Pod", "Pond", "Pounce", "Prance", "Prim",
			"Quick", "Rattle", "Rift", "Rot", "Rubble", "Running", "Rush", "Sea", "Shard", "Shimmer", "Slope", 
			"Sneeze", "Song", "Spire", "Spring", "Strike", "Stump", "Swallow", "Swamp", "Sweet", "Tall", "Tip",
			"Torn", "Tuft", "Tumble", "Whirl", "Wild", "Lightning", "Odd", "Echo", "Bluff", "Cold", "Rumble",
			"Bloom", "Blossom", "Bubble", "Petal", "Ripple", "Yin", "Yang", "Blight", "Hollow", "Broken", "Blotch",
			"Dog", "Dead", "Kink"],

  black_prefixes: ["Black", "Grey", "Dark", "Slate", "Wool", "Down", "Mouse", "Lynx", "Otter", "Deer", "Faun", "Rat", "Mole",
			"Bat", "Sheep", "Rabbit", "Hare", "Shrew", "Vole", "Horse", "Beagle", "Terrier", "Badger", "Genet", 
			"Skunk", "Cow", "Crow", "Raven", "Magpie", "Starling", "Swift", "Dipper", "Rook", "Owl", "Duck", "Swan",
			"Quail", "Sparrow", "Wren", "Vulture", "Ant", "Spider", "Beetle", "Bee", "Hornet", "Leech", "Fly", "Cricket",
			"Slug", "Snail", "Wasp", "Lizard", "Snake", "Adder", "Serpent", "Cod", "Ray", "Piranha", "Aspen", "Holly",
			"Rose", "Stormy", "Charcoal", "Dusk", "Flint", "Ash", "Soot", "Cinder", "Boulder", "Onyx", "Coal", "Ink",
			"Bear", "Panda", "Buck", "Cobra", "Condor", "Eel", "Ermine", "Ferret", "Hen", "Rooster", "Midge", "Night",
			"Panther", "Seed", "Shade", "Stag", "Drake", "Dull", "Hound"],
  white_prefixes: ["White", "Ivory", "Pink", "Pale", "Glow", "Light", "Bright", "Clear", "Silk", "Cotton", "Wool", "Down", "Bone",
			"Stark", "Mouse", "Lemming", "Bilby", "Rat", "Sheep", "Rabbit", "Hare", "Mink", "Shrew", "Weasel", 
			"Stoat", "Horse", "Beagle", "Terrier", "Genet", "Skunk", "Cow", "Coati", "Magpie", "Dove", "Dipper", "Owl",
			"Goose", "Swan", "Cockatoo", "Cuckoo", "Gull", "Thrush", "Moth", "Tuna", "Salmon", "Aspen", "Birch",
			"Asphodel", "Cherry", "Daisy", "Dandelion", "Rose", "Yarrow", "Lily", "Fog", "Mist", "Dawn", "Hail", 
			"Milk", "Ice", "Snow", "Tundra", "Dew", "Flash", "Pearl", "Diamond", "Arctic", "Panda", "Crane", "Day",
			"Egret", "Ermine", "Ferret", "Finch", "Gander", "Gannet", "Hen", "Heron", "Laurel", "Lotus", "Morning",
			"Osprey", "Pidgeon", "Piper", "Plover", "Posy", "Silt", "Steam", "Stork", "Talon", "Thrift", "Vixen",
			"Gum", "Dull", "Fade", "Nacre", "Needle", "Ivy", "Briar", "Web", "Siam", "Foam", "Haze", "Hound"],
  grey_prefixes: ["Grey", "Silver", "Bone", "Light", "Squirrel", "Mouse", "Bilby", "Rat", "Mole", "Bat", "Rabbit", "Hare", 
			"Mink", "Vole", "Horse", "Terrier", "Genet", "Coati", "Raven", "Magpie", "Finch", "Owl", "Goose", 
			"Cuckoo", "Jay", "Gull", "Robin", "Wren", "Vulture", "Spider", "Moth", "Lizard", "Alligator", "Toad",
			"Minnow", "Tuna", "Tang", "Salmon", "Trout", "Comfrey", "Sloe", "Juniper", "Birch", "Asphodel",
			"Cherry", "Lily", "Fir", "Fog", "Rain", "Mist", "Dawn", "Hail", "Ice", "Tundra", "Pebble", "Rock",
			"Dust", "Dew", "Gravel", "Boulder", "Steel", "Pearl", "Pole", "Tin", "Asper", "Bass", "Borage",
			"Buck", "Burdock", "Carp", "Chive", "Cobra", "Condor", "Conifer", "Eel", "Elk", "Gill", "Heron",
			"Mistle", "Nettle", "Osprey", "Pidgeon", "Plover", "Kangaroo", "Steam", "Talon", "Wet", "Gum",
			"Dull", "Wire", "Nacre", "Gorse", "Heather", "Lichen", "Briar", "Web", "Python", "Mau", "Foam",
			"Haze"],
  cream_prefixes: ["Cream", "Pink", "Beige", "Yellow", "Tawny", "Fawn", "Pale", "Light", "Bright", "Mouse", "Lemming",
			"Deer", "Faun", "Rat", "Rabbit", "Hare", "Mink", "Shrew", "Stoat", "Camel", "Meerkat", "Jackal", 
			"Coyote", "Coati", "Cow", "Dove", "Hawk", "Owl", "Swan", "Jay", "Harrier", "Gull", "Thrush", "Eagle",
			"Bee", "Hornet", "Wasp", "Roach", "Frog", "Newt", "Minnow", "Pike", "Thyme", "Comfrey", "Privet",
			"Barley", "Hay", "Beech", "Sap", "Timber", "Tinder", "Acorn", "Nut", "Oat", "Wheat", "Rye", "Apple",
			"Wood", "Dandelion", "Marigold", "Pear", "Apricot", "Moss", "Rose", "Yarrow", "Tulip", "Dawn",
			"Pebble", "Rock", "Flash", "Sand", "Wax", "Topaz", "Banana", "Acacia", "Aspen", "Bass",
			"Buzzard", "Cheetah", "Cinnamon", "Copper", "Cougar", "Crab", "Crane", "Day", "Fennel", "Ferret",
			"Finch", "Flax", "Grass", "Hen", "Heron", "Jasper", "Laurel", "Locust", "Maggot", "Midge", "Morning",
			"Nettle", "Pea", "Pidgeon", "Posy", "Sage", "Silt", "Talon", "Warm", "Skin", "Worm", "Bumble", "Needle",
			"Ivy", "Bramble", "Briar", "Python", "Siam"],
  ginger_prefixes: ["Amber", "Ginger", "Orange", "Hazel", "Honey", "Fawn", "Glow", "Red", "Green", "Scarlet",
			"Crimson", "Bright", "Squirrel", "Mouse", "Lynx",  "Lemming", "Deer", "Faun", "Rat", "Rabbit", "Hare", "Mink", "Shrew", 
			"Stoat",  "Beagle", "Camel", "Jackal", "Coyote", "Coati", "Hawk", "Owl", "Duck",
			"Harrier", "Kite", "Quail", "Robin", "Eagle", "Ant", "Spider", "Beetle", "Bee", "Hornet", "Cricket", "Wasp",
			"Roach", "Lizard", "Komodo", "Turtle", "Frog", "Clown", "Pike", "Piranha", "Pine", "Thyme", "Comfrey",
			"Beech", "Barley", "Hay", "Sap", "Palm", "Elder", "Elm", "Acorn", "Nut", "Rye", "Apple", "Wood", 
			"Holly", "Dandelion", "Marigold", "Pear", "Plum", "Apricot", "Moss", "Rose", "Sorrel", "Lily",
			"Poppy", "Rock", "Dust", "Fire", "Cinder", "Spark", "Ember", "Scorch", "Ruby", "Topaz",
			"Rust", "Gold", "Golden", "Alder", "Acacia", "Almond", "Bass", "Blaze", "Brush", "Buck",
			"Cedar", "Chaffinch", "Cheetah", "Chestnut", "Cinnamon", "Copper", "Crab", "Dahlia",
			"Day", "Elk", "Ermine", "Fennel", "Ferret", "Finch", "Flax", "Grass", "Hen", "Rooster",
			"Jasper", "Kestrel", "Larch", "Locust", "Grasshopper", "Marten", "Mite", "Carrot", "Pheasant", "Kangaroo",
			"Sage", "Sedge", "Seed", "Stag", "Twig", "Vixen", "Warm", "Yew", "Drake", "Fern", "Clover", "Willow",
			"Python", "Hound"],
  brown_prefixes: ["Brown", "Tan", "Cocoa", "Russet", "Mocha", "Fawn", "Hazel", "Red", "Green", "Scarlet", "Crimson",
			"Squirrel", "Mouse", "Lynx", "Otter", "Deer", "Faun", "Rat", "Bat", "Rabbit", "Hare", "Mink", "Shrew", 
			"Vole", "Weasel", "Stoat", "Horse", "Beagle", "Jackal", "Coyote", "Hawk", "Dipper", "Parrot", "Owl",
			"Duck", "Jay", "Harrier", "Kite", "Quail", "Robin", "Sparrow", "Wren", "Eagle", "Vulture", "Ant",
			"Spider", "Beetle", "Hornet", "Leech", "Cricket", "Mantis","Turtle", "Gecko", "Frog", "Newt",
			"Toad", "Pike", "Cod", "Ray", "Piranha", "Pine", "Thyme", "Cypress", "Maple", "Rowan", "Timber", 
			"Tinder", "Coconut", "Palm", "Elder", "Elm", "Acorn", "Cactus", "Wood", "Log", "Pear", "Moss",
			"Reed", "Stormy", "Pebble", "Rock", "Dust", "Mud", "Emerald", "Rust", "Bronze", "Alder", "Algae",
			"Almond", "Basil", "Bear", "Beaver", "Buck", "Buzzard", "Carp", "Cedar", "Chestnut", "Cinnamon",
			"Clay", "Conifer", "Copper", "Eel", "Elk", "Ermine", "Fennel", "Ferret", "Finch", "Grouse", "Hickory",
			"Jasper", "Kestrel", "Larch", "Lark", "Locust", "Grasshopper", "Marten", "Mistle", "Osprey",
			"Parsley", "Partridge", "Pidgeon", "Plover", "Kangaroo", "Raccoon", "Sedge", "Seed", "Spruce", 
			"Stag", "Twig", "Vixen", "Yew", "Worm", "Drake", "Thistle", "Prickle", "Thorn", "Fern", "Clover", 
			"Gorse", "Heather", "Lichen", "Willow", "Ivy", "Bramble", "Briar", "Weed"],
  yellow_prefixes: ["Yellow", "Cream", "Beige", "Rat", "Rabbit", "Hare", "Camel", "Meerkat", "Bee", "Hornet", "Wasp", "Frog", 
			"Newt", "Toad", "Barley", "Hay", "Sap", "Oat", "Wheat", "Rye", "Apple", "Wood", "Marigold", "Pear", 
			"Apricot", "Rose", "Tulip", "Dawn", "Flash", "Spark", "Sand", "Wax", "Topaz", "Rust",  "Gold", "Golden", 
			"Banana", "Chaffinch", "Cheetah", "Cougar", "Day", "Maggot", "Morning", "Warm", "Bumble", "Drake",
			"Siam", "Daffodil", "Spider", "Orb", "Weaver", "Salamander", "Lichen", "Warbler", "Monarch", 
			"Lemon", "Duck", "Chick", "Butter", "Pollen", "Autumn", "Pepper", "Corn", "Pyrite", "Kiwi", "Mango",
			"Mustard", "Sulfur", "Bug", "Straw", "Pumpkin", "Bruise", "Egg", "Clown", "Koi"],
  blue_prefixes: ["Blue", "Ocean", "Sea", "Water", "Wet", "Rain", "Dew", "Beetle", "Parrot", "Pidgeon", "Gull", "Ant", 
			"Moth", "Snake", "Serpent", "Adder", "Turtle", "Frog", "Axolotl", "Tang",  "Comfrey",
			"Pansy", "Sloe", "Juniper", "Lavender", "Cactus", "Rose", "Stormy", "Hail", "Ice", "Mist", "Dusk", 
			"Dawn", "Lapis", "Ink", "Borage", "Iris", "Shade", "Wisteria", "Gorse", "Heather", "Lichen", "Mau", "Haze",
			"Blueberry", "Fire", "Jay", "Smoke", "Booby", "Hyacinth", "Neptune", "Uranus", "Tomato", "Egg", 
			"Peacock", "Kingfisher", "Macaw", "Jay", "Cray", "Lobster", "Betta", "Guppy", "Swallow", "Octopus",
			"Iguana", "Shark", "Whale", "Eel", "Puffer", "Slug", "Fly", "Sapphire", "Lungwort", "Warbler", "Dasher",
			"Aster", "Rot", "Mould", "Koi", "Sonic", "Hedgehog"],
  purple_prefixes: ["Purple", "Lilac", "Tomato", "Red", "Cherry", "Duck", "Pidgeon", "Ant", "Spider", "Beetle", "Fly", 
			"Slug", "Snail", "Betta", "Guppy", "Lizard", "Piranha", "Comfrey", "Lavender", "Apple", "Holly",
			"Pear", "Plum", "Rose", "Sorrel", "Lily", "Poppy", "Stormy", "Dust", "Flint", "Fire", "Cinder",
			"Ruby", "Cobra", "Crab", "Dahlia", "Gleam", "Hen", "Rooster",  "Kestrel", "Mallow", "Seed", 
			"Shade", "Drake", "Wisteria", "Orchid", "Petal", "Rose", "Dragon", "Aster", "Rice", "Blossom", 
			"Amethyst", "Artichoke", "Radish", "Asparagus", "Beetroot", "Current", "Basslet", "Bruise", "Rot",
			"Mould", "Carnation", "Clematis", "Mantis", "Coneflower", "Coral", "Crocus", "Eggplant", 
			"Elder", "Fig", "Fuchsia", "Grape", "Clown", "Koi", "Star", "Gleam"], 
  green_prefixes: ["Lime", "Green", "Grass", "Light", "Glow", "Parrot", "Duck", "Cricket", "Mantis", "Moth", "Stick", "Bug", 
			"Lizard", "Crocodile", "Alligator", "Snake", "Serpent", "Turtle", "Gecko", "Frog", "Newt", "Toad", "Thyme", 
			"Cactus", "Apple", "Holly", "Pear", "Moss", "Reed", "Mint", "Bird", "Algae", "Basil", "Bush", "Frond", "Gleam", 
			"Hickory", "Chive", "Conifer", "Fennel", "Locust", "Grasshopper", "Nettle", "Sage", "Sedge", "Spruce", 
			"Yew", "Prickle", "Thorn", "Thistle", "Fern", "Clover", "Aloe", "Gorse", "Heather", "Lichen", "Willow",
			"Ivy", "Bramble", "Briar", "Python", "Weed", "Pepper", "Celery", "Mustard", "Lettuce", "Marrow",
			"Zinnia", "Tanager", "Chameleon", "Parsley", "Macaw", "Caterpillar", "Mamba", "Dahlia", 
			"Iguana", "Egg", "Koi"], 

  pride_prefixes: {
        "AGENDER": ["Green", "Egg", "Agender", "Enby", "Fluid", "Lime", "Gleam", "Glow", "Parrot", "Grass", "Light", "Duck", "Cricket", 
            "Mantis", "Moth", "Stick", "Bug", "Lizard", "Crocodile", "Alligator", "Snake", "Serpent", "Turtle", "Gecko", 
            "Frog", "Newt", "Toad", "Thyme", "Cactus", "Apple", "Holly", "Pear", "Moss", "Reed", "Mint", "Bird", "Algae", "Basil", 
            "Bush", "Frond", "Gleam", "Hickory", "Chive", "Conifer", "Fennel", "Locust", "Grasshopper", "Nettle", "Sage", 
            "Sedge", "Spruce", "Yew", "Prickle", "Thorn", "Thistle", "Fern", "Clover", "Aloe", "Gorse", "Heather", "Lichen", "Willow",
            "Ivy", "Bramble", "Briar", "Python", "Weed", "Pepper", "Celery", "Mustard", "Lettuce", "Marrow",
            "Zinnia", "Tanager", "Chameleon", "Parsley", "Macaw", "Caterpillar", "Mamba", "Dahlia", "Iguana", "Koi", "Non", 
            "Ichi", "Ni", "San", "Shi", "Yon", "Go", "Roku", "Dark", "Banded", "Splashed"],
        "ENBY": ["Yellow", "Purple", "Enby", "Agender", "Dark", "White", "Striped", "Banded", "Bright", "Splashed", "Patched", "Splotch",
            "Painted", "Paint", "Light", "Fluid", "Non", "Ichi", "Ni", "San", "Shi", "Yon", "Go", "Roku", "Cream", "Beige", 
            "Rat", "Rabbit", "Hare", "Camel", "Meerkat", "Bee", "Hornet", "Wasp", "Frog", 
            "Newt", "Toad", "Barley", "Hay", "Sap", "Oat", "Wheat", "Rye", "Apple", "Wood", "Marigold", "Pear", 
            "Apricot", "Rose", "Tulip", "Dawn", "Flash", "Spark", "Sand", "Wax", "Topaz", "Rust",  "Gold", "Golden", 
            "Banana", "Chaffinch", "Cheetah", "Cougar", "Day", "Maggot", "Morning", "Warm", "Bumble", "Drake",
            "Siam", "Daffodil", "Spider", "Orb", "Weaver", "Salamander", "Lichen", "Warbler", "Monarch", 
            "Lemon", "Duck", "Chick", "Butter", "Pollen", "Autumn", "Pepper", "Corn", "Pyrite", "Kiwi", "Mango",
            "Mustard", "Sulfur", "Bug", "Straw", "Pumpkin", "Bruise", "Egg", "Clown", "Koi"],
        "ASEXUAL": ["Purple", "Black", "Grey", "Banded", "Touch", "Bristle", "Lilac", "Tomato", "Red", "Cherry", "Duck", 
            "Pidgeon", "Ant", "Spider", "Beetle", "Fly", "Slug", "Snail", "Betta", "Guppy", "Lizard", "Piranha", 
            "Comfrey", "Lavender", "Apple", "Holly", "Pear", "Plum", "Rose", "Sorrel", "Lily", "Poppy", "Stormy", "Dust", 
            "Flint", "Fire", "Cinder", "Ruby", "Cobra", "Crab", "Dahlia", "Gleam", "Hen", "Rooster",  "Kestrel", "Mallow", "Seed", 
            "Shade", "Drake", "Wisteria", "Orchid", "Petal", "Rose", "Dragon", "Aster", "Rice", "Blossom", 
            "Amethyst", "Artichoke", "Radish", "Asparagus", "Beetroot", "Current", "Basslet", "Bruise", "Rot",
            "Mould", "Carnation", "Clematis", "Mantis", "Coneflower", "Coral", "Crocus", "Eggplant", 
            "Elder", "Fig", "Fuchsia", "Grape", "Clown", "Koi", "Star", "Gleam"],
        "TRANS": ["Trans", "Blue", "Pink", "Light", "Blue", "Ocean", "Sea", "Water", "Wet", "Rain", "Dew", "Beetle",
            "Parrot", "Pidgeon", "Gull", "Ant", "Moth", "Snake", "Serpent", "Adder", "Turtle", "Frog", "Axolotl", "Tang", "Comfrey",
            "Pansy", "Sloe", "Juniper", "Lavender", "Cactus", "Rose", "Stormy", "Hail", "Ice", "Mist", "Dusk", 
            "Dawn", "Lapis", "Ink", "Borage", "Iris", "Shade", "Wisteria", "Gorse", "Heather", "Lichen", "Mau", "Haze",
            "Blueberry", "Fire", "Jay", "Smoke", "Booby", "Hyacinth", "Neptune", "Uranus", "Tomato", "Egg", 
            "Peacock", "Kingfisher", "Macaw", "Jay", "Cray", "Lobster", "Betta", "Guppy", "Swallow", "Octopus",
            "Iguana", "Shark", "Whale", "Eel", "Puffer", "Slug", "Fly", "Sapphire", "Lungwort", "Warbler", "Dasher",
            "Aster", "Rot", "Mould", "Koi", "Sonic", "Hedgehog", "Two", "Bi", "White", "Foam", "Steam"],
        "GAYBOW": ["Gay", "Rainbow", "Parrot", "Colour", "Bright", "Eyesore", "Shiny", "Fluid", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Long", "Short", "Fluff", "Fluffy", "Gleam", "Star", "Banded",
            "Striped", "Stripes", "Dazzle", "Light", "Vibrant", "Sky", "Aurora", "Wet", "Nacre", "Shell", "Plume",
            "Insect", "Ant", "Bird", "Axolotl", "Chrome", "Poly", "Rain", "Cloudy", "Dream", "Misc", "Stew", "Stone",
            "River", "Ripple", "Robin", "Ribbon", "Multi", "Flower", "Petal", "Lily", "Brocoli"]
  },
  
  albino_prefixes: ["Albino", "Blind", "White", "Nacre", "Plain", "Pink", "Pale", "Snow", "Yellow", "Blue", "Violet",
			"Ivory", "Bilby", "Rat", "Rabbit", "Hare", "Foam", "Haze", "Hound", "Gleam", "Bright", "Flash", "Blaze", "Spark", 
			"Pearl", "Arctic", "Frozen", "Ice", "Snow", "Shell", "Chalk", "Gum", "Milk", "Fog", "Mist", "Stark", "Cloudy",
			"Ripple", "Dove", "Bone", "Stork", "Crane", "Owl", "Gull", "Cow", "Light", "Hope", "Wish", "Diamond", "Web",
			"Wash", "Day", "Dapple", "Rose", "Needle", "Siam", "Dandelion", "Wisp", "Steam", "Foam", "Pidgeon", "Ghost",
			"Curse", "Stoat", "Weasel", "Rapid", "Bubble", "Shiny"],
  melanistic_prefixes: ["Cow", "Crow", "Melan", "Dust", "Ash", "Soot", "Black", "Dark", "Shade", "Shaded", "Cow", "Boar",
			"Night", "Rat", "Hound", "Mortis", "Ichor", "Raven", "Corvid", "Ant", "Beetle", "Flint", "Cinder", "Midnight",
			"Dusk", "Onxy", "Coal", "Snake", "Adder", "Spider", "Serpent", "Charcoal", "Ink", "Void", "Panther", "Shrew",
			"Vole", "Eel", "Edge", "Cliff", "Cave", "Stormy", "Road", "Asphalt"],
  sphynx_prefixes: ["Sphynx", "Bare", "Bald", "Salmon", "Pink", "Light", "Bone", "Thin", "Small", "Rat", "Gremlin",
			"Rat", "Mouse", "Flax", "Splashed", "Patched", "Cold", "Bat", "Vulture", "Hope", "Wish", "Scratch", "Boney", 
			"Twig", "Stick", "Film", "Fade", "Faded", "Spirit", "Dapple", "Mottled", "Needle", "Ghost", "Shiny", "Sleek",
			"Kink", "Hairless", "Hippo", "Mole", "Pig", "Rabbit", "Hare", "Cavy", "Light", "Bright", "Slim", "Short", "Long",
			"Tall", "Cream", "Fawn", "Faun", "Sap", "Tinder", "Sage", "Lily", "Orchid", "Sand", "Wax", "Topaz", "Melt", 
			"Crab", "Shell", "Nacre", "Shiny", "Mew"],
  wing_prefixes: ["Crow", "Raven", "Magpie", "Hawk", "Finch", "Starling", "Swift", "Dipper", "Parrot", "Owl", "Goose", 
			"Duck", "Jay", "Gull", "Quail", "Vulture", "Ant", "Spider", "Beetle", "Leech", "Fly", "Moth", "Bird",
			"Harrier", "Condor", "Hen", "Plume", "Sparrow", "Lark", "Hummer", "Humming", "Starling", "Pidgeon", "Fluff", 
			"Fluffy", "Cloudy", "Prince", "Sky", "Aero", "Osprey", "Partridge", "Vulture", "Shrike", "Penguin", 
			"Toucan", "Winged", "Blue", "Chicken", "Rooster", "Finch", "Falcon", "Robin", "Crane", "Quail", "Turkey", "Night", 
			"Gale", "Nightingale", "Mallard", "Woodpecker", "Cuckoo", "Pelican", "Gull", "Bat", "Fruit", "Fisher", "Warbler",
			"Stork", "Goldfinch", "Gold", "Swan", "Grace"],
  
  loner_names: [
    "Abyss", "Ace", "Adam", "Admiral", "Aether", "Agatha", "Ah", "Ah ha", "Agent Smith", "Akilah", "Alba", "Albedo", "Alcina", "Alec", "Alexa", "Alfie", 
    "Alfredo", "Alice", "Alma", "Alonzo", "Alphys", "Amani", "Amari", "Amaya", "Amber", "Amelia", "Amigo", "Amir", "Amity", "Amor", 
    "Amy", "Angel", "Anita", "Anubis", "Apple Cider", "April", "Apu", "Aquarius", "Archie", "Aries", "Armageddon", "Armin", "Asgore", 
    "Ash", "Aspen", "Asriel", "Aurora", "Ava", "Avellana", "Azula", "Baba Yaga", "Baby", "Bagel", "Bagheera", "Bailey", "Baisel", "Baliyo", 
    "Bamboo", "Bandit", "Banshee", "Banzai", "Baphomet", "Basil", "Bastet", "Bean", "Beanie Baby", "Beanie", "Beans", "Bebe", "Bede", "Beef Stroganoff", 
    "Bella", "Belle", "Bellini", "Ben", "Benito", "Benny", "Bentley", "Berlioz", "Beverly", "Bibelot", "Big Man", "Bigwig", "Bill Bailey", 
    "Binx", "Birb", "Birdie", "Bixby", "Blair", "Blinky Stubbins", "Blitzo", "Blu", "Bluebell", "Bologna", "Bolt", "Bombalurina", "Bombon",
    "Bonbon", "Bongo", "Boni", "Bonnie", "Bonny", "Boo", "Booker", "Boots", "Brandywine", "Bren", "Brioche", "Broccoli", "Brooklyn", "Bub", "Buchito", 
    "Buddy", "Buffy", "Bullwinkle", "Bumblebee", "Bunga", "Bunny", "Burger", "Burm", "Bustopher Jones", "Buttercup", "Butternut", 
    "Butterscotch", "Caesar", "Cake", "Calamari", "Callie", "Calvin", "Camouflage", "Cancer", "Candy", "Canela", "Cannelloni", "Capricorn", "Captain", 
    "Caramel", "Cardamom", "Cardboard", "Carmen", "Carmin", "Carolina", "Caroline", "Carrie", "Cashmere", "Cassandra", "Catalina", "Catie", "Catrick", 
    "Catty", "Cauliflower", "Cayenne", "Cece", "Celeste", "Cerberus", "Chai", "Chance", "Chanel", "Chansey", "Chanterelle", "Chaos", 
    "Chara", "Charles", "Charlie", "Charlotte", "Charm", "Chase", "Cheese", "Cheesecake", "Cheeto", "Cheetoman", "Chef", "Cherry", "Cheshire", 
    "Chester", "Chewie", "Chewy", "Chica", "Chicco", "Chickpea", "Chief", "Chinook", "Chip", "Chiquito", "Chispa", "Chloe", "Chocolate Chip", "Chocolate", 
    "Chorizo", "Chris", "Chrissy", "Chub", "Churro", "Cielo", "Cilantro", "Cinder", "Cinderblock", "Cinnabon", "Clawdette", "Clementine", "Clicker", "Cloe", "Cloud", 
    "Clover", "Cobweb", "Cocoa Puff", "Cocoa", "Coffee", "Cola", "Colby Jack", "Conan", "Confetti", "Cookie", "Cooper", "Coquito", 
    "Coral", "Coriander", "Coricopat", "Cosmo", "Cowbell", "Cowboy", "Crab", "Cracker", "Cream", "Crema", "Crescent", "Crispy", "Crow", 
    "Crumpet", "Crunchwrap", "Crunchy", "Cupcake", "Curry", "Cutie", "Cyprus", "Daisy Mae", "Dakota", "Dali", "Daliah", "Dan", 
    "Dandelion", "Danger Dave", "Dave", "Deli", "Delilah", "Della", "Demeter", "Destiny", "Dewey", "Diablo", "Digiorno", "Dinah", 
    "Diona", "Dirk", "Distinguished Gentleman", "Dizzy", "Dog", "Dolly", "Domingo", "Donald", "Donuts", "Doofenshmirtz", "Dori", "Dorian", "Dorothy", "Double Trouble", 
    "Dova", "Dragonfly", "Dreamy", "Duchess", "Dulce", "Dumpling", "Dune", "Dunnock", "Dust Bunny", "Dusty Cuddles", "Eclipse", "Eda", 
    "Eddie", "Eepy", "Eevee", "Egg", "Elden", "Elijah", "Ellie", "Elton", "Ember", "Emeline", "Emerald", "Emi", "Emilio", "Emma", "Emy", "Enchilada", "Erebus", 
    "Erica", "Esme", "Espresso", "Esther", "Eva", "Eve", "Evelyn", "Evie", "Evilface", "Ezra", "Fallow", "Fang", "Fawn", "Feather", 
    "Felix", "Feliz", "Fern", "Ferret", "Ferry", "Fig", "Figaro", "Finch", "Finnian", "Fireball", "Firecracker", "Firefly", "Fishleg", "Fishtail", "Fiver", "Flabby", 
    "Flamenco", "Flower", "Fluffy", "Flutie", "Fork", "Foxtrot", "Frank", "Frankie", "Frannie", "Fred", "Freddy", "Free", 
    "French Fry", "French", "Frisk", "Frito", "Froggy", "Frumpkin", "Fry", "Frye", "Fudge", "Fuli", "Fuzziwig", "Gabriel", "Galahad", 
    "Gamble", "Garfield", "Gargoyle", "Garnet", "Gato", "Gemelli", "Gemini", "General Erasmus Dickinson", "Geode", "George", "Ghost", 
    "Gibby", "Gilded Lily", "Gingersnap", "Gir", "Gizmo", "Glass", "Glory", "Gnocchi", "Gofrette", "Goldfish", "Good Sir", "Goose", "Goryo", "Grace", "Grain", "Grasshopper", 
    "Grave", "Gravy", "Grizabella", "Guillermo", "Guinness", "Gumbo", "Guppy", "Gus", "Gust", "Gwendoline", "Gwyndolin", "Gwynn", "Gyoza", "Habanero", 
    "Haiku", "Haku", "Hamburger", "Hantu", "Harlequin", "Haru", "Harvest", "Harvey", "Havoc", "Hawkbit", "Hawkeye", "Hazel", "Heathcliff", "Heisenberg", "Henry", "Herbert", "Herc", 
    "Hercules", "Hershey", "Hex", "Hiccup", "Hickory", "Highness", "Hlao", "Hobbes", "Hocus Pocus", "Holly", "Honda", "Honeydew", "Hop", 
    "Hot Sauce", "Hotdog", "Howler", "Hubert", "Hughie", "Human", "Humphrey", "Hunter", "Ice Cube", "Ice", "Icecube", "Icee", "Igor", "Ike", "Indi", 
    "Inigo", "Insect", "Ipsy", "Isabel", "Isaiah", "Israel", "Itsy Bitsy", "Jack", "Jade", "Jaiden", "Jake", "James", "Jasmine", "Jasper", "Jaxon", "Jay", "Jaylen", 
    "Jeep Wrangler", "Jelly Jam", "Jellylorum", "Jenny", "Jennyanydots", "Jesse", "Jessica", "Jester", "Jethro", "Jetta", "Jewel", 
    "Jewels", "Jigsaw", "Jiminy Cricket", "Jimmy", "Jinn", "Jinx", "John", "Johnny", "Joker", "Jolly Rancher", "Jolly", "Joob", "Jubie", 
    "Judas", "Jude", "Judy", "Juliet", "June", "Jupiter", "Kale", "Kaleb", "Kasi", "Kate", "Katjie", "Katy", "KD", "Kelloggs", "Ken", 
    "Kendra", "Kenny", "Kermit", "Kerry", "Ketchup", "Ketsl", "Kettlingur", "Keziah", "Kiara", "Kianna", "Kibble", "Kimani", "King", "Kingston", "Kion", 
    "Kip", "Kisha", "Kitty Cat", "Kitty Softpaws", "Kitty", "Kiwi", "Klee", "Klondike", "Knox", "Kodiak", "Kokomi", "Kong", "Kovu", 
    "Kyle", " L ", "Lacy", "Lady Figment", "Lady Liberty", "Lady", "Laila", "Lakota", "Laku", "Larch", "Lark", "Leche", "Lee", "Leif", "Lemmy", "Lemon", 
    "Leo", "Leon", "Lester", "Levi", "Levon", "Lex", "Libra", "Lil Baby", "Lilac", "Lilith", "Lily", "Linden", "Linguine", "Little Lady", "Little Nicky", "Little One", 
    "Loaf", "Lobster", "Loca", "Loki", "Lola", "Lollipop", "London", "Loona", "Lora", "Lorado", "Louie", "Louis", "Loyalty", "Luchasaurus", "Luci-Purr", "Lucia", 
    "Lucky", "Lucy", "Lugnut", "Luigi", "Lulu", "Lumine", "Luna", "Lupo", "Luz", "Lydia", "Mabel", "Macaroon", "Macavity", "Maddy", 
    "Madi", "Maggie", "Magic", "Maize", "Majesty", "Makini", "Makwa", "Maleficent", "Malia", "Malik", "Manda", "Mange", "Mango", 
    "Mangosteen", "Mani", "Marathon", "Marceline",
    "Mare", "Marie", "Mario", "Mariposa", "Marny", "Martini", "Matador", "Matcha", "Maverick", "Max", "May", "Maya", "McChicken", 
    "McFlurry", "Meatloaf", "Meatlug", "Medusa", "Melody", "Melon", "Meow-Meow", "Meowyman", "Mera", "Mercedes", "Mercy", "Merlot", "Merry", "Mew", "Mick", "Midnight Goddess", "Miles", 
    "Milhouse", "Milky Way", "Millie", "Milo", "Milque", "Mimi", "Minette", "Mini", "Minna", "Minnie", "Mint", "Minty", "Miriam", "Miso", "Missile Launcher", "Misty", 
    "Mitaine", "Mitski", "Mitsubishi", "Mittens", "Mitzy Moo Moo", "Mocha", "Mochi", "Mojito", "Mojo", "Mollie", "Molly Murder Mittens", "Molly", "Monika", "Monster", "Monte", 
    "Monzi", "Moon", "Mop", "Mora", "Morel", "Morbius", "Morphius", "Moxie", "Mr. Anderson", "Mr. Kitty Whiskers", "Mr. Kitty", "Mr. Mistoffolees", "Mr. Whiskers", 
    "Mr. Wigglebottom", "Mucha", "Mufasa", "Muffet", "Mullido", "Mungojerrie", "Munkustrap", "Murder", "Mushroom", "Myko", "Nadia", 
    "Nagi", "Nakala", "Nakeena", "Nala", "Naomi", "Neel", "Neil", "Nemo", "Nessie", "Nevaeh", "Nick", "Nightmare", "Nikki", 
    "Niles", "Nine", "Ninja", "Nintendo", "Nirvana", "Nisha", "Nissan", "Neo", "Nitro", "Noche", "Noelle", "Noir", "Noodle", "Nori", "Norman", 
    "Nottingham", "Nova", "Nugget", "Nuggets", "Nuka", "Nutella", "Nutmeg", "O'Leary", "Oakley", "Oapie", "Obi Wan", "October", 
    "Odetta", "Old Deuteronomy", "Old Man Sam", "Oleander", "Olga", "Oliva", "Oliver", "Ollie", "Omelet", "Omen", "Onion", "Onyx", 
    "Oops", "Oopsy Dazey", "Ophelia", "Orchard", "Oregano", "Oreo", "Orion", "Orzo", "Oscar", "Otto", "Owen", "Pablo", "Paella", 
    "Paimon", "Paloma", "Pancake", "Pancho", "Pangur", "Panini", "Paprika", "Papyrus", "Paquito", "Patience", "Paulina", "Pawmi", "Peach", 
    "Peanut Wigglebutt", "Peanut", "Pear", "Pearl", "Pecan", "Penny", "Peony", "Pepita", "Pepper", "Pepsi", "Pequeno", "Perry", "Petya", "Phantom", "Pichi", "Pickles", "Pierre", "Piggy",
    "Pikachu", "Ping Pong", "Ping", "Pip", "Piper", "Pipkin", "Pipsqueak", "Pisces", "Pixel", "Pina Colada", "Plato", "Pochito", "Pocket", "Poe", "Poki", "Polly",
    "Pong", "Ponyboy", "Poopy", "Porsche", "Potato", "Pouncival", "President", "Prickle", "Princess", "Private Eye", "Pudding", 
    "Pumba", "Pumpernickel", "Pumpkin", "Punk", "Purdy", "Purry", "Pushee", "Puzzle", "Quagmire", "Quake", "Qubo", "Queen", "Queenie", "Queeny", "Querida", 
    "Quesadilla", "Queso Ruby", "Queso", "Quest", "Quickie", "Quimby", "Quinn", "Quino", "Quinzee", "Radar", "Rafael", "Rafiki", "Ramble", "Ramen", "Randy", 
    "Rani", "Raptor", "Rapunzel", "Rarity", "Rat", "Raven", "Ravioli", "Ray", "Reese", "Reeses Puff", "Ren", "Rhianna", "Rhubarb", "Rice",
    "Rico", "Rigatoni", "Rio", "Riot", "Risa", "River", "Riya", "Rizz", "Robbie", "Rocket", "Rodeo", "Rolo", "Roman", "Roomba", "Rooster", 
    "Rory", "Rose", "Roselie", "Rosewood", "Ruby", "Rudolph", "Rue", "Ruffnut", "Rufus", "Rum Tum Tugger", "Rum", "Rumpleteazer", 
    "Runt", "Russel", "Sable", "Sadie", "Saffron", "Sagittarius", "Sagwa", "Sailor", "Saki", "Sakura", "Salem", "Salmon", "Salt", "Sam", "Samantha", 
    "Sanai", "Sandwich", "Sandy", "Sangria", "Sans", "Sarabi", "Sarafina", "Sarge", "Sashimi", "Sassy", "Sausage", "Savannah",
    "Runt", "Russel", "Sable", "Sadie", "Saffron", "Sagittarius", "Sagwa", "Samus", "Sailor", "Saki", "Sakura", "Salem", "Salmon", "Salt", "Sam", "Samantha", 
    "Sanai", "Sandwich", "Sandy", "Sangria", "Sans", "Sarabi", "Sarafina", "Sarge", "Sashimi", "Sassy", "Sausage", "Savannah", 
    "Scarecrow", "Schmidt", "Scorpio", "Scotch", "Scrooge", "Seamus", "Sega", "Sekhmet", "Serenity", "Sergei", "Sergio", "Seri", "Seven", "Seven Of Nine",
    "Shaka", "Shamash", "Shampoo", "Shamwow", "Shani", "Shay", "Shenzi", "Sherman", "Shiloh", "Shimmer", "Shiver", "Sillabub", "Silly", 
    "Silva", "Silver", "Simba", "Simone", "Siri", "Sirius", "Skimbleshanks", "Skittles", "Skrunkly", "Skylar", "Slinky", "Sloane", 
    "Slug", "Slushie", "Smarty Pants", "Smoothie", "Smores", "Sneakers", "Snek", "Snook", "Snook", "Snoots", "Snotlout", "Socks", "Soda Pop", "Sofa", 
    "Sofrito", "Sol", "Sonata", "Sonnet", "Sonic", "Sookie", "Sophie", "Sorbet", "Sox", "Spam", "Sparky", "Speedwell", "Spicy", "Spinach", "Spots", "Siracha", "Stan", 
    "Star", "Starfish", "Stella", "Steve", "Steven", "Stinkbutt", "Stinky", "Stolas", "Strawberry", "Stripes", "Subaru", "Sucrose", "Sueno",
    "Sugar", "Sundae", "Sunflower", "Sunny", "Sunset", "Sushi", "Sweet Creature", "Sweet Leon", "Sweet Marmalade", "Sweet", "Sweetie", 
    "Sylvester", "Tabasco", "Tabatha", "Tabby", "Tabbytha", "Taco Bell", "Taco", "Taffy", "Talia", "Tamagotchi", "Tamale", 
    "Tantomile", "Tasha", "Taurus", "Tay", "Tazama", "Teacup", "Teddie", "Tempest", "Tesla", "Tesora", "Tetris", "Teufel", "Theo", 
    "Thor", "Thumbelina", "Thyme", "Tiana", "Tigger", "Tikka", "Timmy", "Timon", "Tin Man", "Tiny", "Toast", "Toastee", "Toffee", "Tofu", "Tom", "Tomato Soup", "Tomato", "Toni", 
    "Toothless", "Top Hat", "Toriel", "Toro", "Torque", "Tortellini", "Tortilla", "Toulouse", "Toyota", "Treasure", "Trick", "Trinity", "Trinket", "Trip", "Triscuit", "Trixie", "Trouble Nuggets", 
    "Trouble", "Troublemaker", "Tucker", "Tuffnut", "Tumble", "Tumblebrutus", "Turbo", "Twilight", "Twinkle Lights", "Twister", "Twix", "Ula", "Ulyssa", "Undyne", "Union", 
    "Uriel", "Valente", "Valentino", "Van Pelt", "Vanilla", "Vaxx", "Velociraptor", "Venti", "Venture", "Via", "Victor", "Victoria", 
    "Vida", "Viktor", "Vinnie", "Vinyl", "Violet", "Virgo", "Vivienne", "Void", "Volkswagen", "Voltage", "Vox", "Waffle", "Wagyu", "Walnut", "Wanda", "Warren Peace", "Wasabi", "Webby", "Wednesday", 
    "Wendy", "Whiskers", "Whiskey", "Whisper", "Whiz Kid", "Wiggity Wacks", "Wigglebutt", "Windy", "Wishbone", "Wisp", "Wisteria", 
    "Wolverine", "Wonder", "Worm", "X'ek", "Xelle", "Yaoyao", "Yeet", "Yeeted", "Yen", "Yeza", "Yote", "Yooted", "Yokai", "Yoshi", "Yuca", "Yuki", "Zari", "Zariah", "Zazu", "Zelda", "Zim", "Zion", "Zira", "Ziti", "Zoe", "Zorro" 
    ]

    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 skin=None,
                 eyes=None,
                 pelt=None,
                 tortiepattern=None):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        
        # Set prefix
        if prefix is None:
            possible_prefix_categories = []
            if colour is not None:
                if colour in black_colours:
                    possible_prefix_categories.append(black_prefixes)
                elif colour in grey_colours:
                    possible_prefix_categories.append(grey_prefixes)
                elif colour in white_colours:
                    possible_prefix_categories.append(white_prefixes)
                elif colour in ginger_colours:
                    possible_prefix_categories.append(ginger_prefixes)
                elif colour in brown_colours:
                    possible_prefix_categories.append(brown_prefixes)                   
                elif colour in cream_colours:
                    possible_prefix_categories.append(cream_prefixes)
                elif colour in yellow_colours:
                    possible_prefix_categories.append(yellow_prefixes)
                elif colour in green_colours:
                    possible_prefix_categories.append(green_prefixes)                    
                elif colour in blue_colours:
                    possible_prefix_categories.append(blue_prefixes)
                elif colour in purple_colours:
                    possible_prefix_categories.append(purple_prefixes)
                elif colour in pride_colours:
                    possible_prefix_categories.append(pride_prefixes[colour]) 
            if skin is not None:
                if skin in albino_sprites:
                    possible_prefix_categories.append(albino_prefixes)
                elif skin in melanistic_sprites:    
                    possible_prefix_categories.append(melanistic_prefixes)
                elif skin in sphynx:    
                    possible_prefix_categories.append(sphynx_prefixes)
                elif skin in wings:    
                    possible_prefix_categories.append(wing_prefixes)
            # Choose appearance-based prefix if possible and named_after_appearance because True.
            if possible_prefix_categories:
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(normal_prefixes)
                    
        # Set suffix
        while self.suffix is None or self.suffix == self.prefix.casefold() or str(self.suffix) in \
                self.prefix.casefold() and not str(self.suffix) == '':
            if pelt is None or pelt == 'SingleColour':
                self.suffix = random.choice(normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3) # Chance for True is '1/8'.
                # Pelt name only gets used if there's an associated suffix.
                possible_suffix_categories = []
                if named_after_pelt:
                    possible_suffix_categories.append(normal_suffixes)
                    if pelt in tabbies:
                        possible_suffix_categories.append(tabby_suffixes)
                    elif pelt in spotted:
                        possible_suffix_categories.append(spotted_suffixes)
                    elif pelt in exotic:
                        possible_suffix_categories.append(exotic_suffixes)
                    elif pelt in torties:
                        possible_suffix_categories.append(tortie_suffixes)
                    elif skin in sphynx:    
                        possible_suffix_categories.append(sphynx_suffixes)     
                    elif skin in magic_kitty:    
                        possible_suffix_categories.append(magic_suffixes)   
                if possible_suffix_categories:    
                    suffix_category = random.choice(possible_suffix_categories)
                    self.suffix = random.choice(suffix_category)
                else:
                    self.suffix = random.choice(normal_suffixes)

        if self.suffix:
            possible_three_letter = (self.prefix[-2:] + self.suffix[0], self.prefix[-1] + self.suffix[:2])

            if all(i == possible_three_letter[0][0] for i in possible_three_letter[0]) or \
                    all(i == possible_three_letter[1][0] for i in possible_three_letter[1]):
                triple_letter = True

                MAX_ATTEMPT = 3
                while triple_letter and MAX_ATTEMPT > 0:
                    self.suffix = random.choice(normal_suffixes)
                    possible_three_letter = (self.prefix[-2:] + self.suffix[0], self.prefix[-1] + self.suffix[:2])    
                    if all(i == possible_three_letter[0][0] for i in possible_three_letter[0]) or \
                            all(i == possible_three_letter[1][0] for i in possible_three_letter[1]):
                        pass
                    else:
                        triple_letter = False
                MAX_ATTEMPT -= 1


    def __repr__(self):
        if self.status in special_suffixes:
            return self.prefix + special_suffixes[self.status]
        else:
            return self.prefix + self.suffix

names = Name()
