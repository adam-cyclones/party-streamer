<centre>
    <img width='200px' src='./silly-logo.png' alt='A really daft logo that made me smile'/>
</centre>

# party-streamer
Tech task: A log streamer

## Meta
- *Unzip logs into `/artifacts` directory*
- [REQUIREMENTS](https://docs.google.com/document/d/18aRtOHwuJSL__AJGflHzg5oI9aoNk-EUYPuvzbJDI7A/edit?tab=t.0) You can see my thoughts on the requirements here.

- Docker is used but I will explain how to use the host machine if you enjoy that sort of thing.
- [TODO](./TODO.md) - I write EVERYTHING down, its just how I work, so here is my TODO list.

## Design
- Web based because I am comfotable with it, could I have done it with Electron or Desktop or VSCode (my repos will answer that with a yes)?
- [TLDRAW](https://www.tldraw.com/p/CL5z-LoIRzng-31hCtqfk?d=v-64.443.1744.1168.page) or [design-ideas.png](./design-ideas.png)

Which translates to this API design:
```
GET /api/logs - List all available log files
GET /api/logs/{id} - Read a specific log file with chunking parameters
GET /api/logs/{id}/search?query={keywords} - Search within a log file
GET /api/logs/{id}/errors - Quick navigation to errors re-using search
```

I will be using FastAPI to make the swagger OpenAPI compliant API.

Even if this idea is horrible, I still want to use MCP to perform searches on tags, I think this will be an interesting learning tool.

# Project Setup

## Prerequisites
- Python 3.9 / (LTS) 
- Node.js 22 / (LTS) 
- Poetry (Python dependency management)
- Git
- Docker (optional)

## Install
0. **Clone the Repository**

### Prod with Docker
```sh
docker compose up
```

### Manual Backend - Python with Poetry

1. **Install Poetry**
Poetry makes it easy install Python projects inside the project directory, using a venv, similar to node.js development in some ways. Follow the docs to install poetry.

[Poetry docs](https://python-poetry.org/docs/)

3. **Install Python Dependencies**
   ```bash
   # Navigate to backend directory
   cd projects/api

   # Install dependencies in project venv
   poetry install
   ```

### Manual Frontend - Vue3 with Vite

1. **Node.js Installation**
   ```bash
   # Recommended: Use nvm (Node Version Manager)
   # Install nvm first: https://github.com/nvm-sh/nvm#installing-and-updating
   
   # Install latest Node.js LTS
   nvm install --lts
   nvm use --lts

   # Alternative: Direct download from nodejs.org
   # Or use package manager (varies by OS and Platform)
   ```

2. **Install Frontend Dependencies**
   ```bash
   # Navigate to frontend directory
   cd projects/ui

   # Install dependencies
   npm i
   ```

## Development Workflow

### Run Backend (FastAPI)
```bash
cd projects/api
poetry run dev
# http://127.0.0.1:9000/docs
```

### Run Frontend (Vite)
```bash
cd projects/ui
npm run dev
```

### Run Tests

#### Backend Tests
```bash
cd projects/api
poetry run pytest
```

#### Frontend Tests
```bash
cd projects/ui
npm run test
```