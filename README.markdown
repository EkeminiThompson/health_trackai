# Health TrackAI: A Machine Learning Health Tracker

Welcome to **Health TrackAI**, a web application that predicts heart disease risk, lifestyle health, and mental health status, and provides personalized health recommendations. This guide is for beginners and will walk you through setting up and running the project on your computer, step by step. No prior coding experience is needed!

## What You’ll Need
- A computer (Windows, macOS, or Linux).
- An internet connection.
- About 30–60 minutes to set everything up.

## Step-by-Step Instructions

### 1. Install Python
Python is the programming language used by this project. You need to install it first.

1. **Download Python**:
   - Go to [python.org/downloads](https://www.python.org/downloads/).
   - Download the latest version (e.g., Python 3.11 or higher). Choose the version for your operating system (Windows, macOS, or Linux).
   - **Important**: During installation, check the box that says **"Add Python to PATH"** (on Windows) to make Python easier to use.

2. **Install Python**:
   - Run the downloaded installer.
   - Follow the prompts. On Windows, select “Install Now” and ensure “Add Python to PATH” is checked.
   - On macOS or Linux, follow the installer instructions.

3. **Verify Python Installation**:
   - Open a terminal:
     - **Windows**: Press `Win + R`, type `cmd`, and press Enter.
     - **macOS**: Search for “Terminal” in Spotlight (press `Cmd + Space`).
     - **Linux**: Open your terminal app.
   - Type `python --version` and press Enter.
   - You should see something like `Python 3.11.5`. If you see an error, ensure Python was installed correctly and added to PATH.

### 2. Install Git
Git is a tool to download the project files from GitHub.

1. **Download Git**:
   - Go to [git-scm.com/download](https://git-scm.com/download).
   - Download the version for your operating system.

2. **Install Git**:
   - Run the installer and follow the prompts. Use the default settings unless you know what to change.
   - On Windows, choose “Use Git from the Windows Command Prompt” during setup.

3. **Verify Git Installation**:
   - In your terminal, type `git --version` and press Enter.
   - You should see something like `git version 2.41.0`. If not, reinstall Git.

### 3. Clone the Project from GitHub
The project files are stored on GitHub. You’ll download them to your computer.

1. **Create a Project Folder**:
   - On your computer, create a folder where you want to store the project (e.g., `HealthTrackAI` on your Desktop).
   - Remember the folder’s location (e.g., `C:\Users\YourName\Desktop\HealthTrackAI` on Windows).

2. **Open Terminal in the Folder**:
   - **Windows**: Right-click inside the folder, select “Open in Command Prompt” or “Git Bash Here” (if installed).
   - **macOS/Linux**: Open Terminal, then type `cd ~/Desktop/HealthTrackAI` (adjust the path to your folder) and press Enter.

3. **Clone the Repository**:
   - In the terminal, type:
     ```
     git clone https://github.com/EkeminiThompson/health_trackai.git
     ```
   - Press Enter. This downloads the project files into a `health_trackai` subfolder.
   - Type `cd health_trackai` and press Enter to move into the project folder.

4. **Check Files**:
   - Type `dir` (Windows) or `ls` (macOS/Linux) to list files.
   - You should see files like `health_tracker_app.py`, `health_tracker_ml.py`, `requirements.txt`, a `templates` folder with `index.html`, and `.pkl` files (e.g., `heart_disease_model.pkl`, `features.pkl`).

### 4. Set Up a Virtual Environment
A virtual environment keeps the project’s dependencies separate from other Python projects.

1. **Create a Virtual Environment**:
   - In the terminal (inside the `health_trackai` folder), type:
     ```
     python -m venv venv
     ```
   - Press Enter. This creates a `venv` folder.

2. **Activate the Virtual Environment**:
   - **Windows**:
     ```
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```
     source venv/bin/activate
     ```
   - Press Enter. You should see `(venv)` in your terminal prompt, indicating the environment is active.

### 5. Install Project Dependencies
The project needs specific Python libraries listed in `requirements.txt`.

1. **Install Dependencies**:
   - With the virtual environment active, type:
     ```
     pip install -r requirements.txt
     ```
   - Press Enter. This installs libraries like Flask, scikit-learn, numpy, and others.
   - Wait for the installation to complete (may take a few minutes).

2. **Verify Installation**:
   - Type `pip list` to see installed packages.
   - Look for `flask`, `joblib`, `numpy`, `scikit-learn`, and others from `requirements.txt`.

### 6. Run the Health Tracker App
Now you’ll start the web app and access it in a browser.

1. **Run the Flask App**:
   - In the terminal (with `(venv)` active and inside `health_trackai`), type:
     ```
     python health_tracker_app.py
     ```
   - Press Enter. You should see output like:
     ```
     * Running on http://127.0.0.1:5000
     ```
   - This means the app is running locally.

2. **Access the App in a Browser**:
   - Open a web browser (e.g., Chrome, Firefox, Edge).
   - Copy this URL: `http://127.0.0.1:5000`
   - Paste it into the browser’s address bar and press Enter.
   - You should see the Health Tracker web page with a form to enter health data.

3. **Use the App**:
   - Fill in the form fields (e.g., age, cholesterol, exercise level). Each field has help text (e.g., “0 for female, 1 for male” for sex).
   - Click “Get Predictions” to see your heart disease risk, lifestyle status, mental health prediction, and personalized recommendations.
   - If you see a warning about low confidence (e.g., “Heart disease prediction has low confidence”), double-check your inputs or consult a doctor.

4. **Stop the App**:
   - To stop the app, go back to the terminal and press `Ctrl + C`.
   - To deactivate the virtual environment, type `deactivate` and press Enter.

### Troubleshooting Common Issues
- **“python: command not found”**:
  - Python isn’t installed or not added to PATH. Reinstall Python and ensure “Add Python to PATH” is checked.
  - On Windows, try `py --version` instead of `python --version`.
- **“git: command not found”**:
  - Git isn’t installed. Install it from [git-scm.com](https://git-scm.com).
- **“pip install -r requirements.txt” fails**:
  - Ensure the virtual environment is active (`(venv)` in the prompt).
  - Check your internet connection.
  - Try `pip install --upgrade pip` first, then rerun the command.
- **“No module named flask”**:
  - Dependencies weren’t installed correctly. Activate the virtual environment and rerun `pip install -r requirements.txt`.
- **App doesn’t load in browser**:
  - Ensure the terminal shows `Running on http://127.0.0.1:5000`.
  - Check that you typed the URL exactly: `http://127.0.0.1:5000`.
  - Try a different browser or clear your browser cache.
- **Error about missing `.pkl` files**:
  - Verify that `heart_disease_model.pkl`, `lifestyle_model.pkl`, `mental_health_model.pkl`, `heart_disease_scaler.pkl`, `lifestyle_scaler.pkl`, `mental_health_scaler.pkl`, and `features.pkl` are in the `health_trackai` folder.
  - If missing, ensure you cloned the correct repository.

### Optional: Run the Machine Learning Training Script
If you want to retrain the models (not required to use the app), you can run `health_tracker_ml.py`:
1. Activate the virtual environment (see Step 4).
2. Type:
   ```
   python health_tracker_ml.py
   ```
3. This downloads the UCI Heart Disease dataset, trains the models, and saves new `.pkl` files.

### Project Structure
Here’s what the files in `health_trackai` do:
- `health_tracker_app.py`: Runs the web app.
- `health_tracker_ml.py`: Trains the machine learning models.
- `requirements.txt`: Lists required Python libraries.
- `templates/index.html`: The web page layout.
- `.pkl` files: Pre-trained models and scalers for predictions.
- `features.pkl`: List of input features.

### Questions or Issues?
If you run into problems or have questions:
- Check the [GitHub repository](https://github.com/EkeminiThompson/health_trackai) for updates.
- Contact the project maintainer (details in the repository).
- Search online for error messages (e.g., on Stack Overflow).

Enjoy using Health TrackAI to explore your health predictions and get personalized recommendations!