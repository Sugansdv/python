import json
import functools
import os

def param_logger(logfile='cli_log.json'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_entry = {
                "function": func.__name__,
                "args": args,
                "kwargs": kwargs
            }

            # Read existing logs
            if os.path.exists(logfile):
                with open(logfile, 'r') as f:
                    logs = json.load(f)
            else:
                logs = []

            logs.append(log_entry)

            # Write updated logs
            with open(logfile, 'w') as f:
                json.dump(logs, f, indent=4)

            print(f"[LOGGED] Call logged to {logfile}")
            return func(*args, **kwargs)

        return wrapper
    return decorator


@param_logger()
def cli_tool(command, **options):
    print(f"[RUNNING] CLI command: {command} with options {options}")

if __name__ == "__main__":
    cli_tool("init", path="/user/project", verbose=True)
    cli_tool("build", optimize=True, threads=4)
