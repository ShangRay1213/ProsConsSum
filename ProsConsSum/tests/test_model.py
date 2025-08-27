from ProsConsSum import summarize_review

def test_sample():
    text = "I really enjoyed the new café downtown—the coffee was rich and flavorful, and the atmosphere was cozy. However, the service was a bit slow, and the pastries were overpriced for their size."
    result = summarize_review(text)
    print(result)

if __name__ == "__main__":
    test_sample()
