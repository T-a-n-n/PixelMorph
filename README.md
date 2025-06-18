# 🧬 PixelMorph: Chaos-Based Image Encryption with Genetic Intelligence

> **Final Year Mini Project** • BMS College of Engineering • VTU 2024-25  
> 👩‍💻 By Tanisha Jamie Das, Prajwal K Jain & Shambhu Sah  
> 🎓 Under the guidance of Dr. Nagarathna N, Professor & HOD, CSE (IoT & Cybersecurity)

---

## 🔒 Overview

PixelMorph is a secure image encryption and decryption system that combines **Chaotic maps** with **Genetic Crossover** operations to protect images in real-time. It breaks pixel correlation, scrambles structure, and maintains fidelity after decryption — making it ideal for sensitive applications like medical imaging and defense.

Core Concepts
- **Chaotic Maps:**
  - 📈 Logistic Map
  - 🌀 Henon Map
  - 🔁 Chebyshev Map
- **Genetic Operator:**
  - Row & column-wise crossover for pseudo-random pixel scrambling.
- **Encryption Logic:**
  - Bitwise XOR with chaotic key streams for diffusion.
- **Reversibility:**
  - Decryption restores exact original image (lossless).


## 📂 Folder Structure
PixelMorph/
├── main.py # Full encryption & decryption logic
├── requirements.txt # All Python dependencies
├── sample.jpg # Test image (you can replace with your own)
└── README.md # Current file

## 💻 How to Run

1. 🐍 **Install Python** (v3.8+)
2. 📁 Place your image as `loffy.jpg` in the same folder
3. 📦 Install dependencies:

```bash
pip install -r requirements.txt


