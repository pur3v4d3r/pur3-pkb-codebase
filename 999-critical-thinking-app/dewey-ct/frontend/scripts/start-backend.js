/**
 * Spawns the FastAPI backend (uvicorn) as a child process.
 *
 * Key design decisions:
 * - Uses the venv's uvicorn.exe directly (no PATH activation needed)
 * - shell: false — bypasses cmd.exe entirely, which avoids Windows
 *   path-quoting failures caused by the apostrophe in the vault path
 *   (10_pur3v4d3r's-vault).
 */
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const backendDir = path.resolve(__dirname, '../../backend');

// Vault root is 4 levels up: scripts → frontend → dewey-ct → 999-cta → vault
const vaultRoot = path.resolve(__dirname, '../../../..');

// Windows needs the .exe suffix when shell: false is used
const exeSuffix = process.platform === 'win32' ? '.exe' : '';
const venvUvicorn = path.join(vaultRoot, '.venv', 'Scripts', `uvicorn${exeSuffix}`);

const uvicornCmd = fs.existsSync(venvUvicorn) ? venvUvicorn : 'uvicorn';

const proc = spawn(uvicornCmd, ['main:app', '--port', '8000', '--reload'], {
  cwd: backendDir,
  stdio: 'inherit',
  shell: false,   // NO shell — avoids apostrophe-in-path quoting bug
});

proc.on('close', (code) => process.exit(code ?? 0));

