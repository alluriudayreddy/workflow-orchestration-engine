import time

class TaskExecutor:

    def execute_task(self, task):

        should_fail = False

        if task == "Scan Files":

            if should_fail:
                raise Exception("Scan Failed")
            
            time.sleep(2)
            print("Scanning system files...")


        elif task == "Compress Files":

            if should_fail:
                raise Exception("Compression Failed")

            time.sleep(2)
            print("Compressing backup files...")


        elif task == "Create Backup":

            if should_fail:
                raise Exception("Backup Creation Failed")

            time.sleep(2)
            print("Creating backup archive...")


        elif task == "Verify Backup":

            if should_fail:
                raise Exception("Backup Verification Failed")

            time.sleep(2)
            print("Verifying backup integrity...")


        elif task == "Save Log":

            if should_fail:
                raise Exception("Log Saving Failed")

            time.sleep(2)
            print("Saving backup logs...")


        else:

            print(f"Executing Task: {task}")