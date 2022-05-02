import regex

# Replaces parts of a given string based on an array of tuples each containing a regex pattern and a replacement string
def multiple_replace(replacements, string):
  res = string
  for pattern, replacement in replacements:
    res = regex.sub(pattern, replacement, res, flags=regex.I)

  return res

# Translates given text to Ork speech
def orkify(text):
  replacements = [
    # specific vocab
    (r"\bwar\b", "waaagh"),
    (r"\bhey\b", "oi"),
    (r"\bstrong\b", "'ard"),
    (r"\battention\b", "attenchun"),
    (r"\properly\b", "propally"),
    (r"\bfight\b", "bash"),
    (r"\bbest\b", "bestest"),
    (r"\bmost\b", "mostest"),
    (r"\bbeen\b", "bin"),
    (r"\bsword\b", "choppa"),
    (r"\bkill", "krump"),
    (r"(\bdangerous\b)|(\blethal\b)|(\bdeadly\b)", "killy"),
    (r"(\baggressive\b)|(\bviolent\b)", "fighty"),
    (r"(\bfirepower\b)|(\bguns\b)|(\bammunition\b)|(\bammo\b)|(\bbullets\b)", "dakka"),
    (r"\bdead\b", "ded"),
    (r"\bdeath\b", "deff"),
    (r"\bfor\b", "fer"),
    (r"\byou\b", "ya"),
    (r"\byour\b", "yer"),
    (r"\bmouth\b", "gob"),
    (r"\bto\b", "ta"),
    (r"\bgood\b", "gud"),
    (r"\bpp\b", "jibbliez"),
    (r"\bhuman\b", "humie"),
    (r"\bfuck\b", "zog"),
    (r"fuck", "zogg"),
    (r"i've", "i'z"),
    (r"(\bguy)|(\bdumbass\b)|(\bidiot)", "git"),
    (r"\bdumbasses", "gitz"),
    # numbers
    (r"^([0-9]{2,})(?![A-Za-z0-9\s])$", "lotz"),
    (r"^([0-9]{2,})(?=\s\w+)$", "lotsa"),
    (r"^[6-9](?![A-Za-z0-9\s])$", "lotz"),
    (r"^[6-9](?=\s\w+)$", "lotsa"),
    (r"^1$|\bone\b", "wun"),
    (r"^2$|\btwo\b", "too"),
    (r"^3$|\bthree\b", "free"),
    (r"^4$|four", "forr"),
    (r"^5$|five", "fyve"),
    (r"first", "furst"),
    (r"second", "sekund"),
    (r"third", "fird"),
    (r"fourth", "forf"),
    (r"fifth", "fyff"),
    # ould to ud
    (r"ould", "ud"),
    # ending er to a
    (r"er\b", "a"),
    # beginning h exceptions
    (r"\bhe\b", "'ee"),
    (r"he'll", "'ee'l"),
    (r"he's", "'ee'z"),
    # beginning h to '
    (r"\bh", "'"),
    # various th exceptions
    (r"\bthe\b", "da"),
    (r"(\bthere)|(\btheir)", "dere"),
    (r"\bthem", "dem"),
    (r"\bthey\b", "dey"),
    (r"(\btheyre\b)|(\bthey're\b)|(\btheyve\b)|(\bthey've\b)", "dey'ze"),
    (r"\bthose\b", "dose"),
    (r"\bthis\b", "dis"),
    (r"\bthat\b", "dat"),
    (r"\bthan\b", "dan"),
    (r"\bthen\b", "den"),
    (r"(\bthats\b)|(\bthat's\b)", "dat'z"),
    # possessives
    (r"\bours\b", "arrz"),
    (r"\byour\b", "yer"),
    # beginning th to f
    (r"\bth", "f"),
    # middle th to vv/f/ff
    (r"something", "sumfing"),
    (r"nothing", "nuffing"),
    (r"everything", "everyfing"),
    (r"worthless", "wurfless"),
    (r"\Bth\B", "vv"),
    # ending th to ff
    (r"with", "wiv"),
    (r"th\b", "ff"),
    # ck to kk
    (r"ck", "kk"),
    # ending s to z
    (r"(?<![ios])s\b(?!s)", "z"),
    # hard c to k
    (r"\bc(?![ehiy])", "k"),
    (r"(?<!\bet)c\b", "k"),
    # ending ing with in'
    (r"(?<=\w*[aeiou]+\w*in)g\b", "'"),
    # certain ough to uff
    (r"\benough\b", "enuff"),
    (r"\btough\b", "tuff"),
    # certain wh
    (r"what", "wot"),
    (r"\bwho\b", "oo"),
    (r"who's", "oo'z"),
    (r"whether", "wevva")
    ]
  return multiple_replace(replacements, text).upper()