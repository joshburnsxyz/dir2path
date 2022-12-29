import os


supported_shells = {
    "bash": "~/.bashrc",
    "zsh": "~/.zshrc",
}

def run():
    dirp = os.getcwd()
    system_shell_var = os.environ['SHELL'].split("/")
    shell_name = system_shell_var[-1]
    print(shell_name)
    if shell_name in supported_shells:
        print(f"appending {dirp} to {shell_name}")
        quit()
    else:
        print(f"Unsupported shell: {system_shell_var}")
        quit(1)
