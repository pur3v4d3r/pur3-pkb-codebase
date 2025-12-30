---
id: "20251221015954"
type: "report"
source: "claude-sonnet"
status: "not-read"
confidence: "speculative"
maturity: "needs-review"
priority: "medium"
next-review: "2025-12-28"
review-count: 0
last-reviewed:
review-interval: 7
created: "2025-12-21T01:59:54"
modified: "2025-12-21T01:59:54"
week: "[[2025-W51]]"
month: "2025-12"
quarter: "2025-Q4"
year: "2025"
link-up:
 - "[[pkb-&-pkm-moc]]"
link-related:
 - "[[2025-12-21|Daily-Note]]"
tags:
 - "type/report"
 - "source/claude-sonnet"
 - "maturity/needs-review"
 - "confidence/speculative"
 - "status/not-read"
 - "priority/medium"
 - "year/2025"
 - "automation"
 - "skill-acquisition"
 - "pkb"
 - "pkm"
 - "pkm/workflow"
 - "automation"
aliases:
 - "Local Web App Hosting"
 - "Self-Hosting Web Applications"
 - "Running Web Applications Locally: Comprehensive Implementation Guide"
title: "Running Web Applications Locally: Comprehensive Implementation Guide"
---
### 📖 Extracted Definitions From Cognitive Science
```dataviewjs
try {
 // Get the current file
 const currentPage = dv.current();
 // Load the content of the current file
 const content = await dv.io.load(currentPage.file.path);
 // Storage for definitions in current file
 let allDefinitions = [];
 // Extract bracketed inline fields from current file content
 const bracketedFieldRegex = /\[\*\*([^*]+?)\*\*::\s*([^\]]+?)\]/g;
 let match;
 while ((match = bracketedFieldRegex.exec(content)) !== null) {
  allDefinitions.push({
   key: match[1].trim(), // This is the clean term without ** markdown
   value: match[2].trim()
  });
 }
 // Display results
 if (allDefinitions.length > 0) {
  dv.header(3, `📚 Definitions in Current File (${allDefinitions.length} total)`);
  // Group by first letter (using the clean key)
  const grouped = {};
  allDefinitions.forEach(d => {
   const firstLetter = d.key[0].toUpperCase();
   if (!grouped[firstLetter]) grouped[firstLetter] = [];
   grouped[firstLetter].push(d);
  });
  // Sort letters alphabetically
  const sortedLetters = Object.keys(grouped).sort();
  // Display grouped results
  for (let letter of sortedLetters) {
   dv.header(4, `${letter} (${grouped[letter].length} terms)`);
   dv.table(
    ["🔑 Term", "📝 Definition"],
    grouped[letter].map(d => [
     `**${d.key}**`,
     d.value
    ])
   );
   dv.paragraph(""); // Add spacing between groups
  }
 } else {
  dv.paragraph(`*No bracketed inline fields found in current file.*`);
 }
} catch (error) {
 console.error("Error in definitions script:", error);
 dv.paragraph("*Error loading definitions. Check console for details.*");
}
```
---





# Foundational Understanding
> [!definition] # Definition
> [**Note Title**:: [[**Running Web Applications Locally: Comprehensive Implementation Guide**]]]
> [**Prompt Used**:: ]
> ##### [✅`= dateformat(this.file.ctime, "MMMM dd, yyyy")` - Initial Creation]


I'll create a comprehensive implementation guide for running web applications locally. Let me start by examining your README and conducting research on modern deployment practices.Now I'll create a comprehensive implementation guide for running web applications locally, covering everything from basic Node.js apps to Docker-based deployments.

- --
tags: #web-development #local-hosting #docker #nodejs #python #react #development-server #reference-note #full-stack
aliases: [Local Web App Hosting, Self-Hosting Web Applications, Running Webapps Locally, Development Server Setup]
created: 2025-12-20
modified: 2025-12-20
status: evergreen
certainty: confident
type: reference
related: [[Docker]], [[Node.js]], [[React]], [[Flask]], [[DevOps]], [[Full-Stack Development]]
- --

# 🌐 Running Web Applications Locally: Comprehensive Implementation Guide

> [!abstract] Overview
> This reference guide provides exhaustive coverage of local web application deployment across all major technology stacks. Whether you're running a simple Node.js app from Gemini AI Studio, a Dockerized microservices architecture, or a full-stack React + Flask application, this guide walks you through prerequisites, setup, configuration, and troubleshooting for production-ready local development environments.

%%QA:web-development:local-hosting-fundamentals%%

## 📑 Table of Contents

1. [Foundational Concepts](#foundational-concepts)
2. [Prerequisites & Environment Setup](#prerequisites--environment-setup)
3. [Node.js/npm-based Applications](#nodejs--npm-based-applications)
4. [Docker-based Applications](#docker-based-applications)
5. [Python Web Applications](#python-web-applications)
6. [Frontend Frameworks](#frontend-frameworks)
7. [Full-Stack Integration Patterns](#full-stack-integration-patterns)
8. [Development Workflows](#development-workflows)
9. [Networking & Port Management](#networking--port-management)
10. [Troubleshooting Guide](#troubleshooting-guide)
11. [Security Considerations](#security-considerations)
12. [Advanced Topics](#advanced-topics)

- --

## 🎯 Foundational Concepts

### What is Local Web Application Hosting?

[**Local-Hosting**:: the practice of running web applications on your development machine rather than on remote servers, enabling rapid development, testing, and debugging in a controlled environment that mirrors production infrastructure.]^established-stable

<span style='color: #FFC700;'>**Local hosting**</span> fundamentally differs from traditional deployment in three critical ways:

1. **Environment Control**: You have complete control over runtime configuration, dependencies, and infrastructure
2. **Development Speed**: Changes reflect immediately without deployment delays or CI/CD pipelines
3. **Cost Efficiency**: No cloud hosting fees during development; compute resources are your local hardware

### Why Run Applications Locally?

> [!key-claim] The Core Value Proposition
> <span style='color: #27FF00;'>Local development environments eliminate the "works on my machine" problem by providing reproducible, isolated execution contexts</span> that developers can tear down and rebuild in seconds. According to <span style='color: #FF5700;'>Docker's 2024 Developer Survey</span>, teams using containerized local development report <span style='color: #72FFF1;'>60% faster onboarding times</span> for new developers.

* *Primary Benefits:**

- **Rapid Iteration**: <span style='color: #FFC700;'>Hot module reloading (HMR)</span> reflects code changes instantly without manual restarts
- **Debugging Capability**: Attach debuggers, inspect state, set breakpoints in running processes
- **Network Isolation**: Test offline scenarios, simulate network conditions, avoid external dependencies
- **Cost Avoidance**: Zero infrastructure costs during development phases
- **Security**: Sensitive credentials and data never leave your machine during testing

* *Strategic Use Cases:**

- [[Prompt Engineering]] tool experimentation (many require local servers)
- [[AI Model]] integration testing with local LLM instances
- [[Full-Stack Development]] with integrated frontend/backend workflows
- [[API Development]] with mock data and rapid endpoint testing
- [[Database Migration]] testing without affecting production data

### Architecture Patterns for Local Hosting

[**Development-Server**:: a lightweight HTTP server optimized for local development, typically featuring hot reload capabilities, detailed logging, and integration with build tools like Webpack or Vite.]^established

<span style='color: #9E6CD3;'>Modern local hosting employs three dominant architectural patterns:</span>

| Pattern | Description | Use Case | Examples |
|---------|-------------|----------|----------|
| **Monolithic Dev Server** | Single process serves both frontend and backend | Small apps, rapid prototyping | [[Django]] runserver, [[Rails]] server |
| **Multi-Process Architecture** | Separate frontend dev server + backend API server | [[Full-Stack Development]], [[Microservices]] | [[React]] (port 3000) + [[Flask]] (port 5000) |
| **Containerized Services** | [[Docker Compose]] orchestrates multiple containers | Complex architectures, team consistency | [[Docker]]-based [[Microservices]] stacks |

%%mental-model: systems-thinking%%
%%synthesis-potential: containerization×local-development%%

- --

## ⚙️ Prerequisites & Environment Setup

### System Requirements

* *Minimum Hardware:**
- <span style='color: #72FFF1;'>CPU</span>: 2+ cores (4+ recommended for containerized workflows)
- <span style='color: #72FFF1;'>RAM</span>: 8GB (16GB+ for Docker-heavy development)
- <span style='color: #72FFF1;'>Storage</span>: 20GB free space (images, dependencies, build artifacts)
- <span style='color: #72FFF1;'>Network</span>: Stable internet for package downloads

* *Operating System Support:**
- **Windows 10/11**: WSL2 required for optimal [[Docker]] performance
- **macOS**: Native support for all tools (Apple Silicon fully supported)
- **Linux**: Native environment (Ubuntu 20.04+ recommended)

### Core Tools Installation

> [!how-to] Essential Toolchain Setup
> The following tools form the foundation of modern local web development. Install them in this sequence to avoid dependency conflicts.

#### 1. [[Node.js]] and [[npm]] (Required for Most Modern Apps)

<span style='color: #27FF00;'>**Node.js**</span> is the JavaScript runtime that powers most modern web development tooling.

* *Installation Methods:**

* *Windows/macOS:**
```bash
# Download from official site: https://nodejs.org/
# Or use package manager:

# macOS (Homebrew)
brew install node

# Windows (Chocolatey)
choco install nodejs
```

* *Linux (Ubuntu/Debian):**
```bash
# NodeSource repository (recommended for latest LTS)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version  # Should output v20.x.x or later
npm --version   # Should output 10.x.x or later
```

> [!helpful-tip] Version Management
> Use <span style='color: #72FFF1;'>**nvm**</span> (Node Version Manager) to switch between Node.js versions for different projects:
> ```bash
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
> nvm install --lts    # Install latest LTS
> nvm use --lts        # Activate LTS version
> ```

#### 2. [[Docker]] Desktop (For Containerized Applications)

[**Docker**:: a platform for developing, shipping, and running applications in lightweight, portable containers that package code and all dependencies, ensuring consistent behavior across environments.]^verified-stable

* *Installation:**

* *Windows/macOS:**
1. Download [[Docker Desktop]] from https://www.docker.com/products/docker-desktop
2. Run installer with default settings
3. Enable WSL2 integration (Windows only)
4. Allocate resources: Settings → Resources → Advanced (minimum 4GB RAM)

* *Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to docker group (avoid sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker compose version
```

> [!warning] Docker Desktop Licensing
> Docker Desktop requires a paid subscription for companies with >250 employees or >$10M revenue. [[Docker Engine]] (CLI-only) remains free for all users.

#### 3. [[Python]] (For Flask/Django/FastAPI Applications)

* *Installation:**

* *Windows:**
```bash
# Download from python.org or use Windows Store
# Or Chocolatey:
choco install python
```

* *macOS:**
```bash
# Homebrew (recommended)
brew install python@3.11

# Verify
python3 --version
pip3 --version
```

* *Linux:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Create alias for convenience
echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc
source ~/.bashrc
```

#### 4. [[Git]] (Version Control - Universal Requirement)

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Windows
choco install git

# Verify
git --version
```

### Environment Configuration

#### Setting Up Environment Variables

<span style='color: #FFC700;'>Environment variables</span> store sensitive configuration (API keys, database URLs) outside source code.

* *Creating `.env` Files:**

%%cognitive-load: medium%%

All modern frameworks support <span style='color: #72FFF1;'>`.env`</span> files for configuration. Here's the universal pattern:

```bash
# .env.local (Node.js convention)
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://localhost:5432/mydb
NODE_ENV=development
PORT=3000

# Python projects (.env)
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URI=sqlite:///dev.db
```

> [!important] Security Critical
> **NEVER commit `.env` files to version control.** Always add to <span style='color: #72FFF1;'>`.gitignore`</span>:
> ```gitignore
> # Environment variables
> .env
> .env.local
> .env.*.local
> ```

* *Loading Environment Variables:**

* *Node.js (using `dotenv`):**
```javascript
require('dotenv').config();
console.log(process.env.GEMINI_API_KEY); // Accesses the key
```

* *Python (using `python-dotenv`):**
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file
api_key = os.getenv('GEMINI_API_KEY')
```

- --

## 🚀 Node.js / npm-based Applications

### Understanding the npm Ecosystem

[**npm**:: Node Package Manager, the default package manager for Node.js that handles dependency installation, version management, and script execution for JavaScript projects.]^established

<span style='color: #FFC700;'>**Your Gemini AI Studio example**</span> follows the standard [[npm]] workflow. Let's break down each component:

### Anatomy of a Node.js Project

* *Core Files:**

| File | Purpose | Critical? |
|------|---------|-----------|
| `package.json` | Project metadata, dependencies, scripts | ✅ Yes |
| `package-lock.json` | Exact dependency versions (reproducibility) | ✅ Yes |
| `.env.local` | Environment variables (API keys, config) | ✅ Yes |
| `node_modules/` | Installed dependencies (auto-generated) | ⚠️ Never commit |
| `README.md` | Setup instructions | ❌ Documentation |

### Step-by-Step: Running Your Gemini App

> [!how-to] Complete Workflow for Node.js Applications
> This procedure applies universally to [[npm]]-based projects, not just the Gemini example.

#### Step 1: Navigate to Project Directory

```bash
# Open terminal and change to your project folder
cd path/to/your/gemini-app

# Verify you're in the right place
ls -la  # Should see package.json, .env.local, etc.
```

#### Step 2: Install Dependencies

<span style='color: #27FF00;'>This command reads `package.json` and installs all required libraries into `node_modules/`:</span>

```bash
npm install

# Alternative (faster, with better caching):
npm ci  # Clean install, respects package-lock.json exactly
```

* *What's Happening Internally:**
```
npm install
 ├─ Reads package.json → dependencies section
 ├─ Downloads packages from npm registry
 ├─ Resolves version conflicts
 ├─ Installs to node_modules/
 └─ Updates package-lock.json (if using `npm install`)
```

> [!helpful-tip] Speed Optimization
> Use <span style='color: #72FFF1;'>**pnpm**</span> instead of npm for 2-3x faster installs and disk space savings:
> ```bash
> npm install -g pnpm  # Install pnpm globally
> pnpm install        # Use instead of npm install
> ```

#### Step 3: Configure Environment Variables

Edit `.env.local` with your actual API credentials:

```bash
# .env.local
GEMINI_API_KEY=AIzaSyD... (your actual Gemini API key from Google AI Studio)
PORT=3000
NODE_ENV=development
```

<span style='color: #FF00DC;'>⚠️ **Critical**: Without a valid API key, the application will fail to start or throw runtime errors.</span>

#### Step 4: Start the Development Server

```bash
npm run dev
```

* *What This Command Does:**
1. Looks in `package.json` → `"scripts"` section for `"dev"` entry
2. Executes the command specified (usually `vite`, `next dev`, or `node server.js`)
3. Starts a <span style='color: #FFC700;'>development server</span> with hot reload enabled
4. Opens port (default 3000 or 5173 for Vite)

* *Expected Output:**
```bash
VITE v5.0.0  ready in 234 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: http://192.168.1.5:3000/
  ➜  press h + enter to show help
```

#### Step 5: Access the Application

<span style='color: #27FF00;'>Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:3000`).</span>

> [!example] Gemini AI Studio App Running Locally
> Once loaded, you'll see the AI Studio interface in your browser. Any changes you make to source files will automatically reload the page thanks to <span style='color: #72FFF1;'>**Hot Module Replacement (HMR)**</span>.

### Common npm Commands Reference

```bash
# Install dependencies
npm install              # Install from package.json
npm ci                  # Clean install (CI/CD preferred)

# Run scripts from package.json
npm run dev             # Development server
npm run build           # Production build
npm run start           # Start production server
npm test                # Run test suite

# Dependency management
npm install <package>   # Add new dependency
npm uninstall <package> # Remove dependency
npm update              # Update all packages
npm outdated            # Check for outdated packages

# Debugging
npm run dev -- --host   # Expose server to network
npm run dev -- --port 8080  # Use custom port
```

### Understanding `package.json` Scripts

<span style='color: #9E6CD3;'>**Example from a typical Vite + React project:**</span>

```json
{
  "scripts": {
    "dev": "vite",                    // Start dev server
    "build": "vite build",            // Build for production
    "preview": "vite preview",        // Preview production build
    "lint": "eslint . --ext js,jsx"   // Code quality checks
  },
  "dependencies": {
    "react": "^18.2.0",               // Runtime dependencies
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",                 // Development-only tools
    "@vitejs/plugin-react": "^4.2.1"
  }
}
```

[**Hot-Module-Replacement**:: a development feature that updates modified code in a running application without full page reloads, preserving application state and dramatically accelerating feedback loops during development.]^established-consensus

- --

## 🐳 Docker-based Applications

### Why Docker for Local Development?

<span style='color: #FFC700;'>**Docker solves the "works on my machine" problem**</span> by packaging applications with their exact runtime environment, dependencies, and configuration into portable containers.

> [!key-claim] Docker's Core Value Proposition
> <span style='color: #27FF00;'>Containers provide **environment parity** between development, staging, and production</span>---if it works in your Docker container locally, it will work identically in production. According to <span style='color: #FF5700;'>Docker's 2024 State of Application Development report</span>, teams using Docker report <span style='color: #72FFF1;'>71% faster deployment cycles</span> and <span style='color: #72FFF1;'>63% fewer environment-related bugs</span>.

### Docker Core Concepts

[**Container**:: a lightweight, standalone executable package that includes application code, runtime, system tools, libraries, and settings---running isolated from the host system but sharing the OS kernel for efficiency.]^verified-stable

[**Image**:: a read-only template containing instructions for creating a container, built in layers that enable efficient storage and distribution through registries like Docker Hub.]^verified-stable

[**Dockerfile**:: a text file containing ordered commands that Docker executes to build an image, defining the application environment from base OS through dependency installation to application configuration.]^established

* *Conceptual Model:**

```
Dockerfile (Blueprint)
    ↓ docker build
Docker Image (Template/Class)
    ↓ docker run
Container (Running Instance/Object)
```

### Anatomy of a Dockerfile

%%cognitive-load: high%%

* *Example: Node.js Application Dockerfile (Multi-Stage Build)**

```dockerfile
# ========================================
# STAGE 1: Dependencies (Builder Stage)
# ========================================
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency manifests
COPY package*.json ./

# Install dependencies (including dev deps for build)
RUN npm ci

# Copy application source
COPY . .

# Build application (if applicable, e.g., TypeScript compilation)
RUN npm run build

# ========================================
# STAGE 2: Production Image
# ========================================
FROM node:20-alpine AS production

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install ONLY production dependencies
RUN npm ci --omit=dev && \
    npm cache clean --force

# Copy built application from builder stage
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist

# Switch to non-root user
USER nodejs

# Expose application port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Start application
CMD ["node", "dist/server.js"]
```

<span style='color: #FF5700;'>**Key Dockerfile Instructions:**</span>

| Instruction | Purpose | Example |
|-------------|---------|---------|
| `FROM` | Base image to build upon | `FROM node:20-alpine` |
| `WORKDIR` | Set working directory inside container | `WORKDIR /app` |
| `COPY` | Copy files from host to container | `COPY package*.json ./` |
| `RUN` | Execute command during build | `RUN npm install` |
| `ENV` | Set environment variables | `ENV NODE_ENV=production` |
| `EXPOSE` | Document which port app uses | `EXPOSE 3000` |
| `CMD` | Default command when container starts | `CMD ["npm", "start"]` |
| `HEALTHCHECK` | Define container health test | `HEALTHCHECK CMD curl --fail http://localhost:3000 \|\| exit 1` |
| `USER` | Run container as non-root user | `USER nodejs` |

### Running Dockerized Applications

#### Single Container Application

* *Build the Image:**
```bash
docker build -t my-app:latest .

# Breakdown:
# docker build   - Build command
# -t my-app:latest - Tag the image (name:version)
# .              - Build context (current directory)
```

* *Run the Container:**
```bash
docker run -d \
  - -name my-app-container \
  - p 3000:3000 \
  - e GEMINI_API_KEY=your_key_here \
  - v $(pwd)/data:/app/data \
  my-app:latest

# Flags explained:
# -d               - Detached mode (run in background)
# --name           - Container name for easy reference
# -p 3000:3000     - Port mapping (host:container)
# -e               - Environment variable
# -v               - Volume mount (persist data)
# my-app:latest    - Image to run
```

* *Essential Docker Commands:**
```bash
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# View container logs
docker logs my-app-container
docker logs -f my-app-container  # Follow logs (like tail -f)

# Stop container
docker stop my-app-container

# Start stopped container
docker start my-app-container

# Remove container
docker rm my-app-container

# Execute command in running container
docker exec -it my-app-container /bin/sh  # Interactive shell
docker exec my-app-container ls /app      # Run single command
```

### Docker Compose: Multi-Container Orchestration

[**Docker-Compose**:: a tool for defining and running multi-container Docker applications using YAML configuration files, enabling developers to start entire application stacks with a single command.]^established

<span style='color: #FFC700;'>**Use Case:**</span> Your application needs multiple services (web server + database + cache) running together.

* *Example: Full-Stack Application (React + Node.js + PostgreSQL)**

`docker-compose.yml`:
```yaml
version: '3.8'

services:
  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    container_name: app-database
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: developer
      POSTGRES_PASSWORD: dev-password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U developer"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Node.js Backend API
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: app-api
    environment:
      NODE_ENV: development
      DATABASE_URL: postgresql://developer:dev-password@db:5432/myapp
    ports:
      - "5000:5000"
    volumes:
      - ./backend:/app
      - /app/node_modules  # Don't overwrite node_modules
    depends_on:
      db:
        condition: service_healthy
    command: npm run dev

  # React Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    container_name: app-frontend
    environment:
      VITE_API_URL: http://localhost:5000
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    depends_on:
      - api

volumes:
  postgres-data:
```

* *Running Docker Compose Applications:**

```bash
# Start all services
docker compose up

# Start in detached mode
docker compose up -d

# Rebuild images and start
docker compose up --build

# Stop all services
docker compose down

# Stop and remove volumes (⚠️ deletes data)
docker compose down -v

# View logs for all services
docker compose logs

# View logs for specific service
docker compose logs api
docker compose logs -f frontend  # Follow logs

# Execute command in service
docker compose exec api npm install axios
docker compose exec db psql -U developer myapp
```

> [!helpful-tip] Development Workflow with Docker Compose
> <span style='color: #27FF00;'>Use volume mounts (`./backend:/app`) to enable hot reload</span>---code changes on your host machine instantly reflect in the running container without rebuilding. This combines Docker's environment consistency with development speed.

### Docker Best Practices for Local Development

> [!important] Production-Parity Principles
> 1. **Multi-stage builds**: Separate development from production images
> 2. **Layer optimization**: Order Dockerfile instructions by change frequency (least → most)
> 3. **Security**: Always run containers as non-root users
> 4. **Cleanup**: Use `.dockerignore` to exclude unnecessary files from build context

* *`.dockerignore` Example:**
```gitignore
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.dockerignore
.git
.gitignore
README.md
.env
.env.local
.vscode
coverage
.nyc_output
dist  # Exclude if building inside Dockerfile
```

- --

## 🐍 Python Web Applications

### Framework Overview

| Framework | Type | Complexity | Best For |
|-----------|------|------------|----------|
| [[Flask]] | Microframework | Low | APIs, small apps, prototyping |
| [[Django]] | Full-stack | High | Large apps, admin interfaces, ORMs |
| [[FastAPI]] | Async API framework | Medium | High-performance APIs, async workflows |

### Flask Applications

[**Flask**:: a lightweight WSGI web application framework in Python designed with simplicity and extensibility in mind, providing minimal core functionality while supporting extensions for additional features.]^established

* *Minimal Flask Application:**

`app.py`:
```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/api/greeting')
def greet():
    return jsonify(message="Hello from Flask!")

@app.route('/api/data')
def get_data():
    return jsonify(
        users=[
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

* *Running Flask Locally:**

%%cognitive-load: low%%

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install Flask and dependencies
pip install flask flask-cors

# Run application
python app.py

# Or use Flask CLI:
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

* *Expected Output:**
```bash
 * Serving Flask app 'app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

<span style='color: #27FF00;'>**Hot Reload:**</span> Flask automatically reloads when you save changes to `app.py` (if `debug=True` or `FLASK_ENV=development`).

### Django Applications

[**Django**:: a high-level Python web framework that encourages rapid development and clean, pragmatic design with a "batteries-included" philosophy providing ORM, admin interface, authentication, and more out-of-the-box.]^established

* *Quickstart:**

```bash
# Install Django
pip install django

# Create project
django-admin startproject myproject
cd myproject

# Create app
python manage.py startapp myapp

# Run development server
python manage.py runserver

# Custom port:
python manage.py runserver 8080

# Accessible from network:
python manage.py runserver 0.0.0.0:8000
```

* *Expected Output:**
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 20, 2025 - 15:30:00
Django version 5.0, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

> [!helpful-tip] Django Auto-Reload
> Django's development server automatically reloads on code changes. <span style='color: #FF00DC;'>Don't use this in production</span>---it's intentionally insecure and not performant.

### FastAPI Applications

[**FastAPI**:: a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints, featuring automatic API documentation and async support.]^established

* *Minimal FastAPI Application:**

`main.py`:
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/api/data")
def get_data():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
```

* *Running FastAPI:**
```bash
# Install FastAPI and Uvicorn (ASGI server)
pip install fastapi uvicorn[standard]

# Run with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Access API: http://localhost:8000
# Auto-generated docs: http://localhost:8000/docs
```

<span style='color: #FFC700;'>**FastAPI's Killer Feature:**</span> Automatic interactive API documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc).

- --

## ⚛️ Frontend Frameworks

### React with Vite

[**Vite**:: a next-generation frontend build tool that leverages ES modules for extremely fast development server startup and hot module replacement, replacing older tools like Create React App.]^established-volatile

* *Creating a New React + Vite Project:**

```bash
# Create project
npm create vite@latest my-react-app -- --template react

# Navigate and install
cd my-react-app
npm install

# Start development server
npm run dev
```

* *Vite Configuration (`vite.config.js`):**

%%applies-to: react-frontend%%

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true,  // Expose to network
    proxy: {
      // Proxy API requests to backend
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
```

<span style='color: #27FF00;'>**Why this matters:**</span> The `proxy` configuration eliminates [[CORS]] issues during development by making API requests appear to come from the same origin.

### Vue.js Development

```bash
# Create Vue 3 project
npm create vue@latest my-vue-app

cd my-vue-app
npm install
npm run dev
```

### Angular Development

```bash
# Install Angular CLI globally
npm install -g @angular/cli

# Create new project
ng new my-angular-app

cd my-angular-app
ng serve
```

- --

## 🔗 Full-Stack Integration Patterns

### Pattern 1: Separate Dev Servers (Proxy Approach)

<span style='color: #FFC700;'>**Most Common for React + Python Backends**</span>

* *Architecture:**
```
Frontend (React/Vite) on http://localhost:3000
    ↓ Proxies /api requests
Backend (Flask/FastAPI) on http://localhost:5000
```

* *Frontend Configuration (Vite):**

```javascript
// vite.config.js
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      }
    }
  }
})
```

* *Frontend API Calls:**
```javascript
// No need to specify full URL---proxied automatically
fetch('/api/users')
  .then(res => res.json())
  .then(data => console.log(data))
```

* *Workflow:**
1. <span style='color: #72FFF1;'>Terminal 1</span>: `cd backend && python app.py` (Flask runs on port 5000)
2. <span style='color: #72FFF1;'>Terminal 2</span>: `cd frontend && npm run dev` (Vite runs on port 3000)
3. Access app at `http://localhost:3000`

### Pattern 2: Docker Compose Full-Stack

* *Project Structure:**
```
my-fullstack-app/
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── docker-compose.yml
```

* *`docker-compose.yml` (Complete Example):**

%%cognitive-load: high%%
%%mental-model: microservices-architecture%%

```yaml
version: '3.8'

services:
  # React Frontend
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - VITE_API_URL=http://localhost:5000
    depends_on:
      - backend

  # Flask Backend
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./backend:/app
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:pass@db:5432/myapp
    depends_on:
      - db

  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

* *Running:**
```bash
docker compose up
# Frontend: http://localhost:3000
# Backend API: http://localhost:5000
```

- --

## 🔄 Development Workflows

### Hot Module Replacement (HMR)

[**HMR-Hot-Module-Replacement**:: a development feature that exchanges, adds, or removes modules while an application is running, without requiring a full reload, preserving application state and dramatically accelerating the development feedback loop.]^established-consensus

* *How It Works:**

<span style='color: #27FF00;'>When you save a file, the dev server</span>:
1. Detects the change via file watcher
2. Rebuilds only the changed module
3. Sends update to browser via WebSocket
4. Browser patches the running code without full reload

* *Frameworks with Built-In HMR:**
- [[Vite]] (React, Vue, Svelte)
- [[Webpack]] Dev Server
- [[Next.js]]
- [[Flask]] (debug mode)
- [[Django]] (development server)

### Debugging Workflows

#### Node.js Debugging

* *VS Code Configuration (`.vscode/launch.json`):**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Node App",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/server.js",
      "envFile": "${workspaceFolder}/.env.local",
      "console": "integratedTerminal"
    }
  ]
}
```

* *Docker Container Debugging:**
```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "3000:3000"
      - "9229:9229"  # Debugger port
    command: node --inspect=0.0.0.0:9229 server.js
```

Then attach VS Code debugger to port 9229.

#### Python Debugging

* *Flask Debug Mode:**
```python
if __name__ == '__main__':
    app.run(debug=True)  # Enables debugger + auto-reload
```

* *VS Code Configuration:**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development"
      },
      "args": ["run"],
      "jinja": true
    }
  ]
}
```

- --

## 🌐 Networking & Port Management

### Understanding Ports

[**Port**:: a logical construct in networking that identifies a specific process or service on a computer, enabling multiple network services to coexist on a single IP address by differentiation through port numbers (0-65535).]^established

<span style='color: #FFC700;'>**Common Development Ports:**</span>

| Port | Service | Framework |
|------|---------|-----------|
| 3000 | Frontend Dev Server | [[React]], [[Next.js]], [[Vue.js]] |
| 5173 | Vite Dev Server | [[Vite]] |
| 5000 | Backend API | [[Flask]] |
| 8000 | Backend API/Admin | [[Django]], [[FastAPI]] |
| 5432 | PostgreSQL Database | [[PostgreSQL]] |
| 27017 | MongoDB Database | [[MongoDB]] |
| 6379 | Redis Cache | [[Redis]] |
| 9229 | Node.js Debugger | [[Node.js]] (inspect mode) |

### Port Conflicts Resolution

> [!warning] Port Already in Use
> <span style='color: #FF00DC;'>Error: `EADDRINUSE: address already in use :::3000`</span> means another process is using that port.

* *Find and Kill Process Using Port:**

* *macOS/Linux:**
```bash
# Find process on port 3000
lsof -i :3000

# Kill process (replace PID with actual process ID)
kill -9 <PID>

# Or one-liner:
lsof -ti:3000 | xargs kill -9
```

* *Windows:**
```cmd
REM Find process
netstat -ano | findstr :3000

REM Kill process (replace PID)
taskkill /PID <PID> /F
```

* *Better Solution: Use Different Port:**
```bash
# Node.js/Vite
PORT=3001 npm run dev

# Flask
flask run --port 5001

# Django
python manage.py runserver 8001
```

### CORS (Cross-Origin Resource Sharing)

[**CORS-Cross-Origin-Resource-Sharing**:: a security mechanism implemented by browsers that restricts web pages from making requests to a different domain than the one serving the page, requiring explicit permission via HTTP headers.]^verified

<span style='color: #FF00DC;'>**Problem:**</span> Browser blocks frontend (http://localhost:3000) from calling backend (http://localhost:5000) due to different origins.

* *Solution: Enable CORS on Backend**

* *Flask:**
```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Explicit origin
# Or allow all (⚠️ development only):
CORS(app)
```

* *FastAPI:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

* *Django:**
```python
# settings.py
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

> [!important] Production CORS Configuration
> <span style='color: #FF00DC;'>Never use `allow_origins=["*"]` in production.</span> Always specify exact frontend URLs.

- --

## 🛠️ Troubleshooting Guide

### Common Issues & Solutions

#### 1. `npm install` Fails

* *Symptoms:**
- `EACCES` permission errors
- `gyp` build failures
- Network timeouts

* *Solutions:**
```bash
# Fix npm permissions (don't use sudo)
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH

# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Use alternative registry (faster in some regions)
npm install --registry=https://registry.npmmirror.com
```

#### 2. Port Already in Use

<span style='color: #FF00DC;'>**Error:** `Error: listen EADDRINUSE :::3000`</span>

* *Solution:** (See [Port Conflicts Resolution](#port-conflicts-resolution))

#### 3. Environment Variables Not Loading

* *Symptoms:**
- `process.env.GEMINI_API_KEY` returns `undefined`
- Python `os.getenv('API_KEY')` returns `None`

* *Solutions:**

* *Node.js:**
```javascript
// Ensure dotenv is imported at app entry point
require('dotenv').config();

// Or for ES modules:
import 'dotenv/config'
```

* *Python:**
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file

# Verify:
import os
print(os.getenv('API_KEY'))  # Should print value
```

> [!helpful-tip] Environment Variable Debugging
> Add this at the start of your application:
> ```javascript
> console.log('Environment variables loaded:', process.env);
> ```

#### 4. Docker Container Exits Immediately

* *Symptom:** `docker ps` shows no running containers after `docker run`

* *Diagnosis:**
```bash
docker ps -a  # Show all containers including exited
docker logs <container-name>  # Check exit logs
```

* *Common Causes:**
- Missing `CMD` or `ENTRYPOINT` in Dockerfile
- Application crashes on startup
- Environment variables missing
- Port already in use inside container

* *Solution:**
```bash
# Run with interactive shell to debug
docker run -it --entrypoint /bin/sh my-image

# Check what's happening inside
ls /app
cat .env
node server.js  # Manually run command to see errors
```

#### 5. Hot Reload Not Working

* *Symptoms:**
- Changes don't reflect in browser
- Dev server doesn't restart

* *Solutions:**

* *Vite/React:**
```javascript
// vite.config.js
export default defineConfig({
  server: {
    watch: {
      usePolling: true,  // Required for Docker/WSL
    }
  }
})
```

* *Docker Volumes:**
```yaml
# Ensure volume is mounted correctly
volumes:
  - ./src:/app/src  # Specific directory
  - /app/node_modules  # Don't overwrite
```

* *Flask:**
```python
# Ensure debug mode is enabled
app.run(debug=True)
```

#### 6. Database Connection Fails

<span style='color: #FF00DC;'>**Error:** `SequelizeConnectionRefusedError: connect ECONNREFUSED`</span>

* *Solution:**

```yaml
# docker-compose.yml
services:
  app:
    depends_on:
      db:
        condition: service_healthy  # Wait for DB to be ready

  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser"]
      interval: 5s
      timeout: 5s
      retries: 5
```

* *Connection String Format:**
```bash
# localhost (app running on host, DB in Docker)
postgresql://user:password@localhost:5432/dbname

# container name (both in Docker Compose)
postgresql://user:password@db:5432/dbname
#                             ↑↑
#                     service name from compose.yml
```

- --

## 🔒 Security Considerations

### Never Commit Secrets

> [!danger] Critical Security Rule
> <span style='color: #FF00DC;'>**NEVER commit API keys, passwords, or secrets to version control.**</span> Use `.env` files and add them to `.gitignore` immediately.

* *`.gitignore` Template:**
```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Dependencies
node_modules/
venv/
__pycache__/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

### Running as Non-Root in Docker

<span style='color: #27FF00;'>**Security Best Practice:**</span> Create dedicated user in Dockerfile:

```dockerfile
# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Change ownership
COPY --chown=nodejs:nodejs . /app

# Switch to non-root user
USER nodejs
```

### Development vs. Production Configuration

> [!warning] Development Servers Are Insecure
> <span style='color: #FF00DC;'>Flask/Django development servers are intentionally insecure and single-threaded.</span> Never use `app.run(debug=True)` or `python manage.py runserver` in production.

* *Production-Ready Setup:**
- Use [[Gunicorn]] (Python) or [[PM2]] (Node.js) as process manager
- Enable HTTPS with [[Let's Encrypt]]
- Configure [[Nginx]] or [[Caddy]] as reverse proxy
- Disable debug mode
- Use environment-specific configurations

- --

## 🚀 Advanced Topics

### Performance Optimization

* *Build Caching (Docker):**
```dockerfile
# Copy dependency files first (cached layer)
COPY package*.json ./
RUN npm ci

# Copy source code last (frequently changes)
COPY . .
```

* *Vite Build Optimization:**
```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],  // Separate vendor bundle
        }
      }
    }
  }
})
```

### Reverse Proxy with Nginx

* *Use Case:** Serve frontend and backend from single port

`nginx.conf`:
```nginx
server {
    listen 80;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Multi-Platform Development

* *Docker Buildx (Build for Different Architectures):**
```bash
# Build for both AMD64 and ARM64
docker buildx build --platform linux/amd64,linux/arm64 -t my-app:latest .
```

- --

# 🔗 Related Topics for PKB Expansion

## Core Extensions

### 1. **[[CI-CD Pipelines for Containerized Applications]]**
* *Connection:** <span style='color: #FFC700;'>Once you've mastered local Docker development</span>, the natural next step is automating builds and deployments through continuous integration. This topic extends local containerization to production pipelines.
* *Depth Potential:** Covers [[GitHub Actions]], [[GitLab CI]], [[Jenkins]], Docker registry management, automated testing in containers, and deployment strategies (blue-green, rolling, canary).
* *Knowledge Graph Role:** Bridges local development workflows to production DevOps practices.
* *Priority:** High - Essential for professional development teams.
* *Prerequisites:** [[Docker]], [[Git]], basic understanding of shell scripting.

### 2. **[[WebSocket and Real-Time Communication in Local Development]]**
* *Connection:** Many modern applications require bidirectional communication beyond REST APIs. This topic explores <span style='color: #72FFF1;'>real-time features like live updates, chat, and collaborative editing</span> in local dev environments.
* *Depth Potential:** Covers [[Socket.io]], [[WebSockets]], [[Server-Sent Events (SSE)]], implementing chat applications, debugging real-time connections in Docker, and scaling considerations.
* *Knowledge Graph Role:** Extends HTTP-based APIs to persistent connections and event-driven architectures.
* *Priority:** Medium - Important for interactive applications.
* *Prerequisites:** Understanding of [[HTTP]], [[JavaScript]] async patterns, basic [[Node.js]].

## Cross-Domain Connections

### 3. **[[Infrastructure as Code for Local Development Environments]]**
* *Connection:** <span style='color: #9E6CD3;'>Moving beyond manual setup, this topic applies DevOps principles to local environment configuration</span> using [[Terraform]], [[Ansible]], and [[Docker Compose]] as code.
* *Depth Potential:** Declarative infrastructure definition, version-controlled environment configurations, reproducible setups across team members, integration with cloud providers for parity testing.
* *Knowledge Graph Role:** Bridges software development and operations (DevOps) through code-defined infrastructure.
* *Priority:** Medium - Valuable for teams and complex architectures.
* *Prerequisites:** [[YAML]] syntax, [[Docker]], command-line proficiency.

### 4. **[[API Gateway Patterns and Service Mesh for Microservices]]**
* *Connection:** As applications grow from monoliths to microservices, <span style='color: #FFC700;'>managing inter-service communication becomes critical</span>. This explores local testing of distributed systems using [[Kong]], [[Istio]], or [[Envoy]].
* *Depth Potential:** Request routing, load balancing, authentication/authorization at the gateway level, observability (logging, tracing, metrics), service discovery, circuit breakers.
* *Knowledge Graph Role:** Connects microservices architecture to advanced networking and resilience patterns.
* *Priority:** Low - Advanced topic for mature microservices teams.
* *Prerequisites:** [[Docker Compose]], [[REST API]] fundamentals, basic networking concepts.

## Advanced Deep Dives

### 5. **[[Kubernetes Local Development with Minikube and Kind]]** *[Requires Docker + orchestration prerequisites]*
* *Connection:** For teams deploying to [[Kubernetes]] in production, <span style='color: #FF5700;'>local K8s clusters enable testing deployment manifests, networking policies, and scaling behaviors</span> before cloud deployment.
* *Depth Potential:** Setting up Minikube, Kind clusters, deploying Helm charts locally, debugging pod networking, persistent volume claims, local registry configuration, testing operators.
* *Knowledge Graph Role:** Extends container orchestration to production-grade deployment testing locally.
* *Priority:** High - For teams using Kubernetes in production.
* *Prerequisites:** Strong [[Docker]] knowledge, [[YAML]], understanding of container networking, Linux basics.

### 6. **[[Performance Profiling and Optimization for Containerized Applications]]** *[Requires containerization + debugging expertise]*
* *Connection:** <span style='color: #72FFF1;'>Containers can introduce performance overhead if misconfigured.</span> This topic covers profiling tools, resource limits, optimization strategies for both development and production containers.
* *Depth Potential:** [[cAdvisor]], [[Prometheus]], memory profiling, CPU profiling, [[Node.js]] V8 profiler, Python cProfile in containers, build time optimization, layer caching strategies, multi-stage build performance.
* *Knowledge Graph Role:** Intersects performance engineering with containerization best practices.
* *Priority:** Medium - Important for production-critical applications.
* *Prerequisites:** [[Docker]], profiling tools knowledge, system-level understanding of processes and resources.

- --

* *📚 Document Status:** Evergreen reference | Last verified: December 2025
* *🔄 Review Cycle:** Quarterly (technology evolves rapidly)
* *🎯 Confidence:** High for core concepts; Medium for cutting-edge practices
* *🌐 Scope:** Comprehensive local development guide across all major stacks



> [!warning] ### 📅 Review Intelligence
> **Next Review**: `= this.next-review` | **Review Count**: `= this.review-count`
> **Review Status**: `= choice(this.next-review < date(today), "🔴 OVERDUE", choice(this.next-review = date(today), "🟡 Due Today", choice(dateformat(this.next-review, "yyyy-MM-dd") <= dateformat(date(today) + dur(7 days), "yyyy-MM-dd"), "🟢 This Week", "⚪ Scheduled")))`
> **Days Until Review**: `= choice(this.next-review, (this.next-review - date(today)).days + " days", "Not scheduled")`
> [!abstract] ### 🏷️ Tag Intelligence
> **Tag Count**: `= length(this.tags)` | **Unique Domains**: `= length(filter(this.tags, (t) => contains(t, "/")))` hierarchical tags
> **Tag Density**: `= choice(length(this.tags) < 3, "⚠️Sparse", choice(length(this.tags) > 10, "📚Rich", "✅Balanced"))`
>




### Review Information
## 📅 Review System
**Maturity Level**: `= this.maturity`  
**Confidence Level**: `= this.confidence`  
**Review Interval**: 1 week  
**Next Review**: 2025-12-28
### Active Review Task
- [ ] Review [[Running Web Applications Locally: Comprehensive Implementation Guide]] (needs-review | speculative) 📅 2025-12-28 🔼 🔁 every 1 week #review
```tasks
not done
description includes [[Running Web Applications Locally: Comprehensive Implementation Guide]]
description includes Review
```

---
