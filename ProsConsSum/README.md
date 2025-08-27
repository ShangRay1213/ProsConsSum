# ProsConsSum

**ProsConsSum** is a Python tool for automatically summarizing product reviews into a clear **Pros / Cons** format.  
This helps businesses and researchers quickly extract insights from customer feedback.

---

## 🚀 Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/ShangRay1213/ProsConsSum.git
cd ProsConsSum
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn torch transformers tqdm
```

## 📥 Download Models

Due to GitHub file size limits, trained models are hosted on Google Drive:

🔗 [Download models here](https://drive.google.com/drive/folders/1m_RmfyLH_TFJnMvna5dyw2GBbOfXwvFS?usp=sharing)

After downloading, place the models inside the `ProsConsSum/models/` directory:

```
ProsConsSum/
│── models/
│   ├── t5_stage1_trained/
│   ├── t5_stage2_trained_local/
│── ProsConsSum/
│── main.py
│── ...
```

---

## 📖 Usage Example

```python
from ProsConsSum import summarize_review

def test_sample():
    text = "I really enjoyed the new café downtown—the coffee was rich and flavorful, and the atmosphere was cozy. However, the service was a bit slow, and the pastries were overpriced for their size."
    result = summarize_review(text)
    print(result)

if __name__ == "__main__":
    test_sample()
```

### ✅ Expected Output

```
Pros: new downtown café, rich and flavorful coffee, cozy atmosphere
Cons: slow service, overpriced pastries
```

---

## 📂 File Structure

```
ProsConsSum/
│── models/                  # Pretrained models (download from Google Drive)
│── ProsConsSum/             # Core library
│── main.py                  # Example entry point
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
```
