How to Run
Follow these instructions to run the calculator locally on your machine.

Prerequisites
Python 3.x: Ensure you have Python 3 installed. You can check your version by running:

Bash
python --version
Tkinter: Tkinter comes pre-bundled with standard Python installations on Windows and macOS.

Linux Users: If Tkinter is not already available on your machine, install it via your default package manager:

Bash
sudo apt-get install python3-tk
Step 1: Clone the Repository
Clone the codebase directly to your local file system using the Git CLI tool:

Bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
Step 2: Run the Script
Execute the Python script using your terminal or system command prompt:

Bash
python calculator.py
Roadmap & Enhancements
[ ] Implement a complete Division (/) block accompanied by dedicated error-handling modules to intercept ZeroDivisionError (division by zero exceptions).

[ ] Integrate active global keyboard listener hooks so users can input values via their physical numeric keypad (e.g., typing keys instead of just clicking buttons).

[ ] Refactor the static component layouts using the .grid() manager to support dynamic app window resizing.