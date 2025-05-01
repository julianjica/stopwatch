# ⏱️ Stopwatch Logger

A simple terminal stopwatch script that logs elapsed time and task descriptions to a CSV file — using `termdown` if available, or falling back to a built-in mode if not. Additionally, a **terminal dashboard** is provided to visualize the time spent on tasks and categories.

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/julianjica/stopwatch
   cd stopwatch
   ```

2. Make the script executable:

   ```bash
   chmod +x stopwatch.sh
   ```

3. *(Optional)* Install `termdown` for enhanced stopwatch display:

   ```bash
   pip install termdown
   ```

4. Install the necessary Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

You can start the stopwatch in two ways:

### ▶️ With a task name as an argument:
```bash
./stopwatch.sh "Practice tennis"
```

### ✍️ Or interactively:
```bash
./stopwatch.sh
```
You'll be prompted to enter a task name.

---

## 🔁 How It Works

- If `termdown` is installed, it runs in stopwatch mode. You can stop it by pressing `q`.
- If `termdown` is **not** installed, it falls back to a minimal mode — just press `q` then `Enter` to stop the timer.
- The elapsed time and task are logged to a CSV file automatically.

---

## 📝 Output

Each session is logged in a `data.csv` file (in the same directory as the script) in the format:

```csv
Date and Time,Task Name,Elapsed Time
2025-04-24 14:33:00,Practice tennis,00:45:12
```

---

## 🧠 Categorizing Tasks with Gemini API

To categorize tasks automatically using Google Gemini, run:

```bash
python categorize_tasks.py
```

This script will:
- Use the Gemini API to analyze all task names in `data.csv`
- Assign them to relevant categories
- Save a new file called `categorized_data.csv` with an additional `Category` column

Make sure to set your Gemini API key in the script before running it.

---

## 📊 Terminal Dashboard

A **terminal dashboard** is available to explore how your time is distributed across tasks and categories. It provides an interactive experience directly in the terminal using the `rich` library.

### ▶️ To launch the terminal dashboard:

```bash
python terminal_dashboard.py
```

- View total time per category
- Select a category to see detailed tasks and durations

---

## 💡 Tip

You can set an alias in your shell config to call the script more easily:

```bash
alias stopwatch="~/path/to/stopwatch.sh"
```

Now just run:
```bash
stopwatch "Reading"
```

