# Rahyx: AI-Driven Steganography Framework

Rahyx is a sophisticated AI-driven steganography framework designed for secure and covert communication. By combining deep learning-based data hiding with adaptive feedback, dynamic routing, and multi-fragment transmission, the system minimizes detection risk while preserving high image quality.

---

## 📖 Overview

The project implements an end-to-end pipeline where encrypted messages are embedded into images using a neural network. A steganalysis model evaluates detection risk in real-time, allowing the system to adapt its embedding strategy dynamically.

The communication process is further strengthened using message fragmentation and risk-aware routing, making interception and reconstruction significantly more difficult for adversarial observers.

---

## ✨ Key Features

- **AI-Based Steganography:**  
  Utilizes an encoder-decoder architecture for high-capacity data hiding.

- **Real-Time Steganalysis:**  
  Integrated detection feedback loop to evaluate security risks on the fly.

- **Adaptive Embedding:**  
  Dynamically balances the trade-off between payload visibility and security.

- **Multi-Fragment Transmission:**  
  Splits messages into smaller chunks across multiple carrier images.

- **Risk-Aware Dynamic Routing:**  
  Optimizes transmission paths based on calculated detection probabilities.

- **Attack Simulation:**  
  Includes noise-based robustness evaluation to test against real-world interference.

- **Comprehensive Metrics:**  
  Tracks performance using PSNR, SSIM, and detection probability.

---

## 🔄 System Workflow

1. **Encryption:**  
   Secure the raw message using cryptographic protocols.

2. **Fragmentation:**  
   Break the encrypted data into smaller, manageable chunks.

3. **Neural Embedding:**  
   Embed fragments into carrier images using the AI Encoder.

4. **Risk Evaluation:**  
   Analyze the stego-images with a steganalysis model.

5. **Adaptive Optimization:**  
   Fine-tune embedding parameters to minimize detection risk.

6. **Transmission:**  
   Send fragments via dynamic, risk-aware routing.

7. **Reconstruction:**  
   Extract and reassemble fragments at the receiver end.

---

## 📂 Project Structure

```

Rahyx/
├── modules/
│   ├── ai_steganography/   # Neural network models (Encoder/Decoder)
│   ├── steganalysis/       # Detection risk evaluation models
│   ├── encryption/         # Message security & fragmentation
│   └── routing/            # Dynamic transmission logic
├── data/
│   ├── input_images/       # Source carrier images
│   └── output_images/      # Generated stego-images
├── final_system.py         # Main execution script
└── requirements.txt        # Project dependencies

````

---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.10+
- NVIDIA GPU (recommended for training/inference)

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/rahyx.git
cd rahyx

# Install dependencies
pip install -r requirements.txt
````

### Running the System

```bash
python final_system.py
```

---

## 📊 Metrics

The framework evaluates performance based on three core pillars:

* **PSNR (Peak Signal-to-Noise Ratio):**
  Measures the visual fidelity of the stego-image compared to the original.

* **Detection Probability:**
  Quantifies the likelihood of an adversary detecting hidden content.

* **Efficiency Score:**
  A composite metric evaluating the trade-off between capacity, quality, and security.

---

## 🚀 Future Roadmap

* **Adversarial Training:**
  Implement GAN-based training for enhanced stealth.

* **Video Steganography:**
  Extend the framework to temporal data streams.

* **RL-Based Routing:**
  Use Reinforcement Learning to optimize transmission paths dynamically.

* **Edge Deployment:**
  Optimize for hardware-level deployment on embedded systems.

---

## 👤 Author

**Vijay Kumar Gupta**

Research Intern | Samsung R&D Institute India
Electronics and Communication Engineering | RV College of Engineering
