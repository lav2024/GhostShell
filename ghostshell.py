import json
import urllib.request
import urllib.error

MODEL = "llama3.2:1b"
OLLAMA_URL = "http://localhost:11434/api/generate"


def check_risks(command):
    """Find selected risky command patterns without executing them."""
    text = command.lower()
    warnings = []

    risk_rules = [
        ("rm -rf", "Recursive deletion may permanently remove files."),
        ("format ", "Formatting a drive can erase its data."),
        ("shutdown", "This command may shut down the system."),
        ("diskpart", "Disk management commands can modify partitions."),
        ("del ", "This command may delete files."),
        ("remove-item", "This command may delete files or folders."),
        ("drop database", "This SQL command may remove an entire database."),
    ]

    for pattern, message in risk_rules:
        if pattern in text:
            warnings.append(message)

    if any(symbol in command for symbol in (";", "&&", "||", "|")):
        warnings.append(
            "This input contains command separators or a pipe. "
            "Review each part carefully."
        )

    return list(dict.fromkeys(warnings))


def explain_known_command(command):
    """Explain selected commands using predefined Python rules."""
    parts = command.strip().split()

    if not parts:
        return None

    name = parts[0].lower()

    if name == "mkdir":
        options = [
            part for part in parts[1:]
            if part.startswith("-")
        ]
        paths = [
            part for part in parts[1:]
            if not part.startswith("-")
        ]

        if not paths:
            return (
                "Purpose: mkdir creates a new directory.\n"
                "Caution: Provide a directory name to create."
            )

        if "-p" in options:
            return (
                f"Purpose: Creates directory path(s): {', '.join(paths)}.\n"
                "Options: -p creates parent directories as needed "
                "and does not fail just because a directory already exists."
            )

        return (
            f"Purpose: Creates a directory named {', '.join(paths)}.\n"
            "Caution: Creating a directory that already exists "
            "may produce an error."
        )

    if name == "cd":
        if len(parts) == 1:
            return (
                "Purpose: Changes the current directory. "
                "With no path, its behavior depends on the shell."
            )

        path = " ".join(parts[1:])
        if path == "..":
            return (
                "Purpose: Changes the current directory "
                "to its parent directory."
            )

        return f"Purpose: Changes the current directory to {path}."

    return None


def ask_ghost(command):
    """Use known explanations first, then ask the local AI."""
    known_explanation = explain_known_command(command)

    if known_explanation is not None:
        print("\n👻 The Ghost whispers:\n")
        print(known_explanation)
        return

    prompt = f"""
You are GhostShell, a concise and accurate terminal command explainer.

Explain this command as text only:
{command!r}

Follow these rules:
- State what the command does in plain English.
- Explain important options or flags when present.
- Describe realistic side effects, not imaginary ones.
- For potentially destructive commands, explain what they can delete
  or change and advise the user to verify the target first.
- Do not refuse merely because a command can be destructive.
- Never claim that you executed the command.
- Do not invent what a command will create or change.
- Use at most one short spooky phrase.
- Keep the answer under 80 words.

Use this format:
Purpose: ...
Options: ... (only when relevant)
Caution: ... (only when relevant)
"""

    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 120,
            "temperature": 0.2
        }
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        print("\n👻 The Ghost whispers:\n")
        print(result.get("response", "The Ghost has no words today."))

    except urllib.error.URLError:
        print("\nThe Ghost is sleeping!")
        print("Check that Ollama is running.")

    except TimeoutError:
        print("\nThe Ghost took too long to respond. Try again.")


def main():
    print("=" * 40)
    print("       👻 GHOSTSHELL 👻")
    print("  Your local AI terminal companion")
    print("=" * 40)

    while True:
        command = input(
            "\nEnter a command (or 'exit'): "
        ).strip()

        if command.lower() == "exit":
            print("The Ghost disappears into the terminal...")
            break

        if not command:
            print("The Ghost needs a command to investigate!")
            continue

        warnings = check_risks(command)

        ask_ghost(command)

        print("\n🛡️ Safety check:")

        if warnings:
            for warning in warnings:
                print(f"⚠️ {warning}")
        else:
            print("No predefined risk pattern detected.")

        print("Note: This basic check cannot guarantee command safety.")
        print("GhostShell analyzes commands; it never executes them.")


if __name__ == "__main__":
    main()
