# predicTCR Development Setup (Windows)

Quick guide to set up the local development environment on Windows.

## Prerequisites

1. **Python 3.11+** - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **pnpm** - Install via PowerShell:
   ```powershell
   iwr https://get.pnpm.io/install.ps1 -useb | iex
   ```

3. **Node.js** - Install via pnpm after pnpm is installed:
   ```powershell
   pnpm env use --global lts
   ```

## CLI Basics (for beginners)

If you're new to the command line, here are some essential navigation commands:

| Command | What it does |
|---------|--------------|
| `cd folder_name` | Go into a folder |
| `cd ..` | Go up one folder (back to parent) |
| `cd ..\..` | Go up two folders |
| `cd \` | Go to the root of the drive |
| `dir` | List files and folders in current directory |
| `pwd` | Show your current location (full path) |

**Example:** If you're in `predicTCR\frontend` and want to go to `predicTCR\backend`:
```powershell
cd ..\backend
```


## Setup Steps

### 1. Clone the Repository

```powershell
git clone https://github.com/ssciwr/predicTCR.git
cd predicTCR
```

### 2. Set Up Backend

Open a terminal in the `backend` folder:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

### 3. Set Up Frontend

Open a terminal in the `frontend` folder:

```powershell
cd frontend
pnpm install
```

## Running the Dev Servers

You'll need **two separate terminals** running at the same time.

### Terminal 1: Backend

```powershell
cd predicTCR\backend
.venv\Scripts\activate
predicTCR_server
```

The backend runs at `http://localhost:8080`

> ⚠️ **Keep this terminal open and running!** Don't close it.

### Terminal 2: Frontend

**Open a new terminal tab** (Ctrl+Shift+T in Windows Terminal, or right-click the tab bar → "New Tab") while keeping Terminal 1 running.

```powershell
cd predicTCR\frontend
pnpm run dev
```

The frontend runs at `http://localhost:5173`

## Access the Site

Open your browser and go to: **http://localhost:5173/**

> **Note:** You'll be automatically logged in as `dev@local` (admin) - no registration needed for local development.
