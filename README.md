# AI Text Generator

You start with a simple idea — just a sentence or two — adjust a few settings, and the app builds on it, turning your prompt into a full piece of text. Everything runs locally on your machine using a lightweight language model powered by Python.

I built the interface using Streamlit and integrated it with Hugging Face's Transformers library. The goal was to keep it all simple.

## 📋 Table of Contents
- [Key Features](#-key-features)
- [Getting Started](#-getting-started)
- [Running the App](#-running-the-app)
- [How to Use](#-how-to-use)
- [Technical Notes](#-technical-notes)


## 🚀 Key Features

* **Creative Text Output** – Enter a starting prompt and receive a context-aware continuation.
* **Flexible Controls** – Fine-tune the length and creativity of the output using sliders.
* **No-Hassle Setup** – A minimal web interface that runs entirely in your browser with no cloud dependencies.

---

## 🛠 Getting Started

### 1. Clone the project or create a new folder

```bash
git clone https://github.com/juamecos/ai-text-generator.git
cd ai-text-generator
```

Project folders that are in the repository: `app.py`, `requirements.txt`, and `README.md`.

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:
```bash
.\venv\Scripts\activate
```

On macOS / Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the App

1. Make sure your virtual environment is active.
2. Launch the app with Streamlit:

```bash
streamlit run app.py
```

Your default browser will open at http://localhost:8501 where you can interact with the app.

## 🧭 How to Use

1. Enter a prompt (any starting phrase or idea).
2. Use the sidebar to set:
   - The maximum length of the generated text.
   - The temperature, which controls how creative/random the output is.
3. Click "Generate Text" and wait a few seconds for the result.

## 🧠 Technical Notes

- The first time you run the app, it will download the distilgpt2 model from Hugging Face. This may take a minute depending on your internet connection.
- distilgpt2 is a lightweight model — great for quick testing. You can upgrade to a more powerful model (like gpt2, gpt-neo, etc.) if you have the resources.