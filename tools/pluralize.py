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
}

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one noun."
    
    word = str(args[0]).strip()
    if not word:
        return ""

    word_lower = word.lower()

    if word_lower in IRREGULAR_PLURALS:
        result = IRREGULAR_PLURALS[word_lower]
        return result.capitalize() if word.istitle() else result

    if word_lower.endswith("y") and len(word_lower) > 1 and word_lower[-2] not in "aeiou":
        return word[:-1] + "ies"

    if word_lower.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es"

    if word_lower.endswith("fe"):
        return word[:-2] + "ves"
    if word_lower.endswith("f") and not word_lower.endswith("ff"):
        return word[:-1] + "ves"

    return word + "s"