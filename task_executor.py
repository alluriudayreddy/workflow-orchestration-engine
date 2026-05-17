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


        elif task == "Load CSV Data":

            if should_fail:
                raise Exception("CSV Loading Failed")

            time.sleep(2)
            print("Loading CSV dataset...")

        elif task == "Clean Missing Values":

            if should_fail:
                raise Exception("Data Cleaning Failed")
            
            time.sleep(2)
            print("Cleaning missing values...")

        elif task == "Transform Records":
            
            if should_fail:
                raise Exception("Data Transformation Failed")

            time.sleep(2)
            print("Transforming datasets records...")

        elif task == "Generate Analytics":
            
            if should_fail:
                raise Exception("Analytics Generation Failed")

            time.sleep(2)
            print("Generating analytics report...")

        elif task == "Export Final Report":
            
            if should_fail:
                raise Exception("Report Export Failed")

            time.sleep(2)
            print("Exporting final processing report...")