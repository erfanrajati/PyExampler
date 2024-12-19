# PyExampler  

[![GitHub stars](https://img.shields.io/github/stars/erfanrajati/PyExampler)](https://github.com/erfanrajati/PyExampler/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/erfanrajati/PyExampler)](https://github.com/erfanrajati/PyExampler/network)  
[![GitHub license](https://img.shields.io/github/license/erfanrajati/PyExampler)](https://github.com/erfanrajati/PyExampler/blob/main/LICENSE)  

**PyExampler** is a Python-based tool designed to simplify teaching by generating diverse programming examples, making learning engaging and effective. Perfect for educators, self-learners, and Python enthusiasts.

---

## Key Features  
- Generate examples for core programming concepts (variables, loops, functions, and more).  
- Simple command-line interface for fast and easy access.  
- Platform-independent and customizable for varied teaching needs.  

---

## Get Started  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/erfanrajati/PyExampler.git  


## Installation Process

Welcome to the **PyExampler** project! This documentation will guide you through two main installation methods (for v1.0):  
1. **Installing a prebuilt version from the releases**  
2. **Cloning the repository and building it yourself**

---

## Section 1: Installing Prebuilt Version (v1.0)

If you want to quickly set up and use **PyExampler**, you can download the prebuilt version from the [Releases](https://github.com/erfanrajati/PyExampler/releases) section of this repository. Follow these simple steps:

### Steps for Installation:

1. Download the **PyExampler v1.0** release zip file from the Releases section. It contains the following files:
   - `addpath.exe`
   - `PyExampler.exe`
   - `python_guide_examples.json`
   
2. Extract the contents of the zip file to a folder on your machine.

3. **Add PyExampler to System Path:**
   - Double-click on the `addpath.exe` file. This will automatically add **PyExampler** to your system's PATH environment variable, making it easy to run from any terminal.
   
4. **Cleanup:**
   - Once the path is successfully added, it is recommended to delete the `addpath.exe` file to keep your installation clean.
   
5. **Running the Program:**
   - After this, you can simply open the **Windows Terminal** or **Command Prompt** and type:
     ```
     PyExampler
     ```
   - The program will start, and you're ready to enjoy!

---

## Section 2: Building the Project from Source

If you want to clone the repository and build the application yourself, follow the steps below:

### Step 1: Clone the Repository

First, clone the repository using the following command:
```bash
git clone https://github.com/erfanrajati/PyExampler.git
```

### Step 2: Install Required Dependencies

The project requires **PyInstaller** to create a standalone executable. Install it using:
```bash
pip install pyinstaller
```

### Step 3: Building the Project

To build **PyExampler**, execute the following PyInstaller command:

```bash
pyinstaller --onefile --name PyExampler --add-data "C:\path\to\python\site-packages\pyfiglet\fonts;pyfiglet/fonts" --workpath ./PyExampler_build/build --distpath ./PyExampler_build/dist --specpath ./PyExampler_build main.py
```

- Replace `C:\path\to\python\site-packages\pyfiglet\fonts` with the actual path to the `pyfiglet/fonts` on your system.

### Step 4: Locating the Build Output

The final build (the `PyExampler.exe` file) will be located in the following directory:
```
\PyExampler\PyExampler_build\dist\
```

### Step 5: Running the Program

The program requires the `python_guide_examples.json` file to run. Ensure this file is in the same directory as the `PyExampler.exe` file.

For the best experience, you can add the **PyExampler** executable to your system path. The repository provides a helpful script located in the `/install` directory.

To add **PyExampler** to your system path:
1. Move the `addpath.py` script from the `/install` directory into the same folder where `PyExampler.exe` and `python_guide_examples.json` are located.
2. Run the script:
   ```bash
   python addpath.py
   ```

This will add **PyExampler** to the system path, allowing you to run it from any terminal.

### Step 6: Running PyExampler

Once the build is complete and the path is added, you can run **PyExampler** by opening a terminal and typing:
```bash
PyExampler
```
The program will start, and you're good to go!

---

Thank you for using **PyExampler**! If you run into any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/erfanrajati/PyExampler/issues).
