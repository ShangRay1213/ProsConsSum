# ProsConsSum

ProsConsSum is a Python library for automatically summarizing product reviews into **Pros / Cons** format.

## Installation

```bash
pip install fastapi uvicorn torch transformers tqdm
```
```
https://drive.google.com/drive/folders/1m_RmfyLH_TFJnMvna5dyw2GBbOfXwvFS?usp=sharing
```
## How to use
```python
from ProsConsSum import summarize_review

def test_sample():
    text = "I really enjoyed the new café downtown—the coffee was rich and flavorful, and the atmosphere was cozy. However, the service was a bit slow, and the pastries were overpriced for their size."
    result = summarize_review(text)
    print(result)

if __name__ == "__main__":
    test_sample()
```
