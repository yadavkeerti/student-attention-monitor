# Real-time attention monitoring system using computer vision with dynamic scoring mechanism

## 📌 Overview

This project presents a real-time computer vision system designed to monitor student attention using webcam input. It evaluates engagement by analyzing facial cues such as eye state and head orientation, and introduces a continuous attention scoring mechanism.

---

## 🚀 Key Features

* 👤 Face Detection using Haar Cascade
* 👁️ Eye Detection for drowsiness analysis
* 🧭 Head Direction Tracking (Left / Right / Center)
* 📊 Real-Time Attention Score (0–100)
* 🧠 Intelligent Classification:

  * Attentive
  * Distracted
  * Drowsy
* ⚡ Lightweight & real-time 

---

## 🧠 System Workflow

```text
Webcam Input → Face Detection → Eye Detection + Head Tracking → Score Calculation → Attention Classification
```

---

## ⚙️ Tech Stack

* Python
* OpenCV
* NumPy

---

## 📊 Attention Scoring Mechanism

The system computes an attention score dynamically based on visual cues:

| Condition    | Score Impact |
| ------------ | ------------ |
| Eyes Closed  | -30          |
| Looking Away | -20          |

### Final Classification:

* **Score > 70** → Attentive
* **Score 40–70** → Distracted
* **Score < 40** → Drowsy

---

## ⭐ Novel Contribution

Unlike traditional approaches that perform only binary classification (attentive vs inattentive), this project introduces a **continuous attention scoring system** that provides a more nuanced and real-time measure of engagement.

---

## 📸 Output

The system displays:

* Face bounding box
* Eye detection
* Head direction
* Attention Score
* Final Attention Status

---

## ⚠️ Limitations

* Performance depends on lighting conditions
* Limited accuracy compared to deep learning models

---

## 🚀 Future Improvements

* Integration with Mediapipe facial landmarks
* Deep learning-based attention prediction (CNN/RNN)
* Emotion recognition integration
* Multi-person tracking

---

## 👩‍💻 Author

**Keerti Yadav**
