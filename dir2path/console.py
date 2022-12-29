import os


supported_shells = {
    "bash": "~/.bashrc",
    "zsh": "~/.zshrc",
}

def run():
    dirp = os.getcwd()
    shell_name = os.environ['SHELL'].split("/")[-1]
    if shell_name in supported_shells:
        shell_config = supported_shells[shell_name]
        path_append_script = f"export PATH=\"$PATH:{dirp}\"\n"
        quit()
    else:
        print(f"Unsupported shell: {system_shell_var}")
        quit(1)
