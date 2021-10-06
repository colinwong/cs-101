# Setting Up Your Python Environment

## Operating System Considerations

* `Windows`  
   Execute the following command on `Windows Powershell` as admin to allow Python scripts to execute.

   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
   ```

## Environment

1. Create `.env` in your workspace folder and edit it:

   ```
   PYTHONPATH = "class"
   ```
  
2. Edit `.vscode/settings.json` and add:

   ```
   "python.envFile": "${workspaceFolder}/.env",
   ```