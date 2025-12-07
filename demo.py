import os
from PIL import Image

# Import from installed ossimg library


# Manual
def run_manual_edit(img: Image.Image) -> Image.Image:
    print("\n" + "=" * 70)
    print(" " * 15 + "MANUAL EDIT MODE")
    print("=" * 70)
    print("\nYou'll be asked to configure 4 parameters.")
    print("Press Enter to use default values.\n")
    
    # Collect all inputs first
    print("-" * 70)
    print("[1/4] SATURATION")
    print("  • 1.0 = original")
    print("  • 0.0 = grayscale")
    print("  • >1.0 = more vibrant")
    print("-" * 70)
    saturation_factor = get_float_input("Enter Saturation Factor", 1.0)
    
    print("\n" + "-" * 70)
    print("[2/4] SHADOWS")
    print("  • 0.0 = neutral")
    print("  • Positive = lift shadows (brighter)")
    print("  • Negative = crush shadows (darker)")
    print("-" * 70)
    shadows_amount = get_float_input("Enter Shadows Amount", 0.0)
    
    print("\n" + "-" * 70)
    print("[3/4] BRIGHTNESS")
    print("  • 1.0 = original")
    print("  • >1.0 = brighter")
    print("  • <1.0 = darker")
    print("-" * 70)
    brightness_factor = get_float_input("Enter Brightness Factor", 1.0)
    
    print("\n" + "-" * 70)
    print("[4/4] SHARPNESS")
    print("  • 1.0 = original")
    print("  • >1.0 = sharper")
    print("  • <1.0 = blurrier")
    print("-" * 70)
    sharpness_factor = get_float_input("Enter Sharpness Factor", 1.0)
    
    # Ensure output directory exists
    os.makedirs("outputs", exist_ok=True)
    
    # Apply edits step-by-step
    print("\n" + "=" * 70)
    print("Applying Edits Step-by-Step...")
    print("=" * 70)
    
    edit_sequence = process_manual_edits(
        img,
        saturation_factor,
        shadows_amount,
        brightness_factor,
        sharpness_factor
    )
    
    final_img = None
    step_count = 1
    
    for feature_name, current_img in edit_sequence:
        preview_name = f"outputs/preview_{step_count:02d}_{feature_name}.png"
        current_img.save(preview_name)
        print(f"  📸 Step {step_count}: {feature_name.upper():12} → {preview_name}")
        final_img = current_img
        step_count += 1
    
    # Save final result
    if final_img:
        final_name = "outputs/output_FINAL_MANUAL_EDIT.png"
        final_img.save(final_name)
        print(f"\n🎉 Final combined result: {final_name}")
        return final_img
    
    return img

# Interface
