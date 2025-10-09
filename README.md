# OpenAI Agents Examples

This repository contains simple examples for experimenting with the OpenAI Agents SDK.
For more information see the project README at
<https://github.com/openai/openai-agents-python>.

## Basic bot

The `basic_bot/bot.py` script demonstrates how to run a single-turn prompt with the Agents SDK.

### Prerequisites

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Export your OpenAI API key so the SDK can authenticate:
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

### Running the bot

Once the dependencies are installed and the `OPENAI_API_KEY` variable is exported, run:

```bash
python basic_bot/bot.py
```

The script will print the assistant's response to the recursion haiku prompt.
