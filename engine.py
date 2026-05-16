from workflow_manager import WorkflowManager
from status_tracker import StatusTracker
from task_executor import TaskExecutor
from helpers import write_log

class WorkflowEngine:

    def __init__(self):
        self.executor = TaskExecutor()

        self.manager = WorkflowManager()
        self.tracker = StatusTracker()

    def run_workflow(self, workflow_name):
        workflow = self.manager.get_workflow(workflow_name)

        if workflow:
            self.tracker.set_status(workflow_name, "running")

            print(f"\nStarting {workflow_name} workflow...\n")
            write_log(f"Starting {workflow_name} workflow...")

            for task in workflow:
                self.executor.execute_task(task)
                write_log(f"Executing Task: {task}")

            self.tracker.set_status(workflow_name, "completed")
            write_log(f"{workflow_name} workflow completed")

            print(f"\nWorkflow Status: {self.tracker.get_status(workflow_name)}")

        else:
            print("workflow not found.")