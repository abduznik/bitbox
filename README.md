# bitbox

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)
![License](https://img.shields.io/badge/license-MIT-gray)

A community-built collection of tiny Python CLI tools. One file. One function. One contributor.

## Quick Start

No install needed. Clone and run.

```bash
git clone https://github.com/abduznik/bitbox.git
cd bitbox
python bitbox.py --list
```

## Usage

```bash
python bitbox.py <tool_name> [arguments...]
```

### Examples

```bash
# Reverse a string
python bitbox.py reverse_string "hello world"
# → dlrow olleh

# Count words
python bitbox.py count_words "the quick brown fox"
# → 4

# Convert Celsius to Fahrenheit
python bitbox.py celsius_to_fahrenheit 100
# → 212.0

# Check if a string is a palindrome
python bitbox.py is_palindrome "racecar"
# → True

# List all available tools
python bitbox.py --list
```

## Available Tools

Run `python bitbox.py --list` to see all tools. Each tool is a single Python file in `tools/`.

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines. The short version:

1. Pick an issue (or open one)
2. Copy `template.py` into `tools/`
3. Implement `run()`
4. Open a PR

## Contributors

| Name | Tool |
|------|------|
| [@abduznik](https://github.com/abduznik) | project scaffold, 7 seed tools |
| [@AviDhandhania](https://github.com/AviDhandhania) | count_vowels |
| [@AlexMnrs](https://github.com/AlexMnrs) | is_anagram |
| [@prakhargaba007](https://github.com/prakhargaba007) | count_chars |
| [@rdhadge](https://github.com/rdhadge) | title_case, repeat_string |

<!-- Contributors are added automatically after PRs are merged -->

