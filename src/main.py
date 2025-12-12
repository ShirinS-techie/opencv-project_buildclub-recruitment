
# Import the helper functions from utils.py
from utils import (
    load_and_convert_image,
    apply_smooth_blur,
    create_posterization_lut,
    apply_lut_mapping,
    display_results
)

def main():
    # --- Configuration ---
    # Replace with the actual path to your image file (e.g., 'obama.jpg' or 'image_0.png')
    IMAGE_PATH = 'assets/input/cat.jpg' 
    # Number of color levels for posterization (e.g., 5 as requested)
    N_LEVELS = 5
    # Resize dimensions for consistent display (width, height)
    RESIZE_DIM = (220, 300)
    # Blur kernel size (must be odd). 7 gives clearer color blocks than 5.
    BLUR_KERNEL = 7

    print(f"Starting posterization process on '{IMAGE_PATH}' with n={N_LEVELS}...")

    # 1. Load image, resize, and convert BGR -> RGB
    image_rgb = load_and_convert_image(IMAGE_PATH, RESIZE_DIM)
    if image_rgb is None:
        return # Exit if loading failed

    # 2. Apply slight median blur for smooth output and better clarity
    image_blurred = apply_smooth_blur(image_rgb, BLUR_KERNEL)
    print("- Image loaded and converted to RGB.")
    print(f"- Median blur applied (kernel size: {BLUR_KERNEL}).")

    # 3. Create the Look-Up Table (LUT) based on 'n' levels
    # This step involves the math that splits range 0-255
    lut = create_posterization_lut(N_LEVELS)
    print(f"- Look-Up Table created for {N_LEVELS} levels.")

    # 4. Map input pixels according to LUT using cv2.LUT()
    image_posterized = apply_lut_mapping(image_blurred, lut)
    print("- LUT mapping applied successfully.")

    # 5. Display the Original and Posterized images side-by-side using pyplot
    display_results(image_rgb, image_posterized)

if __name__ == "__main__":
    main()
