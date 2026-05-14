from workflow_manager import WorkflowManager

class workflowEngine:

    def __init__(self):
        self.manager = WorkflowManager()

    def run_workflow(self, workflow_name):
        workflow = self.manager.get_workflow(workflow_name)

        if workflow:
            print(f"Starting {workflow}...")

        else:
            print("Workflow not found.")