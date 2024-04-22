import logging
import time
import random
import signal
import sys
import re

# Define log file path
LOG_FILE = "app.log"

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define keywords or patterns to search for
keywords_to_search = ["error", "exception", "warning"]

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    print("\nLogging interrupted. Exiting.")
    sys.exit(0)

# Main loop to generate log messages
def generate_log():
    while True:
        try:
            # Randomly select log level
            log_level = random.choice([logging.INFO, logging.DEBUG, logging.ERROR])
            # Get the log message format for the selected log level
            log_message = {
                logging.INFO: "INFO message",
                logging.DEBUG: "DEBUG message",
                logging.ERROR: "ERROR message"
            }[log_level]
            # Log the message
            logging.log(log_level, log_message)

            # Sleep for a short interval
            time.sleep(1)
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
            signal_handler(signal.SIGINT, None)

# Function to perform basic log analysis
def analyze_log():
    print("Performing basic log analysis...")
    try:
        with open(LOG_FILE, "r") as log_file:
            log_data = log_file.read()
            for keyword in keywords_to_search:
                occurrences = len(re.findall(keyword, log_data, re.IGNORECASE))
                print("Occurrences of", keyword + ":", occurrences)
    except FileNotFoundError:
        print("Error: Log file not found.")
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Command line argument to specify monitoring or analysis
    if len(sys.argv) != 2 or sys.argv[1] not in ["generate", "analyze"]:
        print("Usage: python log_monitor.py [generate|analyze]")
        sys.exit(1)

    if sys.argv[1] == "generate":
        generate_log()
    elif sys.argv[1] == "analyze":
        analyze_log()
