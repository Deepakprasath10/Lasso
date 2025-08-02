# House Rent Price Predictor (Lasso Regression)
    A machine learning-powered web application that predicts monthly house rent prices based on various features such as number of bedrooms, size, furnishing status, location, and more. Built using Lasso Regression and deployed with Flask.

## Features
    Predicts rent prices using a trained Lasso Regression model

    ML model trained with real-world housing data

    User-friendly web interface built with HTML + CSS

    Responsive UI for desktops and tablets

    Uses joblib for model persistence and prediction

    Clean and production-ready code structure

## Tech Stack
Frontend: HTML, CSS (Custom Styled)

Backend: Flask (Python)

ML Model: Lasso Regression (Scikit-learn)

Other Tools: Pandas, NumPy, Joblib

## Project Structure
```
lasso_rent_predictor/
│
├── static/
│   └── style.css             # CSS styles
│
├── templates/
│   ├── index.html            # Input form page
│   └── result.html           # Result display page
│
├── model/
│   ├── rent_data.csv         # Dataset
│   └── lasso_model.pkl       # Trained Lasso model
│
├── app.py                    # Main Flask app
├── model_train.py            # Script to train the model
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Installation & Setup
1. Clone the repository
```
git clone https://github.com/your-username/lasso-rent-predictor.git
cd lasso_rent_predictor
```

2. Install dependencies
```
pip install -r requirements.txt
```
3. Train the model (if not already trained)
```
python model_train.py
```
4. Run the Flask app
```
python app.py
```
5. Open the app in your browser
Go to: http://localhost:5000

## Screenshots
![alt text](<Screenshot 2025-08-02 101950.png>)
![alt text](<Screenshot 2025-08-02 102107.png>)
![alt text](<Screenshot 2025-08-02 102116.png>)