# 🧬 PixelMorph: Chaos-Based Image Encryption with Genetic Intelligence
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

💻 How to Run

1. **Install Python** (v3.8+)
2. Place your image as `sampleimage.jpg` in the same folder
3. Install dependencies:

▶️ Automatically install all dependencies using the command:
pip install -r requirements.txt


▶️ Run the program using the command:
python main.py


📊 Output:
    ✅ Original image shown

    🔐 Encrypted (scrambled) image

    🔓 Decrypted (original restored)
    
    📈 RGB histogram for all stages
    
    📉 Correlation stats table

📊 Output images:

Original Image:
![Screenshot 2025-06-18 214336](https://github.com/user-attachments/assets/6d914d0f-6ab6-4373-aac4-a7be694b751a)
Encrypted Image:
![Screenshot 2025-06-18 214400](https://github.com/user-attachments/assets/ac2511ae-f78f-4b32-82d8-9141cd9e93f6)
Decrypted Image:
![Screenshot 2025-06-18 214812](https://github.com/user-attachments/assets/cdd2144c-6752-4870-897e-cc85dfe54c50)

## 📚 Research Reference
This project is primarily based on:
**Sudeep Nooly B, Ravindra S**  
_"Design and Development of Multidimensional Chaotic Maps with Genetic Operator"_  
*International Journal of Mathematical Sciences and Computing (IJMSC), Vol. 9, No. 3, pp. 12–25, 2023.*  
📖 DOI: [10.5815/ijmsc.2023.03.02](https://doi.org/10.5815/ijmsc.2023.03.02)

Additional inspiration and theoretical foundations from:
- **El-Sayed M. El-Alfy & Khaled A. Al-Utaibi**,  
  *“An Encryption Scheme for Color Images Based on Chaotic Maps and Genetic Operators”*,  
  7th International Conference on Networking and Services, 2011.
- **N. Pareek et al. (2006)** – *Image encryption using chaotic logistic maps*
- **Liu & Wang (2011)** – *Color image encryption using one-time keys and chaotic maps*

🧩 Future Enhancements
    Add mutation (genetic operator)
    Support for grayscale/video encryption
    Cloud/web-based encryption service

🙌 Let's Connect
    📬 dasit.tanisha@gmail.com
    🌐 Linkedin: www.linkedin.com/in/tanishajdas




