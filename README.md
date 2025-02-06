# Deep Learning Implementation for Color Recognition Using CNN with Camera Detection

## 📌 Project Description

This project implements **Deep Learning** using the **Convolutional Neural Network (CNN)** method for color recognition based on camera detection. the aim of developing a system that can accurately recognize colors under various lighting conditions and backgrounds.

## 🎯 Objectives

- Design and implement a **CNN model** for color recognition.
- Measure the **accuracy of the model** in recognizing colors from test images.
- Analyze the factors affecting **CNN model performance** in color recognition with camera detection.

## 🏗️ Research Methodology

1. **Dataset Preparation**
   - The dataset consists of images with variations of primary colors (**red, blue, yellow, and black**).
   - Images are collected under different natural and artificial lighting conditions.
2. **CNN Modeling**
   - The training process utilizes **Convolutional Neural Networks (CNN)** with multiple **convolutional, pooling, and fully connected layers**.
   - The model is trained using optimal parameters such as **number of epochs, batch size, and learning rate**.
3. **Model Testing**
   - The model is tested in **real-time** using a camera to recognize colors in different environmental conditions.
   - Evaluation is conducted using a **Confusion Matrix** to determine classification accuracy.

## 📊 Results and Discussion

- **CNN model achieved 100% accuracy** on the test dataset.
- Real-time testing showed that the model performs well under various lighting conditions.
- Factors affecting model performance:
  - **Camera quality**
  - **Environmental lighting**
  - **Object background**

## 🔥 Conclusion

- The CNN model successfully recognized colors with **high accuracy**.
- This model can be adapted for various applications such as **automated monitoring systems, object classification, and autonomous navigation**.
- Future research is recommended to enhance dataset quality and apply image enhancement techniques to make the model more adaptive to different environmental conditions.

## 🚀 Technologies Used

- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **Jupyter Notebook / Google Colab**

## 📂 Directory Structure

```
├── dataset/                # Collection of images for training and validation
├── models/                 # Trained model files (.h5)
├── src/                    # Main program code
│   ├── train.py            # Script for training the model
│   ├── test.py             # Script for testing the model
│   ├── real_time_test.py   # Script for real-time testing
├── README.md               # Project documentation
```

## 📜 References

- **LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444.**
- **Krizhevsky, A., Sutskever, I., & Hinton, G. (2012). ImageNet Classification with Deep Convolutional Neural Networks.**

---

✨ **Created by:** *Dewi Yuliana*

