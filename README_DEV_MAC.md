# predicTCR Development Setup (macOS)

Quick guide to set up the local development environment on macOS.

## Prerequisites

1. **Python 3.11+** - Install via Homebrew:
   ```bash
   brew install python@3.11
   ```
   Or download from [python.org](https://www.python.org/downloads/)

2. **pnpm** - Install via Homebrew:
   ```bash
   brew install pnpm
   ```
   Or via the install script:
   ```bash
   curl -fsSL https://get.pnpm.io/install.sh | sh -
   ```

3. **Node.js** - Install via pnpm after pnpm is installed:
   ```bash
   pnpm env use --global lts
   ```

## CLI Basics (for beginners)

If you're new to the command line, here are some essential navigation commands:

| Command | What it does |
|---------|--------------|
| `cd folder_name` | Go into a folder |
| `cd ..` | Go up one folder (back to parent) |
| `cd ../..` | Go up two folders |
| `cd ~` | Go to your home directory |
| `cd /` | Go to the root of the filesystem |
| `ls` | List files and folders in current directory |
| `pwd` | Show your current location (full path) |

**Example:** If you're in `predicTCR/frontend` and want to go to `predicTCR/backend`:
```bash
cd ../backend
```


## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/ssciwr/predicTCR.git
cd predicTCR
```

### 2. Set Up Backend

Open a terminal in the `backend` folder:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Set Up Frontend

Open a terminal in the `frontend` folder:

```bash
cd frontend
pnpm install
```

## Running the Dev Servers

You'll need **two separate terminals** running at the same time.

### Terminal 1: Backend

```bash
cd predicTCR/backend
source .venv/bin/activate
predicTCR_server
```

The backend runs at `http://localhost:8080`

> ⚠️ **Keep this terminal open and running!** Don't close it.

### Terminal 2: Frontend

**Open a new terminal tab** (Cmd+T in Terminal.app, or right-click → "New Tab") while keeping Terminal 1 running.

```bash
cd predicTCR/frontend
pnpm run dev
```

The frontend runs at `http://localhost:5173`

## Access the Site

Open your browser and go to: **http://localhost:5173/**

> **Note:** You'll be automatically logged in as `dev@local` (admin) - no registration needed for local development.
