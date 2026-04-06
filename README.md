# 📉 Customer Churn Prediction using ANN 

## 🚀 Project Overview

This project is a **Customer Churn Prediction System** built using an **Artificial Neural Network (ANN)**.

---

## 🎯 Objective

The main goal of this project is to:

* Predict whether a customer will churn or not
* Apply **Artificial Neural Networks on tabular data**
* Understand performance of ANN compared to traditional ML models

---

## 📊 Dataset Details

* Dataset: **Churn_Modelling.csv**
* Features include:

  * Credit Score
  * Geography
  * Gender
  * Age
  * Tenure
  * Balance
  * Number of Products
  * Has Credit Card
  * Is Active Member
  * Estimated Salary

---

## 🧠 Model Architecture

* **Model Type:** Artificial Neural Network (ANN)
* **Layers:**

  * Input Layer: **11 neurons**
  * Hidden Layer: **20 neurons**
  * Hidden Layer: **11 neurons**
  * Output Layer: **1 neuron**

---

## ⚙️ Model Configuration

* **Loss Function:** Binary Cross Entropy
* **Optimizer:** Adam
* **Epochs:** 30
* **Evaluation Metric:** Accuracy

---

## 📈 Model Performance
* **Accuracy:** **85.55%**

---

## 🔧 Preprocessing Steps

* Encoding categorical variables (Geography, Gender)
* Feature scaling using standardization
* Train-test split
---

## ⚙️ Technologies & Libraries Used

| Library                | Purpose                    |
| ---------------------- | -------------------------- |
| **Pandas**             | Data preprocessing         |
| **NumPy**              | Numerical operations       |
| **Scikit-learn**       | Preprocessing & evaluation |
| **TensorFlow / Keras** | Building ANN model         |

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash id="p1q2r3"
git clone https://github.com/Shrey-2828/customer-churn-ann.git
cd customer-churn-ann
```

### 2. Install Dependencies

```bash id="s4t5u6"
pip install -r requirements.txt
```

### 3. Run the Application

```bash id="v7w8x9"
streamlit run app.py
```

---

## 📁 Project Structure

```id="y1z2a3"
customer-churn-ann/
│
├── Churn_Modelling.csv   # Dataset
├── ANN_Churn.ipynb       # Jupyternotebook
└── README.md
```
---

## 📈 Future Improvements

* ✅ Build full **Streamlit UI for user interaction**
* Deploy the application online
* Improve model accuracy using hyperparameter tuning
* Try advanced architectures (Dropout, BatchNorm)

---

## 📈 Key Takeaway

> Artificial Neural Networks can effectively model **complex patterns in customer behavior**,
> achieving strong performance (**85.55% accuracy**) on churn prediction tasks.

---

## 👨‍💻 Author

Developed by **Shrey Patel**

---

⭐ If you found this project useful, consider giving it a star!
