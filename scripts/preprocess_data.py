"""Script for preprocessing images for Kaggle ASL hand signs datasets"""
import os
import cv2
import numpy as np
from pathlib import Path
import argparse

def preprocess_dataset(data_dir, output_dir, target_size=(160, 160)):
    # Define HSV range for pink box
    lower_pink = np.array([140, 50, 50])
    upper_pink = np.array([170, 255, 255])

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    class_names = sorted(os.listdir(data_dir))
    for class_name in class_names:
        class_path = os.path.join(data_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        output_class_path = os.path.join(output_dir, class_name)
        Path(output_class_path).mkdir(parents=True, exist_ok=True)

        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"[SKIP] Could not read image: {img_path}")
                continue

            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_pink, upper_pink)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
                pad = 10
                x = max(0, x - pad)
                y = max(0, y - pad)
                w = min(img.shape[1] - x, w + 2 * pad)
                h = min(img.shape[0] - y, h + 2 * pad)

                cropped = img[y:y+h, x:x+w]
                resized = cv2.resize(cropped, target_size)

                save_path = os.path.join(output_class_path, img_name)
                cv2.imwrite(save_path, resized)
            else:
                print(f"[WARNING] No pink box found in {img_path}")

    print("Preprocessing complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess ASL dataset by cropping pink box and resizing.")
    parser.add_argument("data_dir", help="Path to raw dataset directory")
    parser.add_argument("output_dir", help="Path to save preprocessed dataset")
    args = parser.parse_args()

    preprocess_dataset(args.data_dir, args.output_dir)
