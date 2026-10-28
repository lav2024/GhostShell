# 👻 GhostShell

**Your local AI-powered terminal command explainer.**

GhostShell is a Python command-line application that uses a locally running language model to explain terminal commands in simple English. It also checks for selected risky command patterns and displays safety warnings.

GhostShell is designed to explain commands, not execute them.

## ✨ Features

- **Local AI explanations:** Uses Llama 3.2 1B through Ollama.
- **Known-command explanations:** Provides predefined explanations for `mkdir` and `cd`.
- **Risk detection:** Flags selected potentially destructive command patterns.
- **Continuous interaction:** Enter multiple commands in one session.
- **Automated tests:** Includes unit tests for safety checks and known-command explanations.
- **Privacy-conscious design:** Uses a locally running Ollama service instead of a hosted AI API for command explanations.

## 🛠️ Technology Stack

- Python
- Ollama
- Llama 3.2 1B
- Python `unittest`

## 📋 Prerequisites

1. Install Python.
2. Install [Ollama](https://ollama.com/).
3. Download the model:

   ```bash
   ollama pull llama3.2:1b
   ```

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/lav2024/GhostShell.git
cd GhostShell
```

Make sure Ollama is running, then start GhostShell:

```bash
py ghostshell.py
```

Enter a terminal command to receive an explanation and a safety check.

Type `exit` to close GhostShell.

## 🧪 Run the Tests

Run the automated tests with:

```bash
py -m unittest -v test_ghostshell.py
```

The tests cover:

- Ordinary command handling
- Recursive deletion warnings
- Shutdown command warnings
- Command separator detection
- Case-insensitive risk matching
- Known-command explanations for `mkdir` and `cd`
- Handling of unknown commands by the rule-based explanation function

## 🛡️ Safety and Limitations

- GhostShell does not execute commands entered by the user.
- Risk detection relies on predefined text patterns and may miss dangerous commands or flag harmless input.
- AI-generated explanations may be inaccurate. Verify commands before running them yourself.
- Local inference requires Ollama and the selected model to be installed.
- Command prompts are sent to the locally configured Ollama service.

GhostShell is an educational project, not a complete command security system.

## 🎯 Project Goal

Explore how local open-weight language models and rule-based checks can work together to make terminal commands easier to understand.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
