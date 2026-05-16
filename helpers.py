def write_log(message):
    
    with open("logs/execution_log.txt", "a") as log_file:
        log_file.write(message + "\n")