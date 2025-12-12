# Image Cartoonizer (Posterization) Project

## 📝 Description of Approach
This project applies a stylized "posterization" or cartoon effect to input images using Computer Vision techniques. The core logic reduces the number of unique colors in the image while maintaining structural edges.

The processing pipeline consists of four main stages:
1.  **Color Space Conversion:** The input image is converted from BGR (OpenCV default) to RGB to ensure correct color representation during visualization.
2.  **Noise Reduction (Smoothing):** A **Median Blur** filter (kernel size 7) is applied. This step smoothes out fine textures (like noise or roughness) while preserving strong edges, which is crucial for creating clean, "painted" color blocks.
3.  **Color Quantization (Look-Up Table):** A custom **Look-Up Table (LUT)** is generated to map the continuous 0-255 pixel range into `n` discrete levels (e.g., 5 levels). 
    * The algorithm uses integer division to categorize pixels into bins and assigns them the center value of that bin. This effectively reduces the color palette of the image.
4.  **Optimization:** Instead of iterating through every pixel, `cv2.LUT()` is used to vectorise the operation, applying the color mapping instantly across the entire image.

## ⚙️ Steps to Run the Model

### 1. Install Dependencies
Ensure you have Python installed, then run the following command to install the required libraries:
Bash
pip install -requirements.txt

### 2. Project Setup
Ensure your project folder contains the following files:
main.py: The main execution script.
utils.py: The file containing helper functions (blur, LUT, display).
image.jpg: Your input image file.

### 3. Execution
Run the project by executing the main script in your terminal:
Bash
python main.py
(Note: You can change the input image filename inside main.py by modifying the IMAGE_PATH variable).

### 📸 Screenshots / Output Images
Below is a comparison between the original input image and the posterized output (with n=5 levels).
<img width="1236" height="706" alt="output real" src="https://github.com/user-attachments/assets/33b0760a-ffd0-4c20-9da1-75c3a91f86b5" />


