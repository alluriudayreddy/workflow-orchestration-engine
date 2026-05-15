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

            print(f"Starting {workflow}...")
            print(f"Status: {self.tracker.get_status(workflow_name)}")

            self.tracker.set_status(workflow_name, "completed")

            print(f"Status: {self.tracker.get_status(workflow_name)}")

        else:
            print("workflow not found.")