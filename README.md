# Explain_By_Manim
 


# Virtual Environment Setup 

## 1. Virtual Environment Setup

### Prerequisites
- Python 3.x installed on your system
- pip (Python package manager)
- Access to command line/terminal

### Creating a Virtual Environment

#### Windows
```bash
# Navigate to your project directory
cd your_project_directory

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### macOS/Linux
```bash
# Navigate to your project directory
cd your_project_directory

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### Installing Dependencies
Once your virtual environment is activated:
```bash
pip install -r requirements.txt
```

## 2. Running the LLN Script

### Basic Usage
```python
python lln.py
```


### Example Commands
```bash
# Run with default parameters
python lln.py
```

### Expected Output
- Graph showing convergence of sample means
- Statistical summary of results
- Execution time information

## 3. License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/0KeirLi0/Explain_By_Manim/blob/main/LICENSE) file for details.
