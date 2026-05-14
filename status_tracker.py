class StatusTracker:
    def __init__(self):
        self.status = {}

    def set_status(self, workflow_name, current_status):
        self.status[workflow_name] = current_status

    def get_status(self, workflow_name):
        return self.status.get(workflow_name)