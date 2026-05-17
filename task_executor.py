class TaskExecutor:

    def execute_task(self, task):

        if task == "Compress Files":
            raise Exception("Compression Failed")
        print(f"Executing Task: {task}")