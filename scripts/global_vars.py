import pygame
import pygame_gui
from bidict import bidict
pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json')

MANAGER.get_theme().load_theme('resources/buttons.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')

import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()


def sort_bidict(d: bidict, first_element=None):
    """Sorts Dictionary alphbetically. If None if in the dictionary, always have that first. """

    temp = bidict({})
    if first_element in d:
        temp[first_element] = d[first_element]
        del d[first_element]

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    temp.update(sorted_dict)
    return temp


pelt_options = bidict({"SingleColour": "Plain",  "Smoke": "Smoke", 'Backed': "Stripe Backed", 'Tabby': "Tabby",
                       'Ticked': "Ticked Tabby", 'Mackerel': "Mackerel Tabby", 'Classic': "Classic Tabby",
                       'Sokoke': 'Sokoke', 'Agouti': "Agouti", "Speckled": "Speckled Tabby", "Rosette": "Rosette",
                       "Bengal": "Bengal", "Marbled": "Marbled Tabby", "Merle": "Merle", "Snowflake": "Snowflake", "Mottled": "Mottled",
                       "Ghost": "Ghost Tabby", "Doberman": "Doberman Point", "Skitty": "Skitty", "Rat": "Rat", 
                       "Wolf": "Wolf", "Skele": "Skeleton", "Stain": "Stain", "Charcoal": "Charcoal Tabby", "Hooded": "Hooded Tabby", 
                       "Ponit": "Bleach Point", "Spirit": "Ghostly Spirit"})
pelt_options = sort_bidict(pelt_options)

tortie_patches_patterns = bidict({"single": "Plain", "tabby": "Tabby", "bengal": "Bengal", "marbled": "Marbled Tabby",
                                  "ticked": "Ticked Tabby", "rosette": "Rosette", "smoke": "Smoke",
                                  "speckled": "Speckled Tabby", "agouti": "Agouti", "classic": "Classic Tabby",
                                  "mackerel": "Mackerel Tabby", "sokoke": "Sokoke", "merle": "Merle", "ghost": "Ghost Tabby", 
                                  "snowflake": "Snowflake", "mottled": "Mottled", "backed": "Stripe Backed", "doberman": "Doberman Point", 
                                  "skitty": "Skitty", "rat": "Solid Rat", "wolf": "Wolf", "skele": "Skeleton", "stain": "Stain", 
                                  "charcoal": "Charcoal Tabby", "hooded": "Charcoal Hooded Tabby", "ponit": "Bleach Point", 
                                  "spirit": "Ghostly Spirit"})
tortie_patches_patterns = sort_bidict(tortie_patches_patterns)

tortie_patches_shapes = bidict({"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                'DELILAH': "Delilah", 'MINIMAL1': "Minimal 1", 'MINIMAL2': "Minimal 2",
                                'MINIMAL3': "Minimal 3", 'MINIMAL4': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige", 
                                'COMBO': "Combo", 'BLENDED': "Blended", 'SCATTER': "Scatter", 'LIGHT': "Light", 
                                'BROKENONE': "Broken One", 'BROKENTWO': "Broken Two", 'BROKENTHREE': "Broken Three", 
                                'BROKENFOUR': "Broken Four", 'GLITCH': "Glitch", 'WAVE': "Wave", 'STRIPESMASK': "Stripes Mask", 
                                'KOI': "Koi", 'SKULL': "Skull", 'LITTLE': "Little", 'O': "O", 'TOADSTOOL': "Toadstool",
                                'PONITMASK': "Point Mask", 'SPOTSCHAOS': "Spots of Chaos", 'FOG': "Fog", 'SUNSET': "Sunset", 
                                'TAIL': "Tail", 'MOON': "Moon"})
tortie_patches_shapes = sort_bidict(tortie_patches_shapes)

eye_colors = bidict( {'YELLOW': "Yellow", 'AMBER': "Amber", 'HAZEL': "Hazel", 'PALEGREEN': "Pale Green",
                      'GREEN': "Green", 'BLUE': "Blue", 'DARKBLUE': "Dark Blue", 'GREY': "Grey", 'CYAN': "Cyan",
                      'EMERALD': "Emerald", 'PALEBLUE': "Pale Blue", 'VOID': "Void", 'GHOST': "Ghost",
                      'PALEYELLOW': "Pale Yellow", 'GOLD': "Gold", 'HEATHERBLUE': "Heather Blue", 'COPPER': "Copper", 
                      'SAGE': "Sage", 'BLUE2': "Blue 2", 'SUNLITICE': "Sunlit Ice", "GREENYELLOW": "Green-Yellow",
                      'POPPY': "Poppy", 'CRIMSON': "Crimson", 'RUBY': "Ruby", 'BROWN': "Brown", 'EMERALD2': "Emerald 2", 
                      'SKY': "Sky Blue", 'LILAC': "Lilac", 'BROWN2': "Brown 2", 'PEANUT': "Peanut", 'GREY2': "Grey 2", 
                      'YELLOWOLIVE': "Yellow-Olive", 'SUNSHINE': "Sunshine", 'AZURE': "Azure", 'COBOLT': "Cobolt", 
                      'GRASS': "Grass", 'MINT': "Mint", 'LILACGREY': "Lilac Grey", 'WHITE': "White", 'VIOLET': "Violet", 
                      'GRAPE': "Grape", 'INDIGO': "Indigo", 'PRIMARY': "Primary", 'PRIMARY2': "Primary 2", 
                      'PRIMARY3': "Primary 3", 'CHROME': "Chrome", 'CHROME2': "Chrome 2", 'CHROME3': "Chrome 3", 'RBG': "RGB", 
                      'RBG2': "RGB 2", 'RBG3': "RGB 3", 'MONOCHROME': "Monochrome", 'MONOCHROME2': "Monochrome 2", 
                      'MONOCHROME3': "Monochrome 3", 'POPPY2': "Poppy 2", 'STRAWBERRY': "Strawberry", 'MINTCHOC': "Mint-Choc", 
                      'CHOCMINT': "Choc-Mint", 'AMBER2': "Amber 2", 'BEACH': "Beach", 'NACRE': "Nacre", 'NIGHT': "Night", 
                      'OCEAN': "Ocean"})
eye_colors = sort_bidict(eye_colors)

tints = bidict({"none": "None", }) #, "pink": "Pink", "gray": "Gray", "red": "Red", "black": "Black", "orange": "Orange",
                #"yellow": "Yellow", "purple": "Purple", "blue": "Blue"
tints = sort_bidict(tints, 'none')

white_patches_tint = bidict({"none": "None", "darkcream": "Dark Cream", "cream": "Cream", "offwhite": "Blue",
                             "gray": "Gray", "pink": "Pink", "bluewhite": "Blue White", "mint": "Mint", "black": "Black", 
                             "midnight": "Midnight Blue", "scarlet": "Scarlet Red", "starkit": "Vibrant Purple", 
                             "sunshine": "Sunshine"})

skin_colors = bidict({'BLACK': "Black", 'RED': "Red", 'PINK': "Pink", 'DARKBROWN': "Dark Brown", 'BROWN': "Brown",
                      'LIGHTBROWN': "Light Brown", 'DARK': "Dark", 'DARKGREY': "Dark Gray", 'GREY': "Gray",
                      'DARKSALMON': "Dark Salmon", 'SALMON': 'Salmon', 'PEACH': 'Peach', 'DARKMARBLED': 'Dark Marbled',
                      'MARBLED': 'Marbled', 'LIGHTMARBLED': 'Light Marbled', 'DARKBLUE': 'Dark Blue', 'BLUE': 'Blue',
                      'LIGHTBLUE': 'Light Blue', 'XANADU': "Xanadu", 'BLACKGILL': "Black Gills", 'REDGILL': "Red Gills", 
                      'PINKGILL': "Pink Gills", 'DARKBROWNGILL': "Dark Brown Gills", 'BROWNGILL': "Brown Gills", 
                      'LIGHTBROWNGILL': "Light Brown Gills", 'DARKGILL': "Dark Gills", 'DARKGREYGILL': "Dark Grey Gills", 
                      'GREYGILL': "Grey Gills", 'DARKSALMONGILL': "Dark Salmon Gills", 'SALMONGILL': "Salmon Gills", 
                      'PEACHGILL': "Peach Gills", 'DARKMARBLEDGILL': "Dark Marbled Gills", 'MARBLEDGILL': "Marbled Gills", 
                      'LIGHTMARBLEDGILL': "Light Marbled Gills", 'DARKBLUEGILL': "Dark Blue Gills", 'BLUEGILL': "Blue Gills", 
                      'LIGHTBLUEGILL': "Light Blue Gills", 'XANADUGILL': "Xanadu Gills", 'ALBINOPINK': "Pink Albino", 
                      'ALBINOBLUE': "Blue Albino", 'ALBINORED': "Red Albino", 'ALBINOVIOLET': "Violet Albino", 
                      'ALBINOYELLOW': "Yellow Albino", 'ALBINOGREEN': "Green Albino", 'MELANISTICLIGHT': "Melanistic(No Eyes)", 
                      'MELANISTIC': "Melanistic", 'MELANISTICDARK': "Melanistic(Shadowed Eyes)", 'FIRE': "Fire Magic", 'WATER': "Water Magic", 
                      'EARTH': "Earth Magic", 'WIND': "Wind Magic", 'STAR': "Star Magic", 'STEAM': "Steam Magic", 'MAGMA': "Magma Magic", 
                      'SMOKE': "Smoke Magic", 'HELL': "Hell Magic", 'MUD': "Mud Magic", 'STORM': "Storm Magic", 'BLOOD': "Blood Magic", 
                      'SAND': "Sand Magic", 'BERRY': "Berry Magic", 'GHOST': "Ghost Magic", 'WHITEWING': "White Winged", 
                      'BLUEGREENWING': "Blue-Green Winged", 'REDWING': "Red Winged", 'PURPLEFADEWING': "Purple-Fade Winged", 
                      'RAINBOWWING': "Rainbow Winged", 'SILVERWING': "Silver Winged", 'STRAKITWING': "Starkit Winged", 
                      'SONICWING': "Sonic-Blue Winged", 'MEWWING': "Mew Winged", 'OLIVEWING': "Olive Winged", 'GREENWING': "Green Winged", 
                      'GREYWING': "Grey Winged", 'GREYFADEWING': "Grey-Fade Winged", 'BROWNFADEWING': "Brown-Fade Winged", 
                      'PARROTWING': "Parrot Winged", 'GOLDWING': "Golden Winged", 'LIGHTBROWNWING': "Light Brown Winged", 
                      'BLACKWING': "Black Winged", 'ALBINOPINKWING': "Pink Albino Winged", 'ALBINOBLUEWING': "Blue Albino Winged", 
                      'ALBINOREDWING': "Red Albino Winged", 'ALBINOVIOLETWING':"Violet Albino Winged", 'ALBINOYELLOWWING': "Yellow Albino Winged", 
                      'ALBINOGREENWING': "Green Albino Winged", 'MELANISTICLIGHTWING': "Melanistic(No Eyes) Winged", 
                      'MELANISTICWING': "Melanistic Winged", 'MELANISTICDARKWING': "Melanistic(Shadowed Eyes) Winged", 'S_BLACK': "Black Sphynx", 
                      'S_RED': "Red Sphynx", 'S_PINK': "Pink Sphynx", 'S_DARKBROWN': "Dark Brown Sphynx", 'S_BROWN': "Brown Sphynx", 
                      'S_LIGHTBROWN': "Light Brown Sphynx", 'S_DARK': "Dark Sphynx", 'S_DARKGREY': "Dark Grey Sphynx", 'S_GREY': "Grey Sphynx", 
                      'S_DARKSALMON': "Dark Salmon Sphynx", 'S_SALMON': "Salmon Sphynx", 'S_PEACH': "Peach Sphynx", 
                      'S_DARKMARBLED': "Dark Marbled Sphynx", 'S_MARBLED': "Marbled Sphynx", 'S_LIGHTMARBLED': "Light Marbled Sphynx", 
                      'S_DARKBLUE': "Dark Blue Sphynx", 'S_BLUE': "Blue Sphynx", 'S_LIGHTBLUE': "Light Blue Sphynx", 'S_XANADU': "Xanadu Sphynx", 
                      'S_ALBINOPINK': "Pink Albino Sphynx", 'S_ALBINOBLUE': "Blue Albino Sphynx", 'S_ALBINORED': "Red Albino Sphynx", 
                      'S_ALBINOVIOLET': "Violet Albino Sphynx", 'S_ALBINOYELLOW': "Yellow Albino Sphynx", 'S_ALBINOGREEN': "Green Albino Sphynx", 
                      'S_MELANISTICLIGHT': "Melanistic(No Eyes) Sphynx", 'S_MELANISTIC': "Melanistic Sphynx", 'S_MELANISTICDARK': "Melanistic(Shadowed Eyes) Sphynx", 
                      'S_FIRE': "Fire Magic Sphynx", 'S_WATER': "Water Magic Sphynx", 'S_EARTH': "Earth Magic Sphynx", 'S_WIND': "Wind Magic Sphynx", 
                      'S_STAR': "Star Magic Sphynx", 'S_STEAM': "Steam Magic Sphynx", 'S_MAGMA': "Magma Magic Sphynx", 'S_SMOKE': "Smoke Magic Sphynx", 
                      'S_HELL': "Hell Magic Sphynx", 'S_MUD': "Mud Magic Sphynx", 'S_STORM': "Storm Magic Sphynx", 'S_BLOOD': "Blood Magic Sphynx", 
                      'S_SAND': "Sand Magic Sphynx", 'S_BERRY': "Berry Magic Sphynx", 'S_GHOST': "Ghost Magic Sphynx"})
skin_colors = sort_bidict(skin_colors)

colors = bidict({'PALECREAM': "Pale Cream", 'CREAM': "Cream", 'BEIGE': "Beige", 'MEERKAT': "Meerkat", 
                'KHAKI': "Khaki", 'SAND': "Sand", 'WOOD': "Wood", 'ROSE': "Rose", 'GINGER': "Ginger", 'SUNSET': "Sunset", 
                'RUFOUS': "Rufous", 'FIRE': "Fire", 'BRICK': "Brick", 'RED': "Red", 'SCARLET': "Scarlet", 
                'APRICOT': "Apricot", 'GARFIELD': "Garfield", 'APPLE': "Apple", 'CRIMSON': "Crimson", 'BURNT': "Burnt", 
                'CARMINE': "Carmine", 'COSMOS': "Cosmos", 'ROSEWOOD': "Rosewood", 'BLOOD': "Blood", 'SOOT': "Soot", 
                'DARKGREY': "Dark Grey", 'ANCHOR': "Anchor", 'CHARCOAL': "Charcoal", 'COAL': "Coal", 'BLACK': "Black", 
                'GREY': "Grey", 'MARENGO': "Marengo", 'BATTLESHIP': "Battleship", 'CADET': "Cadet", 'BLUEGREY': "Blue-grey", 
                'STEEL': "Steel", 'SLATE': "Slate", 'CAPPUCCINO': "Cappuccino", 'ECRU': "Ecru", 'ASHBROWN': "Ash Brown", 
                'DUSTBROWN': "Dust Brown", 'SANDALWOOD': "Sandalwood", 'PINECONE': "Pinecone", 'WRENGE': "Wrenge", 
                'BROWN': "Brown", 'MINK': "Mink", 'CHESTNUT': "Chestnut", 'TAN': "Tan", 'DARKBROWN': "Dark Brown", 
                'BEAVER': "Beaver", 'CHOCOLATE': "Chocolate", 'MOCHA': "Mocha", 'COFFEE': "Coffee", 'TAUPE': "Taupe", 
                'UMBER': "Umber", 'WHITE': "White", 'SILVER': "Silver", 'BRONZE': "Bronze", 'PALEBOW': "Pastel Rainbow", 
                'TURQUOISE': "Turquoise", 'TIFFANY': "Tiffany", 'SAPPHIRE': "Sapphire", 'OCEAN': "Ocean", 'DENIUM': "Denium", 
                'SHINYMEW': "Shiny Mew Blue", 'SKY': "Sky", 'TEAL': "Teal", 'COBALT': "Cobalt", 'SONIC': "Sonic Blue",
                'POWDERBLUE': "Powderblue", 'JEANS': "Jeans", 'NAVY': "Navy", 'DUSKBOW': "Dusk Rainbow", 'PANTONE': "Pantone", 
                'SALMON': "Salmon", 'THISTLE': "Thistle", 'AMYTHYST': "Amythyst", 'DARKSALMON': "Dark Salmon", 
                'MAGENTA': "Magenta", 'PETAL': "Petal White", 'MEW': "Mew Pink", 'HEATHER': "Heather", 'ORCHID': "Orchid", 
                'STRAKIT': "Starkit Purple", 'PURPLE': "Purple", 'WINE': "Wine", 'RASIN': "Rasin Black", 'GENDER': "Genderfluid Blurple", 
                'REDNEG': "Genderfluid Blurple 2", 'IVORY': "Ivory White", 'BANNANA': "Bannana", 'FARROW': "Farrow", 
                'HAY': "Hay", 'FAWN': "Fawn", 'HAZELNUT': "Hazelnut", 'LEMON': "Lemon", 'LAGUNA': "Laguna", 
                'YELLOW': "Yellow", 'CORN': "Corn", 'GOLD': "Gold", 'HONEY': "Honey", 'BEE': "Bee", 'PINEAPPLE': "Pineapple", 
                'TROMBONE': "Trombone", 'MEDALLION': "Medallion", 'GRANOLA': "Granola", 'SADDLE': "Saddle", 'CEDAR': "Cedar", 
                'ONYX': "Onyx Black", 'LIME': "Lime", 'CHARTRUSE': "Chartruse", 'LETTUCE': "Lettuce", 'GRASS': "Grass", 
                'MINT': "Mint", 'EMERALD': "Emerald", 'OLIVE': "Olive", 'DARKOLIVE': "Dark Olive", 'GREEN': "Green", 'FOREST': "Forest", 
                'JADE': "Jade", 'SPINNACH': "Spinnach", 'SEAWEED': "Seaweed", 'SACRAMENTO': "Sacramento", 'XANADU': "Xanadu", 
                'DEEPFOREST': "Deep Forest", 'AGENDER': "Agender", 'ENBY': "Enby", 'ASEXUAL': "Asexual", 'TRANS': "Trans", 
                'GAYBOW': "Gay Rainbow"})
colors = sort_bidict(colors)

white_patches = bidict({None: 'None', 'MAO': 'Mao', 'LUNA': 'Luna', 'CHESTSPECK': 'Chest Speck', 'WINGS': 'Wings',
                        'PAINTED': 'Painted', 'BLACKSTAR': 'Blackstar', 'LITTLE': 'Little', 'TUXEDO': 'Tuxedo',
                        'LIGHTTUXEDO': 'Light Tuxedo', 'BUZZARDFANG': 'Buzzardfang', 'TIP': 'Tip', 'BLAZE': 'Blaze',
                        'BIB': 'Bib', 'VEE': 'Vee', 'PAWS': 'Paws', 'BELLY': 'Belly', 'TAILTIP': 'Tail Tip',
                        'TOES': 'Toes', 'BROKENBLAZE': 'Broken Blaze', 'LILTWO': 'Lil Two', 'SCOURGE': 'Scourge',
                        'TOESTAIL': 'Toes Tail', 'RAVENPAW': 'Ravenpaw', 'HONEY': 'Honey', 'FANCY': 'Fancy',
                        'UNDERS': 'Unders', 'DAMIEN': 'Damien', 'SKUNK': 'Skunk', 'MITAINE': 'Mitaine',
                        'SQUEAKS': 'Squeaks', 'STAR': 'Star', 'ANY': 'Any', 'ANY2': 'Any 2', 'BROKEN': 'Broken',
                        'FRECKLES': 'Freckles', 'RINGTAIL': 'Ringtail', 'HALFFACE': 'Half Face', 'PANTS2': 'Pants 2',
                        'GOATEE': 'Goatee', 'PRINCE': 'Prince', 'FAROFA': 'Farofa', 'MISTER': 'Mister',
                        'PANTS': 'Pants', 'REVERSEPANTS': 'Reverse Pants', 'HALFWHITE': 'Half White',
                        'APPALOOSA': 'Appaloosa', 'PIEBALD': 'Piebald', 'CURVED': 'Curved', 'GLASS': 'Glass',
                        'MASKMANTLE': 'Mask Mantle', 'VAN': 'Van', 'ONEEAR': 'One Ear', 'LIGHTSONG': 'Lightsong',
                        'TAIL': 'Tail', 'HEART': 'Heart', 'HEART2': 'Heart 2', 'MOORISH': 'Moorish', 'APRON': 'Apron',
                        'CAPSADDLE': 'Cap Saddle', 'COLOURPOINT': 'Colorpoint', 'RAGDOLL': 'Ragdoll',
                        'KARPATI': 'Karpati', 'SEPIAPOINT': 'Sepiapoint', 'MINKPOINT': 'Minkpoint',
                        'SEALPOINT': 'Sealpoint', 'FULLWHITE': 'Full White', 'VITILIGO': 'Vitiligo',
                        'VITILIGO2': 'Vitiligo 2', "EXTRA": "Extra", 'SKELEWHITE': "Skeleton White", 
                        'LIGHTPOINT': "Light Point", 'DARKVITILIGO': "Dark Vitiligo", 'DARKVITILIGO2': "Dark Vitiligo 2",
                        'SNOWSHOE': "Snowshoe", 'VENUS': "Venus", 'SNOWBOOT': "Snowboot", 'CHANCE': "Chance", 
                        'MOSSCLAW': "Mossclaw", 'DAPPLED': "Dappled", 'NIGHTMIST': "Nightmist", 'HAWK': "Hawk",
                        'SHADOWSIGHT': "Shadowsight", 'TWIST': "Twist", 'RETSUKO': "Retsuko", 'OKAPI': "Okapi", 
                        'FRECKLEMASK': "Freckle Mask", 'MOTH': "Moth"})
white_patches = sort_bidict(white_patches, None)

scars = bidict({None: "None", "ONE": "Chest", "TWO": "Shoulder", "THREE": "Over Eye", "TAILSCAR": "Tail",
                "SNOUT": "Snout", "CHEEK": "Cheek",
                "SIDE": "Side", "THROAT": "Throat", "TAILBASE": "Tail Base", "BELLY": "Belly", "LEGBITE": "Bite: Leg",
                "NECKBITE": "Bite: Neck", "FACE": "Face", "MANLEG": "Mangled Leg", "BRIGHTHEART": "Mangled Face",
                "MANTAIL": "Mangled Tail", "BRIDGE": "Bridge", "RIGHTBLIND": "Right Eye Blind",
                "LEFTBLIND": "Left Eye Blind", "BOTHBLIND": "Both Eyes Blind", "BEAKCHEEK": "Beak: Cheek",
                "BEAKLOWER": "Beak: Lower", "CATBITE": "Cat Bite", "RATBITE": "Rat Bite", "QUILLCHUNK": "Quill Chunk",
                "QUILLSCRATCH": "Quill Scratch", "LEFTEAR": "Left Ear Notch", "RIGHTEAR": "Right Ear Notch",
                "NOLEFTEAR": "No Left Ear", "NORIGHTEAR": "No Right Ear", "NOEAR": "No Ears", "NOTAIL": "No Tail",
                "HALFTAIL": "Half Tail", "NOPAW": "Missing Leg",
                "SNAKE": "Bite: Snake", "TOETRAP": "Toe Trap", "BURNPAWS": "Burnt Paws", "BURNTAIL": "Burnt Tail",
                "BURNBELLY": "Burnt Belly", "BURNRUMP": "Burnt Rump", "FROSTFACE": "Frostbitten Face",
                "FROSTTAIL": "Frostbitten Tail", "FROSTMITT": "Frostbitten Paw1", "FROSTSOCK": "Frostbitten Paw2"})
scars = sort_bidict(scars, None)

accessories = bidict({None: "None", "MAPLE LEAF": "Maple Leaf", "HOLLY": "Holly", "BLUE BERRIES": "Blue Berries",
                      "FORGET ME NOTS": "Forget-me-nots", "RYE STALK": "Rye Stalk", "LAUREL": "Laurel",
                      "BLUEBELLS": "Bluebells", "NETTLE": "Nettle", "POPPY": "Poppy", "LAVENDER": "Lavender",
                      "HERBS": "Herbs", "PETALS": "Petals", "DRY HERBS": "Dry Herbs", "OAK LEAVES": "Oak Leaves",
                      "CATMINT": "Catmint", "MAPLE SEED": "Maple Seed", "JUNIPER": "Juniper",
                      "RED FEATHERS": "Red Feathers", "BLUE FEATHERS": "Blue Feathers", "JAY FEATHERS": "Jay Feathers",
                      "MOTH WINGS": "Moth Wings", "CICADA WINGS": "Cicada Wings", "CRIMSON": "Crimson Collar",
                      "BLUE": "Blue Collar", "YELLOW": "Yellow Collar", "CYAN": "Cyan Collar", "RED": "Red Collar",
                      "LIME": "Line Collar", "GREEN": "Green Collar", "RAINBOW": "Rainbow Collar",
                      "BLACK": "Black Collar", "SPIKES": "Spiked Collar", "PINK": "Pink Collar",
                      "PURPLE": "Purple Collar", "MULTI": "Mulicolored Collar", "CRIMSONBELL": "Crimson Bell Collar",
                      "BLUEBELL": "Blue Bell Collar", "YELLOWBELL": "Yellow Bell Collar",
                      "CYANBELL": "Cyan Bell Collar", "REDBELL": "Red Bell Collar", "LIMEBELL": "Lime Bell Collar",
                      "GREENBELL": "Green Bell Collar", "RAINBOWBELL": "Rainbow Bell Color",
                      "BLACKBELL": "Black Bell Collar", "SPIKESBELL": "Spiked Bell Collar",
                      "PINKBELL": "Pine Bell Collar", "PURPLEBELL": "Purple Bell Collar",
                      "MULTIBELL": "Mulitcolored Bell Color", "CRIMSONBOW": "Crimson Bow", "BLUEBOW": "Blue Bow",
                      "YELLOWBOW": "Yellow Bow", "CYANBOW": "Cyan Bow", "REDBOW": "Red Bow", "LIMEBOW": "Line Bow",
                      "GREENBOW": "Green Bow", "RAINBOWBOW": "Rainbow Bow", "BLACKBOW": "Black Bow",
                      "SPIKESBOW": "Spiked Bow", "PINKBOW": "Pink Bow", "PURPLEBOW": "Purple Bow",
                      "MULTIBOW": "Multicolored Bow", "WHITEBOW": "White Bow", "INDIGOBOW": "Indigo Bow",
                      "INDIGO": "Indigo Collar", "WHITE": "White Collar", "WHITEBELL": "White Bell Collar",
                      "INDIGOBELL": "Indigo Bell Collar", "CRIMSONNYLON": "Crimson Nylon Collar",
                      "BLUENYLON": "Blue Nylon Collar", "YELLOWNYLON": "Yellow Nylon Collar",
                      "CYANNYLON": "Cyan Nylon Collar", "REDNYLON": "Red Nylon Collar",
                      "LIMENYLON": "Line Nylon Collar", "GREENNYLON": "Green Nylon Collar",
                      "RAINBOWNYLON": "Rainbow Nylon Collar", "BLACKNYLON": "Black Nylon Collar",
                      "SPIKESNYLON": "Spiked Nylon Collar", "WHITENYLON": "White Nylon Collar",
                      "PINKNYLON": "Pink Nylon Collar", "PURPLENYLON": "Purple Nylon Collar",
                      "MULTINYLON": "Mulicolored Nylon Collar", "INDIGONYLON": "Indigo Nylon Collar",
                      "RAT BLACK": "Black Rat", "RAT BROWN": "Brown Rat", "RAT CREAM": "Cream Rat",
                      "RAT WHITE": "White Rat", "RAT GREY": "Grey Rat", "RAT HOODED": "Hooded Rat",
                      "CRIMSONSTAR": "Crimson Starfish", "BLUESTAR": "Blue Starfish", "YELLOWSTAR": "Yellow Starfish", 
                      "CYANSTAR": "Cyan Starfish", "REDSTAR": "Red Starfish", "LIMESTAR": "Lime Starfish",
                      "DARKSEAWEED": "Dark Seaweed", "LIGHTSEAWEED": "Light Seaweed", "DRYSEAWEED": "Dried Seaweed", 
                      "MAGICSEAWEED": "Magic Seaweed", "DARKPEARLS": "Blue Pearl Chain", "LIGHTPEARL": "White Pearl Chain",
                      "CRIMSONBC": "Crimson Bloodclan Collar", "BLUEBC": "Blue Bloodclan Collar", "YELLOWBC": "Yellow Bloodclan Collar", 
                      "CYANBC": "Cyan Bloodclan Collar", "REDBC": "Red Bloodclan Collar", "LIMEBC": "Lime Bloodclan Collar",
                      "GREENBC": "Green Bloodclan Collar", "RAINBOWBC": "Rainbow Bloodclan Collar", "BLACKBC": "Black Bloodclan Collar", 
                      "SPIKESBC": "Spikes Bloodclan Collar", "PINKBC": "Pink Bloodclan Collar", "PURPLEBC": "Purple Bloodclan Collar", 
                      "MULTIBC": "Lilac Bloodclan Collar", "CRIMSONCAPE": "Crimson Cape", "BLUECAPE": "Blue Cape", 
                      "YELLOWCAPE": "Yellow Cape", "CYANCAPE": "Cyan Cape", "REDCAPE": "Red Cape", "LIMECAPE": "Lime Cape",
                      "GREENCAPE": "Green Cape", "RAINBOWCAPE": "Rainbow Cape", "BLACKCAPE": "Black Cape", 
                      "ORANGECAPE": "Orange Cape", "PINKCAPE": "Pink Cape", "PURPLECAPE": "Purple Cape", "WHITECAPE": "White Cape"})
accessories = sort_bidict(accessories, None)

platforms = {"None": None,
             "Greenleaf Plains - Day": "resources/images/platforms/plains/greenleaf_light.png",
             "Leaf-fall Plains - Day": "resources/images/platforms/plains/leaffall_light.png",
             "Leaf-bare Plains - Day": "resources/images/platforms/plains/leafbare_light.png",
             "Newleaf Plains - Day": "resources/images/platforms/plains/newleaf_light.png",
             "Greenleaf Plains - Night": "resources/images/platforms/plains/greenleaf_dark.png",
             "Leaf-fall Plains - Night": "resources/images/platforms/plains/leaffall_dark.png",
             "Leaf-bare Plains - Night": "resources/images/platforms/plains/leafbare_dark.png",
             "Newleaf Plains - Night": "resources/images/platforms/plains/newleaf_dark.png",
             "Greenleaf Forest - Day": "resources/images/platforms/forest/greenleaf_light.png",
             "Leaf-fall Forest - Day": "resources/images/platforms/forest/leaffall_light.png",
             "Leaf-bare Forest - Day": "resources/images/platforms/forest/leafbare_light.png",
             "Newleaf Forest - Day": "resources/images/platforms/forest/newleaf_light.png",
             "Greenleaf Forest - Night": "resources/images/platforms/forest/greenleaf_dark.png",
             "Leaf-fall Forest - Night": "resources/images/platforms/forest/leaffall_dark.png",
             "Leaf-bare Forest - Night": "resources/images/platforms/forest/leafbare_dark.png",
             "Newleaf Forest - Night": "resources/images/platforms/forest/newleaf_dark.png",
             "Greenleaf Mountains - Day": "resources/images/platforms/mountainous/greenleaf_light.png",
             "Leaf-fall Mountains - Day": "resources/images/platforms/mountainous/leaffall_light.png",
             "Leaf-bare Mountains - Day": "resources/images/platforms/mountainous/leafbare_light.png",
             "Newleaf Mountains - Day": "resources/images/platforms/mountainous/newleaf_light.png",
             "Greenleaf Mountains - Night": "resources/images/platforms/mountainous/greenleaf_dark.png",
             "Leaf-fall Mountains - Night": "resources/images/platforms/mountainous/leaffall_dark.png",
             "Leaf-bare Mountains - Night": "resources/images/platforms/mountainous/leafbare_dark.png",
             "Newleaf Mountains - Night": "resources/images/platforms/mountainous/newleaf_dark.png",
             "Greenleaf Beach - Day": "resources/images/platforms/beach/greenleaf_light.png",
             "Leaf-fall Beach - Day": "resources/images/platforms/beach/leaffall_light.png",
             "Leaf-bare Beach - Day": "resources/images/platforms/beach/leafbare_light.png",
             "Newleaf Beach - Day": "resources/images/platforms/beach/newleaf_light.png",
             "Greenleaf Beach - Night": "resources/images/platforms/beach/greenleaf_dark.png",
             "Leaf-fall Beach - Night": "resources/images/platforms/beach/leaffall_dark.png",
             "Leaf-bare Beach - Night": "resources/images/platforms/beach/leafbare_dark.png",
             "Newleaf Beach - Night": "resources/images/platforms/beach/newleaf_dark.png",
             "Dark Forest - Light": "resources/images/platforms/darkforestplatform_light.png",
             "Dark Forest - Dark": "resources/images/platforms/darkforestplatform_dark.png",
             "StarClan": "resources/images/platforms/starclanplatform_dark.png"}

lineart = ["Normal", "StarClan", "Dark Forest"]

poses = {
    "short": {
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 6,
            "2": 7,
            "3": 8
        },
        "elder": {
            "1": 3,
            "2": 4,
            "3": 5
        }
    },
    "long": {
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "elder": {
            "1": 3,
            "2": 4,
            "3": 5
        }
    }
}