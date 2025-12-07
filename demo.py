import os
from PIL import Image

# Import from installed ossimg library
try:
    from ossimg import (
        load_image,
        apply_golden_hour,
        apply_gritty_contrast,
        apply_pastel_matte,
        process_manual_edits
    )
except ImportError as e:
    print("=" * 70)
    print("  ERROR: ossimg library is not installed!")
    print("=" * 70)
    print("\nPlease install the library first:")
    print("\n  Method 1 - From GitHub (Recommended):")
    print("  pip install git+https://github.com/wamos0922/OSFPLibrary.git")
    print("\n  Method 2 - For Development:")
    print("  git clone https://github.com/wamos0922/OSFPLibrary.git")
    print("  cd OSFPLibrary")
    print("  pip install -e .")
    print("\n" + "=" * 70)
    exit(1)


def get_float_input(prompt: str, default_value: float) -> float:
    while True:
        try:
            user_input = input(f"{prompt} (Default: {default_value:.2f}): ").strip()
            if not user_input:
                return default_value
            return float(user_input)
        except ValueError:
            print(" Invalid input. Please enter a number.")

# Create a dummy image
def create_dummy_image(filename="images/sample_input.png"):
    os.makedirs("images", exist_ok=True)
    
    if not os.path.exists(filename):
        print(f"📷 Creating dummy image: {filename}")
        img = Image.new('RGB', (400, 300), color='#6A5ACD')
        img.save(filename)
        print(f"✅ Created: {filename}")

# Manual


# Interface
