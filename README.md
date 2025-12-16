# AI_agent

An AI coding agent that can list, read, write, and run Python files through CLI prompts. The agent uses a language model (Google GenAI) to plan actions and calls local function tools to perform filesystem and execution tasks.

---

## Features
- Natural-language CLI interface for repository exploration and code editing.
- Available operations (exposed as function tools):
  - List files and directories
  - Read file contents
  - Write or overwrite files
  - Execute Python files with optional arguments
- Iterative function-call loop: model returns function-call plans, the agent executes them locally and returns results back to the model until completion.
- Optional verbose mode that prints token usage and debug info.

---

## Quick links
- CLI entrypoint: `main.py`
- Function-call glue: `call_function.py`
- Function implementations: `functions/`
- Example app: `calculator/`
- Tests: `tests.py`
- Project metadata: `pyproject.toml`

---

## Requirements
- Python 3.8+
- An API key for Google GenAI (Gemini)
- Recommended packages (install with pip or via your preferred dependency manager):
  - google-genai
  - python-dotenv
- See `pyproject.toml` for project metadata and locked dependencies.

---

## Installation

1. Clone the repo
   - git clone https://github.com/jeffeejenson/AI_agent.git
   - cd AI_agent

2. Create and activate a virtual environment
   - python -m venv .venv
   - source .venv/bin/activate  (macOS / Linux)
   - .venv\Scripts\activate     (Windows PowerShell)

3. Install dependencies
   - If you have pip and want only runtime deps used by this project:
     - python -m pip install google-genai python-dotenv
   - Or use your preferred dependency manager (poetry, pip-tools, etc.) and consult `pyproject.toml`.

4. Configure API key
   - Create a `.env` file in the project root with:
     - GEMINI_API_KEY=your_api_key_here
   - Or export the environment variable in your shell:
     - export GEMINI_API_KEY="your_api_key_here"

Do NOT commit your API keys.

---

## Usage

Basic usage:
- python main.py "Describe or ask the agent to modify files in this repository"

The agent expects a single prompt argument. Example:
- python main.py "List files in the repository root"

Verbose mode:
- python main.py "Read main.py" --verbose
- Verbose prints token usage and other debug information returned by the GenAI client.

How it works:
- `main.py` loads your GEMINI_API_KEY, sends the user prompt to the model, and passes a system instruction describing available tools.
- The model returns candidates and (when appropriate) function calls.
- `call_function.py` maps those function calls to the implementations in `functions/` and returns results back to the model.
- The loop continues for up to a configured number of iterations or until the model finishes.

Example prompts to try:
- "List all files and directories."
- "Open functions/get_file_content.py and show me the contents."
- "Create or overwrite src/utils/helper.py with an email validation function."
- "Run calculator/main.py with the expression `3 + 5` and return the result."

---

## Calculator example

The repository includes a small calculator example in `calculator/`. You can run it directly:

- cd calculator
- python main.py "3 + 5"

It prints a JSON-like formatted result for the expression.

---

## Running tests

There is a `tests.py` file at the repo root. Run it with:
- python tests.py

(Review the test file to see its expectations and adjust the environment as needed.)


Security & safety

- The agent can write files and run arbitrary Python code locally. Only run it in environments where you trust the prompts or where changes can be reviewed.

