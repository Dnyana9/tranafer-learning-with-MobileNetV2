#!/bin/bash

echo "Starting ASL project setup..."


# === Step 1: Check for Conda ===
if ! command -v conda &> /dev/null; then
    echo "❌ Conda not found! Please install Anaconda or Miniconda first:"
    echo "🔗 https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# === Step 2: Create Conda environment if it doesn't exist ===
ENV_NAME="asl-classifier"

if conda info --envs | grep -q "^$ENV_NAME"; then
    echo "✅ Conda environment '$ENV_NAME' already exists."
else
    echo "📦 Creating Conda environment '$ENV_NAME'..."
    conda env create -f environment.yml
fi

# === Step 3: Activate environment ===
# NOTE: source the conda environment via conda.sh so it works inside scripts
echo "⚙️ Activating Conda environment..."
CONDA_BASE=$(conda info --base)
source "$CONDA_BASE/etc/profile.d/conda.sh"
conda activate $ENV_NAME


# === Step 4: Check for Kaggle CLI ===
if ! command -v kaggle &> /dev/null; then
    echo "Kaggle CLI not found!"
    echo "Please install it from: https://github.com/Kaggle/kaggle-api"
    exit 1
fi

# === Step 5: Check for Kaggle API key ===
if [ ! -f ~/.kaggle/kaggle.json ]; then
    echo "Kaggle API key not found!"
    echo "Please download your kaggle.json from your Kaggle account and place it in ~/.kaggle/"
    echo "More info: https://www.kaggle.com/docs/api"
    exit 1
fi

chmod 600 ~/.kaggle/kaggle.json

# === Step 6: Define directories ===
RAW_DIR="data/raw"
PREPROCESSED_DIR="data/preprocessed"
ZIP_NAME="hand-signs-asl-hand-sign-data"

KAGGLE_DATASET="jeyasrisenthil/hand-signs-asl-hand-sign-data"

# === Step 7: Create folders ===
mkdir -p $RAW_DIR
mkdir -p $PREPROCESSED_DIR

# === Step 8: Download Dataset ===
echo "Downloading dataset from Kaggle..."
kaggle datasets download -d $KAGGLE_DATASET -p $RAW_DIR

# === Step 9: Unzip ===
echo "Unzipping..."
unzip -q "$RAW_DIR/$ZIP_NAME" -d $RAW_DIR

# === Step 10: Run Preprocessing ===
echo "Running preprocessing script..."
python scripts/preprocess_data.py "$RAW_DIR/DATASET/" "$PREPROCESSED_DIR"

echo "Setup complete! Your data is ready to use."
