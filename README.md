# ASL Sign Language Classifier 🤟

This project demonstrates how to use **transfer learning** with **MobileNetV2** to classify American Sign Language (ASL) hand signs. The model was trained on 36 classes (A–Z + 0–9) using the [ASL Alphabet Dataset](https://www.kaggle.com/datasets/grassknoted/asl-alphabet).

## 🔍 What’s Inside
- ✅ TensorFlow model built using MobileNetV2 as the base
- ✅ Image preprocessing and simple data augmentation
- ✅ Training with early stopping and validation split
- ✅ Fine-tuning using misclassified examples with higher weights
- ✅ Final model reaches over **96% validation accuracy**

## 🗂️ Files
- `transfer_learning.ipynb`: Main training notebook
- `requirements.txt`: Python dependencies
- `README.md`: Project overview

## 🧠 Key Concepts
- Transfer learning
- Data augmentation
- Fine-tuning with weighted datasets
- TensorFlow 2.x

## 🚀 Getting Started

---

## ⚙️ Project Setup

This project includes a `setup_project.sh` script that:

- Downloads the ASL Alphabet dataset from Kaggle
- Unzips it
- Crops the pink bounding box around the hand
- Resizes images to 160x160
- Saves them under `data/preprocessed/` in a class-wise structure

---

### 🧰 Requirements

Before running the setup script, make sure you:

1. Have Python and pip installed
2. Have the [Kaggle CLI](https://github.com/Kaggle/kaggle-api) installed:
    ```bash
    pip install kaggle
    ```
3. Have your Kaggle API key:
    - Download `kaggle.json` from [kaggle.com/account](https://www.kaggle.com/account)
    - Move it to the right location:

    ```bash
    mkdir -p ~/.kaggle
    mv ~/Downloads/kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

### 🚀 Run the Setup Script

Give the script execute permission (only once):

```bash
chmod +x setup_project.sh
