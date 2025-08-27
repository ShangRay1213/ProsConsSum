## **5️⃣ setup.py**


from setuptools import setup, find_packages

setup(
    name="ProsConsSum",
    version="0.1.0",
    author="Ray Chen",
    author_email="your_email@example.com",
    description="Automatically summarize product reviews into Pros/Cons format",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ProsConsSum",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch",
        "transformers",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
