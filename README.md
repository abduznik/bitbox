# bitbox

## Support This Project

> **All projects made with passion** 💙

[![Sponsor me](https://img.shields.io/badge/❤️%20Sponsor-GitHub-red?style=for-the-badge)](https://github.com/sponsors/abduznik)  

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

### Exit codes

Success prints the result to stdout and exits `0`. Anything that fails — an
unknown tool, wrong arguments, or a tool returning an `Error: ...` message —
is printed to stderr and exits `1`.

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
| [@abduznik](https://github.com/abduznik) | project scaffold, 7 seed tools, collapse_whitespace, goldbach_check, is_deficient, is_kaprekar, is_pronic, is_sociable, nth_prime, pairwise_sum, second_smallest, sum_of_primes, word_frequency_top, celsius_to_fahrenheit, count_words, is_palindrome, ordinal, reverse_string, slugify, truncate |
| [@AviDhandhania](https://github.com/AviDhandhania) | count_vowels |
| [@AlexMnrs](https://github.com/AlexMnrs) | is_anagram |
| [@prakhargaba007](https://github.com/prakhargaba007) | count_chars |
| [@rdhadge](https://github.com/rdhadge) | title_case, repeat_string, base64_encode, base64_decode |
| [@JingliangGao](https://github.com/JingliangGao) | is_uppercase |
| [@Julito-Dev](https://github.com/Julito-Dev) | reverse_words, is_iso_date, is_empty |
| [@Diyaaa-12](https://github.com/Diyaaa-12) | absolute, is_odd, flatten_list, unique_list |
| [@Bruce191](https://github.com/Bruce191) | is_even, swap_case |
| [@ishita-0301](https://github.com/ishita-0301) | kg_to_lbs, miles_to_km |
| [@1cbyc](https://github.com/1cbyc) | celsius_to_kelvin, cube, fahrenheit_to_celsius, is_lowercase, keep_vowels, km_to_miles, max_of_two, min_of_two, remove_spaces, remove_vowels, square |
| [@yusichen396](https://github.com/yusichen396) | lbs_to_kg |
| [@Rahul6700](https://github.com/Rahul6700) | contains_substring |
| [@navaneethsankar07](https://github.com/navaneethsankar07) | first_char, last_char, starts_with, snake_to_camel, random_int, is_integer, sentence_count, day_of_week, gcd, url_decode, is_perfect_square, merge_dicts, is_pangram, count_special_chars, count_digits, decimal_to_octal, add_days, is_weekend, is_past, is_armstrong, count_palindromes, count_spaces, generate_random_string, is_mixed_case, mask_email, sort_list, to_lowercase, to_uppercase |
| [@metric-vac](https://github.com/metric-vac) | replace_char |
| [@m-kras](https://github.com/m-kras) | ends_with |
| [@shivsdev2](https://github.com/shivsdev2) | camel_to_snake |
| [@VDeepthi11](https://github.com/VDeepthi11) | generate_password |
| [@blackkingwow](https://github.com/blackkingwow) | url_encode |
| [@itsmgxb24](https://github.com/itsmgxb24) | is_ipv4 |
| [@George4177](https://github.com/George4177) | seconds_to_hms |
| [@Dhruv-Kapri](https://github.com/Dhruv-Kapri) | multiply, remove_char |
| [@persianflower](https://github.com/persianflower) | rgb_to_hex, factorial, hex_to_decimal, is_alphanumeric |
| [@PurpleSwtr](https://github.com/PurpleSwtr) | is_uuid, longest_word, shortest_word, generate_uuid, reading_time |
| [@tmshnko](https://github.com/tmshnko) | file_extension, file_stem |
| [@isaac-sun](https://github.com/isaac-sun) | path_join, path_basename |
| [@zaid-brk](https://github.com/zaid-brk) | json_keys |
| [@AminodinAkbari](https://github.com/AminodinAkbari) | int_to_roman |
| [@byteofhoney](https://github.com/byteofhoney) | csv_to_json |
| [@Evarline](https://github.com/Evarline) | decimal_to_hex (incl. float/negative/malformed-input handling) |
| [@PriyadharshiniRVP](https://github.com/PriyadharshiniRVP) | current_utc |
| [@shayneww](https://github.com/shayneww) | env_parse |
| [@selvakanthanjagavan-byte](https://github.com/selvakanthanjagavan-byte) | html_escape, lcm, octal_to_decimal |
| [@fazalpsinfo-cmyk](https://github.com/fazalpsinfo-cmyk) | error handling (get_description) |
| [@Ayush-0918](https://github.com/Ayush-0918) | decimal_to_binary |
| [@bidisha1005](https://github.com/bidisha1005) | sha256_hash |
| [@HeaTTap](https://github.com/HeaTTap) | is_happy_number, compress_whitespace |
| [@imnaur](https://github.com/imnaur) | is_empty_or_whitespace, is_numeric |
| [@isaakchoi](https://github.com/isaakchoi) | truncate_with_ellipsis, floor, ceil, is_power_of_two, max_of_list, min_of_list, average, extract_letters, extract_digits, abs_diff, trim, wrap_quotes, pad_right, pad_left, is_negative, is_positive, sum_list |
| [@Jesulac](https://github.com/Jesulac) | is_palindrome_ignore_spaces |
| [@0xCrimsonSky](https://github.com/0xCrimsonSky) | count_occurrences |
| [@AshSgDe29071999](https://github.com/AshSgDe29071999) | repeat_char |
| [@mmaxjr](https://github.com/mmaxjr) | index_of |

| [@dreamqwq114-del](https://github.com/dreamqwq114-del) | has_lowercase |
| [@ncmoore55](https://github.com/ncmoore55) | has_uppercase |
| [@shaurya703](https://github.com/shaurya703) | radians_to_degrees, degrees_to_radians |

| [@Solanki-Jatin](https://github.com/Solanki-Jatin) | round_number |
| [@cgkol2005](https://github.com/cgkol2005) | meters_to_feet |
| [@lingeshg18](https://github.com/lingeshg18) | morse_encode |
| [@Almond922](https://github.com/Almond922) | is_port, is_alpha |
| [@aishwarya983](https://github.com/aishwarya983) | age_calculator |
| [@Killerbrine06](https://github.com/Killerbrine06) | binary_to_octal |
| [@AashishGupta2007](https://github.com/AashishGupta2007) | digit_sum |
| [@divyanshsinghtomar-ds](https://github.com/divyanshsinghtomar-ds) | subtract_days |
| [@ShauryaPrakashVerma](https://github.com/ShauryaPrakashVerma) | count_lowercase, count_uppercase, count_non_vowels, is_vowel, count_consonants |

| [@GabrielTrifoni](https://github.com/GabrielTrifoni) | digits_product, char_at |
| [@fathirramadhan-web](https://github.com/fathirramadhan-web) | intersection_of_lists |
| [@1998LJ](https://github.com/1998LJ) | count_primes, next_prime, binary_to_hex, hex_to_binary, octal_to_hex, is_perfect_number, product_of_list, average_of_digits, reverse_number, mode_of_list, range_of_list, collatz_length, prime_factors, longest_common_prefix, catalan_number, fizzbuzz, flatten_nested, is_all_digits, is_mersenne_prime, is_sophie_germain, is_startswith_digit, ngrams, rot13, shuffled_list, top_n_longest_words, triangular_number, union_of_lists |
| [@rmanojgowda](https://github.com/rmanojgowda) | is_abundant |
| [@HarshRajSinghania](https://github.com/HarshRajSinghania) | digital_root |
| [@MateiB20](https://github.com/MateiB20) | octal_to_binary, collatz_steps |
| [@00200200](https://github.com/00200200) | is_twin_prime, variance_of_list, std_dev_of_list, median_of_list, gcd_of_list, lcm_of_list, is_multiple, second_largest, is_sorted, is_hex_color |
| [@rcpeken](https://github.com/rcpeken) | is_weak_password |
| [@jaideepkrishna2008-ui](https://github.com/jaideepkrishna2008-ui) | count_odd_numbers, count_digits_in_string |

| [@Solaris-star](https://github.com/Solaris-star) | binary_to_decimal, caesar_cipher, char_frequency, chunk_list, clamp, current_timestamp, date_to_timestamp, days_between, divide, fibonacci, file_size_human, hex_to_rgb, html_unescape, ini_get, is_credit_card, is_email, is_leap_year, is_prime, is_url, json_minify, json_prettify, levenshtein_distance, line_count, md5_hash, modulo, path_normalize, path_parent, percentage, power, roman_to_int, rotate_list, sha1_hash, strip_html, timestamp_to_date, week_of_year, word_frequency, word_wrap, xml_escape, zip_lists |
| [@sajjadlabx](https://github.com/sajjadlabx) | word_char_ratio |
| [@DYNOSuprovo](https://github.com/DYNOSuprovo) | character_appearances |

<!-- Contributors are added automatically after PRs are merged -->
