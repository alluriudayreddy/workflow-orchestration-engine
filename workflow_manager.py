from workflows.backup_workflow import backup_workflow

class WorkflowManager:
    
    def __init__(self):

        self.workflows = {
            "backup": backup_workflow
        }

    def get_workflow(self, workflow_name):
        return self.workflows.get(workflow_name)