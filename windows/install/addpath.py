import os
import sys
import winreg as reg

def add_current_dir_to_path():
    # Get the current directory where the script is running
    executable_path = os.path.abspath(os.getcwd())

    try:
        # Open the system's environment variables (requires admin privileges)
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Environment', 0, reg.KEY_ALL_ACCESS)
        
        # Get the current path
        current_path, _ = reg.QueryValueEx(key, 'Path')

        # Check if the path is already present
        if executable_path not in current_path:
            # Add the new path
            new_path = current_path + ";" + executable_path
            reg.SetValueEx(key, 'Path', 0, reg.REG_EXPAND_SZ, new_path)
            print(f"Added {executable_path} to PATH.")
        else:
            print(f"{executable_path} is already in PATH.")

        reg.CloseKey(key)

        # Refresh environment variables
        os.system("setx /M PATH \"%PATH%\"")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    add_current_dir_to_path()
