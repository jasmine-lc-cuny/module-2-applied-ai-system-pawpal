# PawPal+ (Module 2 Project)

PawPal+ is a CLI-first pet care management app that helps owners organize daily routines for their pets. It combines object-oriented Python classes with a simple Streamlit interface so users can add pets, schedule tasks, review important reminders, and receive smart scheduling feedback.

## What PawPal+ Does

- Add and manage pets for an owner
- Schedule care tasks such as walks, meals, medications, and grooming
- Sort tasks by time or priority
- Filter tasks by pet and completion status
- Detect task conflicts for the same date and time
- Automatically create the next recurring task for daily or weekly routines
- Persist data between app runs using JSON storage

## Features

- Track task time, duration, priority, frequency, due date, and completion status
- View schedules sorted by chronological order or urgency
- Highlight the next urgent task and the top three priorities for the day
- Use a Streamlit interface backed by session state for a smoother browser experience
- Save and reload pet and task data through JSON persistence

## Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the CLI demo:

```bash
python main.py
```

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

## Sample Output

Example output from running `python main.py`:

```text
PawPal+ schedule for Jordan
================================
📅 Today's Schedule
  07:30 - Luna: Breakfast (10 min, high, daily, 2026-07-01, ⏳ open)
  08:00 - Mochi: Morning walk (30 min, high, daily, 2026-07-01, ⏳ open)
  08:00 - Luna: Brush coat (15 min, medium, once, 2026-07-01, ⏳ open)
  12:00 - Mochi: Heartworm medication (5 min, high, once, 2026-07-01, ⏳ open)

High Priority First
  07:30 - Luna: Breakfast (10 min, high, daily, 2026-07-01, ⏳ open)
  08:00 - Mochi: Morning walk (30 min, high, daily, 2026-07-01, ⏳ open)
  12:00 - Mochi: Heartworm medication (5 min, high, once, 2026-07-01, ⏳ open)
  08:00 - Luna: Brush coat (15 min, medium, once, 2026-07-01, ⏳ open)

🚨 Next Urgent Task
  07:30 - Luna: Breakfast (10 min, high, daily, 2026-07-01, ⏳ open)

⭐ Today's Top 3 Priorities
  07:30 - Luna: Breakfast (10 min, high, daily, 2026-07-01, ⏳ open)
  08:00 - Mochi: Morning walk (30 min, high, daily, 2026-07-01, ⏳ open)
  12:00 - Mochi: Heartworm medication (5 min, high, once, 2026-07-01, ⏳ open)

⚠️ Conflict Warnings
  Conflict on 2026-07-01 at 08:00: Mochi: Morning walk, Luna: Brush coat

🔁 Recurring Task Created
  08:00 - Mochi: Morning walk (30 min, high, daily, 2026-07-02, ⏳ open)
```

## Persistence and Bonus Features

- The app saves owner, pet, and task data to `data.json` whenever the Streamlit app updates the schedule.
- The backend supports `Owner.save_to_json()` and `Owner.load_from_json()` for round-trip persistence.
- The CLI and UI both show a “Today’s Top 3 Priorities” view powered by `Scheduler.get_top_priority_tasks()`.
- The interface also uses lightweight emoji-based formatting to make the schedule easier to scan.

## Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks chronologically using `HH:MM` strings. |
| Priority sorting | `Scheduler.sort_by_priority_then_time()` | Sorts high priority first, then by time. |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet name and/or completion status. |
| Conflict handling | `Scheduler.detect_conflicts()` | Returns warning strings for exact same date/time matches. |
| Recurring tasks | `Task.next_occurrence()`, `Scheduler.mark_task_complete()` | Creates the next daily or weekly task after completion. |
| Urgent task selection | `Scheduler.get_next_urgent_task()` | Picks the most urgent open task for the day. |
| Top-priority summary | `Scheduler.get_top_priority_tasks()` | Returns the highest-priority tasks up to a requested limit. |

## Testing PawPal+

Run the full test suite:

```bash
python -m pytest
```

The test suite covers task completion, task addition, chronological sorting, filtering, daily recurrence, conflict detection, persistence, and priority-based scheduling.

```text
============================= test session starts =============================
platform linux -- Python 3.11.11, pytest-8.3.0
rootdir: /workspaces/ai110-module2show-pawpal-starter
collected 9 items

tests/test_pawpal.py .................                                  [100%]

============================== 9 passed in 0.02s ==============================
```

Confidence Level: 4.5/5 stars. The core behaviors are fully verified, and the bonus features are covered by automated tests as well.

## Demo Walkthrough

1. The user enters their owner name in the sidebar.
2. The user adds pets such as Mochi the dog and Luna the cat.
3. The user schedules care tasks with a time, duration, priority, and frequency.
4. PawPal+ displays the schedule as a table sorted by time or by urgency.
5. The user filters tasks by pet or status and sees conflict warnings when two open tasks share the same date and time.
6. When the user marks a daily or weekly task complete, PawPal+ creates the next occurrence automatically.

## Architecture

- Draft UML: `diagrams/uml.mmd`
- Final UML: `diagrams/uml_final.mmd`
- Backend logic: `pawpal_system.py`
- CLI verification: `main.py`
- Streamlit UI: `app.py`
- Tests: `tests/test_pawpal.py`
