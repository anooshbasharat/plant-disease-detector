# AI-Enabled Plant Disease Detector

A Class 12 CBSE Artificial Intelligence project from Delhi Public School, Srinagar (academic session
2026–27). It identifies plant diseases from a photograph of a leaf using a neural network trained with
scikit-learn, and serves the result through a web app that works on a phone.

- **Live app:** https://plant-disease-detector.fly.dev
- **Video demonstration:** https://tinyurl.com/3ucz334z

## The problem

Plant diseases reduce crop yields, and identifying them usually needs agricultural knowledge and
experience. Symptoms such as spots, discolouration and unusual patterns on leaves are easy to
photograph but hard for a non-expert to interpret, and checking many plants by eye takes time.

The question this project answers: *how can Artificial Intelligence and image classification be used
to analyse an image of a plant leaf and predict the possible disease affecting the plant?*

The system is a demonstration of how AI can be applied to a practical agricultural problem. It
connects with UN Sustainable Development Goal 2, Zero Hunger, because healthier plants mean better
yields and fewer crop losses, and a simple tool can make early identification accessible to farmers,
gardeners and students without specialised knowledge.

## How it works

1. **Image input.** The user takes a photo with the device camera or uploads one from the gallery.
2. **Preprocessing.** The image is resized to 48 x 48 pixels and its red, green and blue values are
   read into a single row of 6,912 numbers, each scaled to between 0 and 1.
3. **Classification.** A Multi-Layer Perceptron, a neural network with one hidden layer of 256
   neurons, turns those numbers into a score for each of 38 categories.
4. **Result.** The app shows the most likely category with a confidence percentage, plus the next
   two possibilities. Healthy results appear in green and diseased results in amber.

## Results

| | |
|---|---|
| Dataset | PlantVillage: 54,305 leaf images, 38 categories, 14 plant species |
| Training / test split | 43,444 images for training, 10,861 kept aside for testing |
| Test accuracy | 76.5% on images the model had never seen |
| Training accuracy | 86.5% |
| Training time | about 4 minutes on a laptop |

The model does best on categories with distinctive patterns such as corn common rust and citrus
greening, and finds it hardest to separate diseases that all appear as small leaf spots, such as
tomato early blight and septoria leaf spot.

## Technologies

| Technology | Why it was chosen |
|---|---|
| Python | Widely used for AI and has many libraries |
| Scikit-learn | Provides the neural network (`MLPClassifier`) and testing tools |
| NumPy | Stores the images as tables of numbers |
| Pillow | Opens and resizes the image files |
| Matplotlib | Draws charts of the data and the results |
| joblib | Saves the trained model for the application |
| Jupyter Notebook | Runs the training code step by step and shows each output |
| Streamlit | Builds the web application using only Python |
| Docker and Fly.io | Package the application and host it online |

## Files

| File | Purpose |
|---|---|
| `main.ipynb` | Data overview, preprocessing, training, evaluation and saving the model |
| `app.py` | The Streamlit web app |
| `model.joblib` | The trained model with its class names and image size |
| `dataset/` | The PlantVillage images, one folder per category |
| `Dockerfile`, `fly.toml` | Deployment to Fly.io |
| `pyproject.toml`, `uv.lock` | Python dependencies, managed with uv |

## Running it yourself

Requires Python 3.11 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
uv run --group dev jupyter notebook main.ipynb   # explore the data and train the model
uv run streamlit run app.py                      # run the app locally
```

Training loads every image into memory and needs about 3.5 GB free.

## Deploying

```bash
fly deploy --ha=false
```

The `--ha=false` flag keeps the app on a single machine. Streamlit needs this: a platform that runs
several copies at once routes the photo upload to a different copy from the one holding the session,
and the upload fails.

## Dataset

[PlantVillage](https://github.com/spmohanty/plantvillage-dataset), colour images. Each image is
labelled with the plant species and either a disease or "healthy". The 14 plants are apple, blueberry,
cherry, corn, grape, orange, peach, bell pepper, potato, raspberry, soybean, squash, strawberry and
tomato. The categories are not equal in size: the largest has 5,507 images and the smallest 152.

## Future scope

- A Convolutional Neural Network, which learns shapes such as spots and edges instead of treating
  every pixel separately, would be the biggest step up in accuracy.
- Larger images, for example 128 x 128, combined with a CNN, to keep fine detail.
- Data augmentation: extra training images made by rotating, flipping or changing the brightness
  of existing ones.
- Photographs taken in real fields, since the dataset images have plain backgrounds.
- In the app: information about each disease and its treatment, more languages, and offline use.

## Team

| Role | Member |
|---|---|
| Group Leader | Maleehah |
| Prototype Builder | Anoosh Basharat |
| Data Expert | Syed Durryyun |
| Designer | Yofna Aftab |

Completed under the guidance of Ms. Aasima Mehraj.
