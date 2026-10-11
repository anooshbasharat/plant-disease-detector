import numpy as np
import streamlit as st
from PIL import Image
import joblib

st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿")


@st.cache_resource  # load the model once, not on every click
def load_model():
    saved = joblib.load("model.joblib")
    return saved["model"], saved["class_names"], saved["img_size"]


model, class_names, img_size = load_model()


def image_to_row(img):
    # Exactly the same steps as in the notebook: shrink, read the pixels, flatten, scale to 0-1
    img = img.convert("RGB").resize((img_size, img_size))
    return np.asarray(img).flatten().astype(np.float32) / 255.0


def pretty(name):
    # "Tomato_Early_blight" -> "Tomato: Early blight"
    plant, _, condition = name.partition("_")
    return f"{plant}: {condition.replace('_', ' ')}"


st.title("🌿 Plant Disease Detector")
st.write("Take a photo of a leaf, or upload one, and the model will guess the plant and disease.")

tab_camera, tab_upload = st.tabs(["📷 Camera", "📁 Upload"])
with tab_camera:
    photo = st.camera_input("Take a photo")
with tab_upload:
    upload = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

file = photo or upload
if file is not None:
    img = Image.open(file)
    st.image(img, caption="Your leaf", use_container_width=True)

    probs = model.predict_proba([image_to_row(img)])[0]
    top3 = probs.argsort()[::-1][:3]  # indexes of the 3 highest scores

    best = class_names[top3[0]]
    if "healthy" in best:
        st.success(f"**{pretty(best)}** ({probs[top3[0]]:.0%} confident)")
    else:
        st.warning(f"**{pretty(best)}** ({probs[top3[0]]:.0%} confident)")

    st.write("Other possibilities:")
    for i in top3[1:]:
        st.write(f"- {pretty(class_names[i])} ({probs[i]:.0%})")
else:
    st.info("Waiting for a photo.")
