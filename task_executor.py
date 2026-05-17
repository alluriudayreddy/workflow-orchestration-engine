class TaskExecutor:

    def execute_task(self, task):

        should_fail = False

        if task == "Scan Files":

            if should_fail:
                raise Exception("Scan Failed")

            print("Scanning system files...")


        elif task == "Compress Files":

            if should_fail:
                raise Exception("Compression Failed")

            print("Compressing backup files...")


        elif task == "Create Backup":

            if should_fail:
                raise Exception("Backup Creation Failed")

            print("Creating backup archive...")


        elif task == "Verify Backup":

            if should_fail:
                raise Exception("Backup Verification Failed")

            print("Verifying backup integrity...")


        elif task == "Save Log":

            if should_fail:
                raise Exception("Log Saving Failed")

            print("Saving backup logs...")


        else:

            print(f"Executing Task: {task}")