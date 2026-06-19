# 🐍 C_from_Python ⚙️

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-Language-A8B9CC?style=flat&logo=c&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=flat&logo=gnu-bash&logoColor=white)

A minimal, clean, and straightforward example of how to execute C code directly from Python. 

This repository demonstrates how to bridge the gap between Python's developer-friendly syntax and C's raw execution speed by compiling C code into a shared library and calling it natively.

---

## 📂 Repository Structure

* **`my_functions.c`** — The C source code containing the core logic and functions.
* **`build.sh`** — A shell script that compiles the C code into a dynamic shared object (`.so`).
* **`test.py`** — The Python script that loads the shared library and invokes the C functions.
* **`my_functions.so`** — The compiled shared library (generated after running the build script).

## 🚀 Getting Started

### Prerequisites
To build and run this project, you will need:
* Python 3.x
* A standard C compiler (like `gcc` or `clang`)
* A Unix-like environment (Linux/macOS) to execute the bash script.

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rmruiz/C_from_Python.git](https://github.com/rmruiz/C_from_Python.git)
   cd C_from_Python

2. **Compile the C code:**
Run the build script to generate the my_functions.so shared library.

   ```bash
   chmod +x build.sh
   ./build.sh

3. **Run the Python script:**
Execute the Python file to see the seamless interaction between Python and C in action.

   ```bash
   python test.py

## 🧠 How It Works (Under the Hood)
* Write C Code: Standard C functions are defined inside my_functions.c.

* Compile to Shared Object: The build.sh script uses a C compiler to create a shared library (my_functions.so). This typically involves using the -shared and -fPIC (Position Independent Code) flags.

* Bridge with Python: Inside test.py, Python's built-in FFI (Foreign Function Interface)—typically the ctypes library—is used to load the .so file. It maps the expected argument and return C-types, allowing Python to call the C functions directly without any extra wrappers.

## 🤝 Contributing
Feel free to fork this repository, add more complex C functions (such as array manipulation, struct passing, or pointers), and submit a Pull Request!
