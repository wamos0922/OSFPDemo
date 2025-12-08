Demonstration Outputs

[![PyPI version](https://badge.fury.io/py/ossimg.svg)](https://pypi.org/project/ossimg/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

##  About

This interactive demo showcases all features of the ossimg library:

1. **3 Preset Templates** - One-click artistic filters
2. **Manual Editing Mode** - Custom adjustments with 4 parameters
3. **Step-by-Step Previews** - See how each adjustment affects your image
---
##  Quick Start

### Method 1: From PyPI (Recommended)
```bash
#1. Install the library
pip install ossimg==2.0.0

# 2. Clone the demo
git clone https://github.com/wamos0922/OSFPDemo.git
cd OSFPDemo

# 3. Run the demo
python demo.py
```
### Method 2: Quick Install (Recommended)
```bash
# 1. Install the library
pip install git+https://github.com/wamos0922/OSFPLibrary.git

# 2. Clone the demo
git clone https://github.com/wamos0922/OSFPDemo.git
cd OSFPDemo

# 3. Run the demo
python demo.py
```
### Method 3: Development Setup

For team members working on both repositories:
```bash
# 1. Clone both repos side-by-side
mkdir ossimg-project
cd ossimg-project

git clone https://github.com/wamos0922/OSFPLibrary.git
git clone https://github.com/wamos0922/OSFPDemo.git

# 2. Install library in editable mode
cd OSFPLibrary
pip install -e .
cd ..

# 3. Run demo
cd OSFPDemo
python demo.py
```
---
## Usage

### Interactive Menu

When you run the demo:
```
======================================================================
                    ossimg Library Demo
======================================================================

Choose an option:

  1: Apply 'Golden Hour' Template
  2: Apply 'Gritty Contrast' Template
  3: Apply 'Pastel Matte' Template
  4: Manual Edit Mode

======================================================================
Enter your choice (1-4):
```

### Template Mode (Options 1-3)

Simply choose a number:
```bash
Enter your choice: 1

🌅 Applying: Golden Hour Template...
✅ Success! Saved as: outputs/output_FINAL_GOLDEN_HOUR.png
```

### Manual Edit Mode (Option 4)

Configure 4 parameters:
```bash
Enter your choice: 4

[1/4] SATURATION
Enter Saturation Factor (Default: 1.00): 1.3

[2/4] SHADOWS
Enter Shadows Amount (Default: 0.00): 0.4

[3/4] BRIGHTNESS
Enter Brightness Factor (Default: 1.00): 1.1

[4/4] SHARPNESS
Enter Sharpness Factor (Default: 1.00): 1.2

📸 Step 1: SATURATION   → outputs/preview_01_saturation.png
📸 Step 2: SHADOWS      → outputs/preview_02_shadows.png
📸 Step 3: BRIGHTNESS   → outputs/preview_03_brightness.png
📸 Step 4: SHARPNESS    → outputs/preview_04_sharpness.png

🎉 Final result: outputs/output_FINAL_MANUAL_EDIT.png
```

---

## 📁 Output Files

### Folders
1. images/

- This is where you put your input photo

- If the folder is empty, the code creates a sample image called `sample_input.png` automatically

- you can replace it with your own photo (just make sure it's a .png file)

2. outputs/

- All edited photos go here

- If you run the demo again, new files will replace the old ones
---
### Generated Files

**Template Outputs:**
- `output_FINAL_GOLDEN_HOUR.png` - Warm sunset look
- `output_FINAL_GRITTY_CONTRAST.png` - High contrast style  
- `output_FINAL_PASTEL_MATTE.png` - Soft dreamy effect

**Manual Edit Outputs:**
- `preview_01_saturation.png` - After saturation adjustment
- `preview_02_shadows.png` - After shadow adjustment
- `preview_03_brightness.png` - After brightness adjustment
- `preview_04_sharpness.png` - After sharpness adjustment
- `output_FINAL_MANUAL_EDIT.png` - Final combined result

---
## Using Your Own Images

### Method 1: Replace Sample
```bash
cp your_photo.jpg images/sample_input.png
python demo.py
```

### Method 2: Modify Script

Edit `demo.py` line 126:
```python
INPUT_FILE = "images/your_photo.jpg"  # Change filename
```

---