import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_and_convert_image(image_path, resize_dim=None):
    """
    Loads an image, optionally resizes it, and converts it from BGR to RGB.
    """
    # Read image in BGR format
    img_bgr = cv2.imread(image_path)
    
    if img_bgr is None:
        print(f"Error: Could not read image '{image_path}'. Check file path.")
        return None

    # Resize if dimensions provided (helps with consistent display)
    if resize_dim:
        img_bgr = cv2.resize(img_bgr, resize_dim)

    # Convert from BGR (OpenCV default) to RGB (Matplotlib requirement)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

def apply_smooth_blur(image_rgb, kernel_size=7):
    """
    Applies a median blur to smooth the image and reduce noise before posterization.
    A larger kernel size increases the "cartoon" effect clarity.
    """
    # Ensure kernel size is odd
    if kernel_size % 2 == 0:
        kernel_size += 1
    return cv2.medianBlur(image_rgb, kernel_size)

def create_posterization_lut(n_levels):
    """
    Creates a Look-Up Table (LUT) to map 256 color values down to 'n_levels'.
    Includes safety clipping to prevent overflow errors.
    """
    # Initialize LUT: 256 rows, 1 column, 8-bit unsigned integers
    lut = np.zeros((256, 1), dtype=np.uint8)
    
    # Calculate the size of each color "bin"
    step_size = 256 // n_levels

    for i in range(256):
        # 1. Determine which bin the pixel belongs to: (i // step_size)
        # 2. Calculate base value of bin: * step_size
        # 3. Offset to center of bin: + step_size // 2
        calculated_val = (i // step_size) * step_size + (step_size // 2)
        
        # CRITICAL FIX: Clip values to ensure they stay within 0-255 range.
        # Without this, calculated_val could exceed 255, causing an OverflowError when cast to uint8.
        lut[i] = np.clip(calculated_val, 0, 255)
        
    return lut

def apply_lut_mapping(image, lut):
    """
    Applies the Look-Up Table to the image using OpenCV's optimized function.
    """
    # cv2.LUT works instantly on all channels at once
    return cv2.LUT(image, lut)

def display_results(original_img, posterized_img):
    """
    Displays the original and processed images side-by-side using Matplotlib.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Display Original
    axes[0].imshow(original_img)
    axes[0].set_title("Original")
    # Setting ticks based on the example output provided in the prompt
    axes[0].set_xticks(np.arange(0, 221, 50))
    axes[0].set_yticks(np.arange(0, 301, 50))

    # Display Posterized
    axes[1].imshow(posterized_img)
    axes[1].set_title("Posterized")
    axes[1].set_xticks(np.arange(0, 221, 50))
    axes[1].set_yticks(np.arange(0, 301, 50))

    plt.tight_layout()
    print("Displaying results... check popup window.")
    plt.show()
