from workflow_manager import WorkflowManager
from status_tracker import StatusTracker
from task_executor import TaskExecutor
from helpers import write_log, log_seperator


class WorkflowEngine:

    def __init__(self):

        self.executor = TaskExecutor()
        self.manager = WorkflowManager()
        self.tracker = StatusTracker()


    def run_workflow(self, workflow_name):

        workflow = self.manager.get_workflow(workflow_name)

        if workflow:

            log_seperator()

            try:

                self.tracker.set_status(workflow_name, "running")
                print(f"Workflow Status: {self.tracker.get_status(workflow_name)}")

                print(f"\nStarting {workflow_name} workflow...\n")
                write_log(f"Starting {workflow_name} workflow...", "INFO")

                for task in workflow:

                    max_retries = 3
                    retry_count = 0

                    while retry_count <= max_retries:

                        try:
                            self.executor.execute_task(task)
                            write_log(f"Executing task: {task}", "INFO")
                            break

                        except Exception as error:
                            retry_count += 1

                            print(f"Retrying {task}...Attempt {retry_count}")
                            write_log(f"Retrying {task}...Attempt {retry_count}", "WARNING")

                            print(f"Task Failed: {error}")
                            write_log(f"Task Failed: {error}", "ERROR")

                            if retry_count > max_retries:
                                raise Exception(f"{task} failed after retries")


                self.tracker.set_status(workflow_name, "completed")

                write_log(f"{workflow_name} workflow completed", "SUCCESS")

                print(f"\nWorkflow Status: {self.tracker.get_status(workflow_name)}")

                print("\nWorkflow Summary")
                print("-----------------")
                print(f"Workflow Name: {workflow_name}")
                print(f"Final Status: {self.tracker.get_status(workflow_name)}")
                print(f"Total tasks: {len(workflow)}")

                write_log(f"Workflow Summary", "INFO")
                write_log(f"Workflow Name: {workflow_name}", "INFO")
                write_log(f"Final Status: {self.tracker.get_status(workflow_name)}", "INFO")
                write_log(f"Total Tasks: {len(workflow)}", "INFO")

                log_seperator()

            except Exception as error:

                self.tracker.set_status(workflow_name, "failed")
                print(f"Workflow Status: {self.tracker.get_status(workflow_name)}")

                print(f"\nWorkflow Failed: {error}")

                write_log(f"{workflow_name} workflow failed: {error}", "ERROR")

                print("\nWorkflow Summary")
                print("----------------")
                print(f"Workflow Name: {workflow_name}")
                print(f"Final Status: {self.tracker.get_status(workflow_name)}")
                print(f"Total Tasks: {len(workflow)}")

                write_log(f"Workflow Summary", "INFO")
                write_log(f"Workflow Name: {workflow_name}", "INFO")
                write_log(f"Final Status: {self.tracker.get_status(workflow_name)}", "INFO")
                write_log(f"Total Tasks: {len(workflow)}", "INFO")
                
                log_seperator()
        else:

            print("workflow not found.")

            write_log(f"Workflow {workflow_name} not found", "ERROR")