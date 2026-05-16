from engine import WorkflowEngine

def show_menu():
    print("\nWORKFLOW ORCHESTRATION ENGINE")
    print("1. Backup Workflow")
    print("2. Data Processing Workflow")
    print("3. Deployment Workflow")
    print("4. Exit")

engine = WorkflowEngine()

while True:
    show_menu()

    choice = input("Select a workflow: ")

    if choice == "1":
        engine.run_workflow("backup")

    elif choice == "2":
        engine.run_workflow("data_processing")

    elif choice == "3":
        engine.run_workflow("deployment")

    elif choice == "4":
        print("Exiting Workflow Orchestration Engine. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid workflow.")