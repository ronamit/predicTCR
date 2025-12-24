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

You'll need **two separate terminals**.

### Terminal 1: Backend

```powershell
cd predicTCR\backend
.venv\Scripts\activate
predicTCR_server
```

The backend runs at `http://localhost:8080`

### Terminal 2: Frontend

```powershell
cd predicTCR\frontend
pnpm run dev
```

The frontend runs at `http://localhost:5173`

## Access the Site

Open your browser and go to: **http://localhost:5173/**

> **Note:** You'll be automatically logged in as `dev@local` (admin) - no registration needed for local development.
