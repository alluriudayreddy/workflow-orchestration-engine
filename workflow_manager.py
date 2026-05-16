from workflows.backup_workflow import backup_workflow
from workflows.data_processing_workflow import data_processing_workflow
from workflows.deployment_workflow import deployment_workflow

class WorkflowManager:
    
    def __init__(self):

        self.workflows = {
            "backup": backup_workflow,
            "data_processing": data_processing_workflow,
            "deployment": deployment_workflow
        }

    def get_workflow(self, workflow_name):
        return self.workflows.get(workflow_name)