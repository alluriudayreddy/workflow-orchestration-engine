from datetime import datetime

def write_log(message, level="INFO"):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_log = f"[{timestamp}] [{level}] [{message}]"

    with open("logs/execution_log.txt", "a") as log_file:
        log_file.write(formatted_log + "\n")
