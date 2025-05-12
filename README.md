# party-streamer
Tech task: A log streamer

## Meta
- You can see my thoughts on the requirements here:
https://docs.google.com/document/d/18aRtOHwuJSL__AJGflHzg5oI9aoNk-EUYPuvzbJDI7A/edit?tab=t.0
- Docker is not going to be used to ship or develop this, to give you a better chance to review.

## Design
- Web based because I am comfotable with it, could I have done it with Electron or Desktop?
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

## Install
### Backend - python, poetry
```sh

```

### UI - Node, vue3 (vite)
#### 1. node.js**
```sh

```


#### 2. Vue 3 - Vite
```sh

```

## Run
### Backend 
...
### UI
...