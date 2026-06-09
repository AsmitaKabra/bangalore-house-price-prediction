# 🏠 Bangalore House Price Prediction

An end-to-end Machine Learning project that predicts residential property prices in Bangalore based on key features such as location, total square footage, number of bathrooms, and BHK configuration.

The project covers the complete ML lifecycle, including data preprocessing, feature engineering, outlier detection, model training, evaluation, and deployment using Streamlit.

---

## 🚀 Project Overview

Buying or selling property often requires understanding the fair market value of a house. This project aims to build a predictive model that estimates house prices in Bangalore using historical housing data.

The application allows users to enter property details and instantly receive a predicted price through an interactive Streamlit web interface.

---

## ✨ Features

* Data Cleaning and Preprocessing
* Feature Engineering
* Outlier Detection and Removal
* Location-Based One-Hot Encoding
* Feature Scaling using StandardScaler
* Model Training and Evaluation
* Interactive Streamlit Web Application
* Real-Time House Price Prediction

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Seaborn

### Model Serialization

* Pickle

---

## 📊 Machine Learning Workflow

### 1. Data Collection

Housing dataset containing information such as:

* Location
* Total Square Feet
* Number of Bathrooms
* BHK
* Price

### 2. Data Cleaning

* Removed unnecessary columns
* Handled missing values
* Standardized data formats

### 3. Feature Engineering

Created additional meaningful features such as:

* Price Per Square Foot

### 4. Outlier Removal

Applied statistical and domain-based techniques to remove:

* Unrealistic square footage values
* Abnormal price-per-square-foot records

### 5. Data Encoding

Converted categorical location data into numerical format using One-Hot Encoding.

### 6. Feature Scaling

Standardized numerical features using StandardScaler.

### 7. Model Training

Multiple regression models were evaluated, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* KNN Regressor
* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor

### 8. Model Selection

Linear Regression was selected as the final model due to its strong performance and generalization capability.

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application where users can:

* Select property location
* Enter total square footage
* Specify number of bathrooms
* Specify BHK configuration
* Receive an estimated property value instantly

---

## 📂 Project Structure

```text
bangalore-house-price-prediction/
│
├── app.py
├── EDA.ipynb
├── house_price_model.pkl
├── scaler.pkl
├── columns.json
├── requirements.txt
├── README.md
└── images/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AsmitaKabra/bangalore-house-price-prediction.git
```

Move into the project directory:

```bash
cd bangalore-house-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

*Add screenshots of your Streamlit application here.*

```markdown
![Home Page](images/home_page.png)
```

---

## 🎯 Future Improvements

* Deploy the application publicly
* Integrate advanced ensemble models
* Add market trend visualizations
* Improve UI/UX design
* Support additional property features

---

## 👩‍💻 Author

**Asmita Kabra**

Aspiring Data Scientist | Machine Learning Enthusiast | Full Stack & AI Enthusiast

Live Demo: https://house-price-prediction-bangalore.streamlit.app/
GitHub: https://github.com/AsmitaKabra
