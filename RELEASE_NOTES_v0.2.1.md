# LabLog v0.2.1 — Release Notes

> Draft: check each item against the final v0.2.1 commit before publishing this as a GitHub Release.

LabLog v0.2.1 is a maintenance update to the terminal-based study tracker. It keeps the procedural, function-and-module-based design while improving the handling of user input and topic operations.

## Improvements

- Centralized status-choice validation in a reusable helper instead of duplicating the same input loop in multiple menu branches.
- Handled invalid integer input with a targeted `ValueError` handler, rather than catching every exception.
- Improved the invalid-selection flow so the status menu can be shown again with a clear error message. *(Keep this item only if the final version redraws the menu as intended.)*

## Fixes

- Reject blank or whitespace-only topic names.
- Prevent adding a topic whose name already exists, avoiding accidental overwrites of its current status.
- Report status changes as successful only when the requested topic exists, and save the data only after a valid change.

## Features carried forward

- Add, delete, and search for topics.
- Display all saved topics.
- Change a topic's status.
- Filter topics by status.
- Persist profile and topic data in `data/study.json`.

## Compatibility and dependencies

- Requires Python 3.15 or newer because the source uses `lazy import` syntax.
- No third-party dependencies are required.

## Upgrade notes

No migration step is expected for the existing `data/study.json` structure. Back up the file before upgrading, especially if it contains personal changes.

## Known limitations

- Data is stored locally in one JSON file; there is no database, user account system, or synchronization between devices.
- The app is a small learning project and has not yet been packaged or distributed as an installable application.

## What's next

The planned v0.3 milestone will explore a class-based design and object-oriented programming. It is not part of v0.2.1.
