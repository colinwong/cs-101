# Setting Up Your Test Environment

## Environment

1. Create `.env` in your workspace folder and edit it:

   ```
   PYTHONPATH = "class/put/your/subdirectories/here"
   ```
  
2. Edit `.vscode/settings.json` and add:

   ```
   "python.envFile": "${workspaceFolder}/.env",
   ```
