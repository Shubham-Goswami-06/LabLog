# LabLog

LabLog is a small terminal-based study tracker written in Python. It helps you keep track of topics you have completed, are currently studying, or have not started yet. It is also a learning project for practising Python, input validation, modular code, JSON persistence, and version control.

## Features

- Add a study topic and choose its status.
- Delete a topic.
- Search for a topic by name.
- Display all saved topics.
- Change a topic's status.
- Filter topics by status.
- Save topic data locally in a JSON file so it persists between runs.
- Validate status-menu input and handle invalid numeric selections.

## Status options

- `Complete`
- `Currently Studying`
- `Not Started`

## Requirements

- Python 3.15 or newer, because the project uses Python's `lazy import` syntax.
- No third-party packages are required; the app uses the Python standard library.

Check your interpreter version with:

```bash
python --version
```

If your system has multiple Python versions installed, use the command that launches Python 3.15 or newer.

## Run LabLog

Clone the repository:

```bash
git clone https://github.com/Shubham-Goswami-06/LabLog.git
cd LabLog
```

Run the application:

```bash
python main.py
```

Use the numbered menu to choose an operation. In status-selection menus, enter `0` to return to the home menu.

## Where is my data stored?

LabLog reads and writes its study data in `data/study.json`. The file contains the profile fields and the topic-to-status mapping. Back up this file before making manual edits, and keep valid JSON syntax when editing it yourself.

The repository currently includes an example study file. Replace the sample profile and topics with your own values before using it as your personal tracker. Avoid committing secrets or information you do not want to publish.

## Project structure

```text
LabLog/
├── main.py          # Main menu and application flow
├── topic.py         # Operations on topics
├── validate.py      # Input validation for status selection
├── ui.py            # Terminal display helpers
├── data.py          # Loading and saving JSON data
├── data/
│   └── study.json   # Saved profile and topic data
└── LICENSE
```


## Project status

**v0.2.1 — procedural version.** The current implementation uses functions and modules. A future v0.3 milestone is planned to explore a class-based design and object-oriented programming (OOP).

LabLog is an educational project and is not yet packaged as an installable Python application.

## License

LabLog is distributed under the Apache License 2.0. See [`LICENSE`](LICENSE) for the full license text.
