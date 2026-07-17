# Contributing to bitbox

Thanks for your interest! bitbox is designed so anyone can contribute a tool in minutes.

## The 3-Step Loop

1. **Pick an issue** — browse [open issues](../../issues) or create a new one using the tool request template.
2. **Copy `template.py`** into `tools/your_tool_name.py` and implement the `run()` function.
3. **Open a PR** — title it `[tool] your_tool_name`.

## Which Issues Can I Work On?

- **PRs are first come, first served** — even if an issue is assigned to someone else, if they haven't opened a PR yet, anyone can submit one. Assignment is not exclusive.
- **Issues are created automatically** — they exist so everyone gets a fair shot at contributing. Please be sporty: don't "steal" an issue someone is actively working on (i.e., already has a PR open), but don't wait around either if there's no activity.

## File Rules (strict)

Every tool file **must** follow these rules:

- **One file** in `tools/`, named `your_tool_name.py`
- **One function** called `run` that accepts `*args` and returns a `str`
- **Header comments required** — the first lines must be:
  ```python
  # tool: your_tool_name
  # description: A short one-line description
  # author: @your_github_username
  # example: your_tool_name "input" → "output"
  ```
- The `author` field must be your **GitHub username** (e.g. `@octocat`)
- **No external dependencies** — stdlib only. No pip installs.
- Return values must be strings (use `str()` to convert)

## PR Title Format

```
[tool] your_tool_name
```

## Testing Locally

Before opening a PR, test your tool:

```bash
python bitbox.py your_tool_name "your test input"
```

## Recognition

Your name will appear in the contributors table in `README.md` automatically after your PR is merged.
