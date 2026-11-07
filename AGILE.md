# Agile Development Notes

## Sprint Goal

Build and verify a minimal Flask REST API with JSON responses for `/hello` and `/data`.

## User Stories

1. As an API user, I want to call `/hello` so that I receive a welcome message in JSON format.
2. As an API user, I want to call `GET /data` so that I can retrieve structured sample data.
3. As an API user, I want to call `POST /data` so that I can submit a new JSON record.
4. As a developer, I want an automated test script so that I can verify the API endpoints quickly.

## Sprint Backlog

- [x] Create Flask application.
- [x] Implement `GET /hello`.
- [x] Implement `GET /data`.
- [x] Implement `POST /data`.
- [x] Add JSON validation and HTTP status codes.
- [x] Create `requirements.txt`.
- [x] Create Python `requests` test script.
- [x] Write project documentation.
- [ ] Capture screenshots of successful API calls.
- [ ] Push completed project to GitHub.

## Definition of Done

A task is complete when:

- The route runs without errors.
- The response is valid JSON.
- The correct HTTP status code is returned.
- The code is readable and follows basic PEP-8 style.
- The endpoint is demonstrated successfully with the test script.
- The work is committed to GitHub.
