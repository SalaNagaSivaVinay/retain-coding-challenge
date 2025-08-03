# CHANGES.md

## Overview
The original codebase had multiple problems, including:
- All logic was dumped into one file without modular structure.
- Passwords were stored in plain text.
- No input validation or error handling.
- Inconsistent route structure and unused code.

## Major Changes Made
- Cleaned up all route endpoints (`/users`, `/login`, etc.).
- Implemented proper CRUD operations (`POST`, `GET`, `PUT`, `DELETE`).
- Added basic validation for user input.
- Tested all routes using Thunder Client.
- Improved HTTP status codes and response formats.
- Removed unused or broken routes.
- Ensured application runs without errors using `Flask` and `SQLite`.

## Trade-offs
- Due to time limits, all logic was kept in a single file (`app.py`).
- No test cases written, but manual testing was done using Thunder Client.

## Tools Used
- Python (Flask)
- SQLite
- Thunder Client (for testing)
- ChatGPT (for debugging and restructuring guidance)

## Future Improvements
- Use a modular structure with folders like `models`, `routes`, `services`.
- Add token-based authentication (e.g., JWT).
- Hash passwords using `bcrypt` or `werkzeug.security`.
- Write automated tests using `pytest`.

## Author
Sala Naga Siva Vinay
