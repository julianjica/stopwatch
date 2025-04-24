#!/bin/bash

# Check if a task name was provided as an argument
if [ -z "$1" ]; then
  read -p "Enter task name: " task
else
  task="$1"
fi

# Start stopwatch and save start time
start_time=$(date +%s)

# Run termdown in stopwatch mode
termdown

# Get end time after Ctrl+C
end_time=$(date +%s)
elapsed=$((end_time - start_time))

# Format elapsed as hh:mm:ss
formatted=$(printf "%02d:%02d:%02d" $((elapsed/3600)) $(((elapsed/60)%60)) $((elapsed%60)))

# Log to CSV with task name and current timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
echo "$timestamp,$task,$formatted" >> data.csv

echo "Logged: [$task] $formatted"

