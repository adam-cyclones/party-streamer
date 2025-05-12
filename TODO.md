# ✅ TODO — Party Streamer

This is the working task list for the log streaming full-stack app.

---

## Core Features

- [ ] **Setup install** 
- [ ] **Create REST API**  
  _Pagination support, OpenAPI schema, async file reading without full memory load._
- [ ] **Create frontend UI**  
  _Display paginated logs with scroll_
- [ ] **CORS config**  
  _Ideally - Dev: allow all. Prod: lock down to known origin(s)._

---

## Developer Experience & Testing

- [ ] **Basic tests**  
  _Include unit tests for the backend file reading + one integration path._
- [ ] **Manual test on large log file (~100MB)**  
  _Ensure no memory blow-up and pagination behaves sanely._
- [ ] **README.md**  
  _Clear run instructions for Linux target. Mention optional Docker setup._

---

## Flex Goals

- [ ] **Production-ready build**
  - [ ] Backend with `gunicorn` + `uvicorn`
  - [ ] Frontend with `vite build`
  - [ ] Optional Dockerfile and `docker-compose.yml`
- [ ] **CI setup**  
  _GitHub Actions or similar to lint, test, and maybe build._
- [ ] **UI Enhancements**
  - [ ] Search by keyword
  - [ ] Jump to first error
  - [ ] Syntax highlighting
  - [ ] Clean styling / layout polish

---

## 🧠 Bonus Ideas

- [ ] ~Optional: sketch how this would work as a VSCode plugin~
