class WorkflowManager:
    
    def __init__(self):

        self.workflows = {
            "backup": "Backup Workflow",
            "data_processing": "Data Processing Workflow",
            "deployment": "Deployment Workflow"
        }

    def get_workflow(self, workflow_name):
        return self.workflows.get(workflow_name)