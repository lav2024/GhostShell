# 👻 GhostShell

**Your local AI-powered terminal command explainer.**

GhostShell is a Python command-line application that uses a locally running language model to explain terminal commands in simple English. It also checks for selected risky command patterns and displays safety warnings.

GhostShell is designed to explain commands, not execute them.

## ✨ Features

- **Local AI explanations:** Uses Llama 3.2 1B through Ollama.
- **Risk detection:** Flags selected potentially destructive commands.
- **Continuous interaction:** Enter multiple commands in one session.
- **Automated tests:** Includes unit tests for the rule-based safety checker.
- **Privacy-conscious design:** Sends prompts to a local Ollama service instead of a hosted AI API.

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
git clone <your-github-repository-url>
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

The tests cover ordinary commands, recursive deletion, shutdown commands, command separators, and case-insensitive matching.

## 🛡️ Safety and Limitations

- GhostShell does not execute the commands entered by the user.
- Risk detection uses predefined text patterns and can miss dangerous commands or flag harmless input.
- AI-generated explanations may be inaccurate. Verify commands before running them yourself.
- Local inference requires Ollama and the selected model to be installed.
- Prompts are sent to the local Ollama service configured in the application.

GhostShell is an educational project, not a complete command security system.

## 🎯 Project Goal

Explore how local open-weight language models and rule-based checks can work together to make terminal commands easier to understand.

## 📄 License

This project is open source. A license has not yet been selected.
