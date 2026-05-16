from workflow_manager import WorkflowManager
from status_tracker import StatusTracker

class WorkflowEngine:

    def __init__(self):
        
        self.manager = WorkflowManager()
        self.tracker = StatusTracker()

    def run_workflow(self, workflow_name):
        workflow = self.manager.get_workflow(workflow_name)

        if workflow:
            self.tracker.set_status(workflow_name, "running")

            print(f"\nStarting {workflow_name} workflow...\n")

            for task in workflow:
                print(f"Executing Task: {task}")

            self.tracker.set_status(workflow_name, "completed")

            print(f"\nWorkflow Status: {self.tracker.get_status(workflow_name)}")

        else:
            print("workflow not found.")