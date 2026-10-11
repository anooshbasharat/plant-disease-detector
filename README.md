# Plant Disease Detector

A school project that identifies plant diseases from a photo of a leaf. A small neural network
(scikit-learn's `MLPClassifier`) is trained on the PlantVillage dataset and served as a Streamlit
web app that works on phones.

**Live app:** https://plant-disease-detector.fly.dev

## How it works

1. Every leaf image is shrunk to 48 x 48 pixels and flattened into 6,912 numbers (the red, green
   and blue value of each pixel), scaled to between 0 and 1.
2. 80% of the images train a neural network with one hidden layer of 256 neurons; 20% are kept
   aside for testing.
3. The trained model is saved to `model.joblib`, and the app applies the same steps to any new
   photo and shows the three most likely categories with a confidence percentage.

| | |
|---|---|
| Dataset | PlantVillage, 54,305 images, 38 categories, 14 plant species |
| Test accuracy | 76.5% on 10,861 images the model never saw |
| Training time | about 4 minutes on a laptop |

## Files

| File | Purpose |
|---|---|
| `main.ipynb` | Data overview, training, evaluation and saving the model |
| `app.py` | Streamlit app: take or upload a photo, see the prediction |
| `model.joblib` | The trained model and class names |
| `dataset/` | One folder per category |
| `Dockerfile`, `fly.toml` | Deployment to Fly.io |

## Running it yourself

Requires Python 3.11 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
uv run --group dev jupyter notebook main.ipynb   # train the model
uv run streamlit run app.py                      # run the app locally
```

Training needs about 3.5 GB of free memory.

## Deploying

```bash
fly deploy --ha=false
```

The `--ha=false` flag keeps the app on a single machine, which Streamlit needs for file uploads
to work.

## Dataset

PlantVillage, from https://github.com/spmohanty/plantvillage-dataset (the colour images). Each
image is labelled with the plant species and either a disease or "healthy".

## Libraries

scikit-learn, NumPy, Pillow, Matplotlib, joblib, Streamlit and Jupyter.
