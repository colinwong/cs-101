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

3. Enable linting with by `PyLint` and `PyCodeStyle` to enforce [PEP 8](https://www.python.org/dev/peps/pep-0008/) style.

   ```
   "python.linting.pylintEnabled": true,
   "python.linting.pycodestyleEnabled": true,

   ```

4. Enable testing with `PyTest`.

   ```
   "python.testing.pytestEnabled": true,
   ```
