#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/data.csv"

# Check if a task name was provided as an argument
if [ -z "$1" ]; then
  read -p "Enter task name: " task
else
  task="$1"
fi

# Save start time
start_time=$(date +%s)

# Check for termdown
if command -v termdown &> /dev/null; then
  termdown 
else
  echo "⚠️ 'termdown' not found. Using fallback mode."
  echo "Press 'q' then Enter to stop the timer."
  
  while true; do
    read -n1 -s key
    if [[ "$key" == "q" ]]; then
      break
    fi
  done
fi

# Get end time
end_time=$(date +%s)
elapsed=$((end_time - start_time))

# Format elapsed as hh:mm:ss
formatted=$(printf "%02d:%02d:%02d" $((elapsed/3600)) $(((elapsed/60)%60)) $((elapsed%60)))

# Get timestamp and log to CSV
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
echo "$timestamp,$task,$formatted" >> "$LOG_FILE"

echo -e "\n✅ Logged: [$task] $formatted"

