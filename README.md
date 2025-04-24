# ⏱️ Stopwatch Logger

A simple terminal stopwatch script that logs elapsed time and task descriptions to a CSV file — using `termdown` if available, or falling back to a built-in mode if not. Additionally, a **dashboard** is provided to visualize the time spent on tasks and categories.

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

## 📊 Interactive Dashboard

A **dashboard** is available to visualize the time spent on each task and category. The dashboard is built using Dash, and you can explore your tasks interactively.

### ▶️ To launch the dashboard:

1. Run the `dashboard.py` script:

   ```bash
   python dashboard.py
   ```

2. Open the link provided in the terminal (usually `http://127.0.0.1:8050/`) in your web browser to access the dashboard.

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
