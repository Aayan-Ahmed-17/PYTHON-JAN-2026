# Day-1: Python File I/O — Speed Practice

Goal: Learn core Python file I/O at a fast pace.
Focus: open, read, write, append

--------------------------------------------------

Q1 — Read a File Line-by-Line (FOUNDATION)

Task:
Read `filesystem_practice_data.txt` line by line and print each line with line numbers.

Requirements:
- Use `with`
- Do NOT use `read()` or `readlines()`
- Strip extra whitespace

Edge Cases:
- Empty lines should still count
- Special characters may exist

Testing:
- Line numbers start from 1
- No extra blank spacing

--------------------------------------------------

Q2 — Read Only a Specific Section

Task:
Print only the lines AFTER `--- LOGS ---`

Requirements:
- Line-by-line reading
- Use a boolean flag

Edge Cases:
- Marker appears once
- Ignore everything before it

Testing:
- Output starts with timestamps
- No user data printed

--------------------------------------------------

Q3 — Write to a New File

Task:
Create `logs_only.txt` and write only log lines into it.

Requirements:
- Use write mode (`w`)
- Preserve formatting
- Use UTF-8 encoding

Edge Cases:
- Overwrite if file exists
- No empty first line

Testing:
- File must exist
- Contains ONLY logs

--------------------------------------------------

Q4 — Append Data (REAL-WORLD)

Task:
Append a new log entry to `filesystem_practice_data.txt`

Example:
2024-01-03 11:00:00 INFO Practice log added

Requirements:
- Use append mode (`a`)
- Do NOT overwrite existing content
- Handle newline correctly

Edge Cases:
- File may or may not end with a newline

Testing:
- Old data remains
- New log is last line

--------------------------------------------------

Q5 — Count Lines

Task:
Count total lines in the file and print the count.

Requirements:
- Line-by-line iteration
- No list conversion

Edge Cases:
- Empty file returns 0

Testing:
- Count matches manual count

--------------------------------------------------

Q6 — Safe File Reading

Task:
Try reading `missing.txt`.
If it does not exist, print:
File not found

Requirements:
- Use try/except
- Catch FileNotFoundError only

Edge Cases:
- File exists but empty

Testing:
- Program does not crash

--------------------------------------------------

Rules:
- Always use `with`
- Always use `encoding="utf-8"`
- No shortcuts

Completion:
When done, say:
"Day-1 done. Check my code."
