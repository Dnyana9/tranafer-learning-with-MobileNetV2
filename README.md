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
```bash
git clone https://github.com/Dnyana9/asl-sign-language-classifier.git
pip install -r requirements.txt
