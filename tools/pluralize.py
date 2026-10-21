# tool: pluralize
# description: Pluralize a simple English noun
# author: @Subham-entity
# example: pluralize "cat" -> "cats"

IRREGULAR_PLURALS = {
    "man": "men",
    "woman": "women",
    "child": "children",
    "tooth": "teeth",
    "foot": "feet",
    "person": "people",
    "mouse": "mice",
    "goose": "geese",
    "fish": "fish",
    "sheep": "sheep",
    "deer": "deer",
    "series": "series",
    "species": "species",
    "octopus": "octopuses",
}

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one noun."
    
    word = str(args[0]).strip()
    if not word:
        return "Error: Please provide a non-empty noun."

    word_lower = word.lower()

    # 1. Check irregular/uncountable dictionary
    if word_lower in IRREGULAR_PLURALS:
        result = IRREGULAR_PLURALS[word_lower]
        return result.capitalize() if word.istitle() else result

    # 2. Check words ending in -y (preceded by a consonant)
    if word_lower.endswith("y") and len(word_lower) > 1 and word_lower[-2] not in "aeiou":
        return word[:-1] + "ies"

    # 3. Check words ending in -s, -sh, -ch, -x, -z
    if word_lower.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es"

    # 4. Check words ending in -fe or -f
    if word_lower.endswith("fe"):
        return word[:-2] + "ves"
    if word_lower.endswith("f") and not word_lower.endswith("ff"):
        return word[:-1] + "ves"

    # 5. Default rule
    return word + "s"