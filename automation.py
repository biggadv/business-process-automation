import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_task(task_name):
    logging.info(f"Starting task: {task_name}")
    print(f"Processing task: {task_name}")
    logging.info(f"Finished task: {task_name}")

def main():
    tasks = ["Import data", "Validate records", "Generate report"]
    for task in tasks:
        process_task(task)

if __name__ == "__main__":
    main()
