# Task 3 — Chat Projects

**Goal:** show how a Project changes results — first with no setup, then with custom instructions, then with knowledge files — and how it remembers across chat sessions.

## Files in this folder
- `project_instructions.md` — paste into the Project's custom instructions
- `test_case_template.csv` — upload as a knowledge file (the format Claude must follow)
- `severity_priority_definitions.md` — upload as a knowledge file
- `naming_conventions.md` — upload as a knowledge file
- `sample_user_story.md` — the input you'll paste into chats

## Run it in four stages (show the difference each time)

**Stage 1 — Plain chat, no Project.**
New normal chat. Paste the user story from `sample_user_story.md` and ask: *"Generate test cases."*
→ Generic format, generic severity words, no naming convention. Note what's missing.

**Stage 2 — Project, instructions only (no files).**
Create a Project "Tristha Test Case Generator". Paste `project_instructions.md` into custom instructions. Don't upload files yet. Paste the same story.
→ Better structure and tone, but it's guessing your template, severity scale, and IDs.

**Stage 3 — Project, instructions + knowledge files.**
Upload the three knowledge files. Paste the same story again.
→ Now it uses YOUR exact columns, YOUR severity definitions (S1–S4), and YOUR ID convention. This is the "aha".

**Stage 4 — Cross-session memory.**
Start a **brand-new chat inside the same Project**. Don't re-paste anything. Ask:
*"Using our standard, generate test cases for an OTP-on-login feature."*
→ It still knows the template, severity scale, and naming — because the Project carries the knowledge across every chat. Then ask: *"Summarise what we've generated in this project so far."*

## Discuss
- Instructions = the durable rules (the "system prompt" they learned yesterday).
- Knowledge files = your standards, read automatically, never re-pasted.
- Every chat in the Project inherits both → consistent output for the whole team.
