# ⏱️ Stopwatch Logger

A simple terminal stopwatch script that logs elapsed time and task descriptions to a CSV file.

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/julianjica/stopwatch
   cd stopwatch-logger
   ```

2. Make the script executable:

   ```bash
   chmod +x stopwatch_logger.sh
   ```

---

## 🚀 Usage

You can start the stopwatch in two ways:

### ▶️ With a task name as an argument:
```bash
./stopwatch_logger.sh "Practice tennis"
```

### ✍️ Or interactively:
```bash
./stopwatch_logger.sh
```
You'll be prompted to enter a task name.
Feel free to set an alias for this command!

---

## 📝 Output

Each session is logged in a `data.csv` file in the format:

```csv
Date and Time,Task Name,Elapsed Time
2025-04-24 14:33:00,Practice tennis,00:45:12
```

---
