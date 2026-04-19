# 🎙️ Multilingual Text-to-Speech (TTS) App

A simple and interactive **Multilingual Text-to-Speech application** built using **Gradio** and **Piper TTS**.
This app converts input text into natural-sounding speech across multiple languages.

---

## 🚀 Features

* 🌐 Supports multiple languages:

  * English
  * Hindi
  * Telugu
* 🎧 Generates high-quality `.wav` audio output
* ⚡ Fast and lightweight using Piper (ONNX-based inference)
* 🖥️ Simple web UI powered by Gradio

---

## 📁 Project Structure

```
project/
│── app.py
│── requirements.txt
│── README.md
│── models/
│    ├── en_US-lessac-medium.onnx
│    ├── en_US-lessac-medium.onnx.json
│    ├── hi_IN-pratham-medium.onnx
│    ├── hi_IN-pratham-medium.onnx.json
│    ├── te_IN-venkatesh-medium.onnx
│    ├── te_IN-venkatesh-medium.onnx.json
│── outputs/
│── venv/   (optional, not included in repo)
```

---

## ⚙️ Environment Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Create a virtual environment

```
python -m venv venv
```

### Activate it:

**Windows**

```
venv\Scripts\activate
```

**Linux/Mac**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 📥 Download Model Weights

This project uses **Piper TTS models**, which must be downloaded manually.

Download the following models:

* **English**: `en_US-lessac-medium`
* **Hindi**: `hi_IN-pratham-medium`
* **Telugu**: `te_IN-venkatesh-medium`

You can download them from the official Piper model repository:
👉 https://github.com/rhasspy/piper/releases

---

### 📌 Important

After downloading, place the files inside the `models/` folder:

Each model should include:

* `.onnx` file
* `.onnx.json` file

Example:

```
models/
├── en_US-lessac-medium.onnx
├── en_US-lessac-medium.onnx.json
```

---

## ▶️ Running the Application

Start the app with:

```
python app.py
```

After running, you will see a local URL like:

```
http://127.0.0.1:7860
```

Open it in your browser.

---

## 🧪 Usage

1. Enter text in the input box
2. Select a language
3. Click **"Generate Speech"**
4. Listen to or download the generated audio

---

## ⚠️ Notes

* Model files are **not included** in the repository due to size
* Ensure model file names match those used in `app.py`
* Generated audio files are saved in the `outputs/` folder

---

## 🛠️ Future Improvements

* Add Kannada and more languages
* Voice selection per language
* Deploy on cloud (Hugging Face / Render)
* Streaming audio support

---

## 📌 Tech Stack

* Python
* Gradio
* Piper TTS (ONNX Runtime)

---

## 🤝 Contributing

Feel free to fork the repo and improve the project.

---

## 📄 License

This project is open-source and available under the MIT License.
