# House Price Prediction Web Application

A machine learning-powered web application that estimates house prices based on property characteristics entered by the user. The application combines a trained regression model with a user-friendly web interface, allowing users to receive price predictions without requiring any knowledge of machine learning.

The primary objective of this project is to demonstrate the integration of machine learning and web development by deploying a predictive model in an interactive application.

---

## Live Demo

🌐 **Website:** https://house-price-prediction-ml-project-5hm1.onrender.com

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Author](#author)

---

## Overview

This project was developed to gain practical experience in:

* Data preprocessing
* Machine learning model development
* Model deployment
* Backend development
* Frontend integration
* Building complete end-to-end applications

---

## Features

* Predict house prices instantly
* Clean and responsive web interface
* User-friendly prediction form
* Machine learning model integration
* Input validation
* Fast prediction response
* Easy deployment
* Organized project structure

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML5
- CSS3
- Jinja2

### Data Visualization 

* Matplotlib
* Seaborn

### Development Tools

* Git
* GitHub
* PyCharm

---

## Project Structure

```text
house-price-prediction-ml-project/
│
├── templates/
│   ├── index.html
│
├── 30-house_price_model_complete.pkl
├── 30_housedata.csv
├── app.py
├── model_tests.py
├── requirements.txt

```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RumeysaCeran/house-price-prediction-ml-project.git
```

Navigate to the project directory:

```bash
cd house-price-prediction-ml-project
```

Create a virtual environment *(optional but recommended)*:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Start the application:

```bash
uvicorn app:app --reload
```

---

## Author

**Rümeysa Ceran**

Computer Engineering Student

---
