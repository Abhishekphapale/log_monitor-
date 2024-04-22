#!/bin/bash

# Define log file path
LOG_FILE="app.log"

# Function to generate log messages
generate_log() {
    while true; do
        # Randomly select log level
        LOG_LEVEL=$(( ( RANDOM % 3 ) + 1 ))

        case $LOG_LEVEL in
            1) echo "$(date) - INFO message" >> $LOG_FILE ;;
            2) echo "$(date) - DEBUG message" >> $LOG_FILE ;;
            3) echo "$(date) - ERROR message" >> $LOG_FILE ;;
        esac

        sleep 1
    done
}

# Function to monitor log file
monitor_log() {
    echo "Monitoring log file..."
    echo "Press Ctrl+C to stop."

    trap 'echo -e "\nMonitoring stopped."; exit' SIGINT

    tail -f $LOG_FILE
}

# Function to perform basic log analysis
analyze_log() {
    echo "Performing basic log analysis..."
    # Count occurrences of specific keywords
    for keyword in "error" "exception" "warning"; do
        occurrences=$(grep -i $keyword $LOG_FILE | wc -l)
        echo "Occurrences of $keyword: $occurrences"
    done
}

# Main function
main() {
    # Start log generation in the background
    generate_log &

    # Command line argument to specify monitoring or analysis
    if [ "$1" == "monitor" ]; then
        monitor_log
    elif [ "$1" == "analyze" ]; then
        analyze_log
    else
        echo "Usage: $0 [monitor|analyze]"
        exit 1
    fi
}

main "$@"
