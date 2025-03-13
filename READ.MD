# Phishing Website Detection

This project is a machine learning-based tool designed to detect phishing websites. Users can input a URL to determine if it is likely phishing or safe. The tool uses various URL features, such as URL length, number of special characters, entropy, and other structural characteristics, to predict phishing sites. The app is built with Streamlit for an interactive user interface.

**Features**

Extracts URL-based features to identify phishing patterns
Uses a trained Random Forest model for accurate detection
User-friendly interface with Streamlit, allowing quick URL validation
Ensures the input URL is complete (requires http:// or https:// prefix)

**Files**

feature_extraction.py: Extracts features from a given URL for prediction.
train_model.py: Trains a machine learning model using a labeled dataset and saves it for use in the app.
app.py: The main Streamlit application file allowing users to input a URL and check if it's a phishing site.

**Dataset**

The model is trained on a dataset of URLs labeled as either phishing or legitimate, with various URL-based features used to train the classifier. The dataset should be in dataset.csv, located in the project directory.

## _Installation_

**Clone the repository:**

    git clone https://github.com/your-username/phishing-website-detection.git
    cd phishing-website-detection

**Install dependencies:**

    pip install -r requirements.txt

**Prepare the dataset:**

Make sure the dataset Dataset.csv is in the data directory. This dataset should have the features mentioned in feature_extraction.py and a target column named Type.

**Train the model:**

Run the train_model.py file to train the model and save it for the app:
python train_model.py

## _Usage_

**Run the Streamlit app:**

    streamlit run app.py
    
**Use the app:**

    Open the app in your browser.
    Enter a full URL (including http:// or https://) in the input field.
    Click the "Detect Phishing" button to see if the URL is safe or likely phishing.
    
**Project Structure**
    
    phishing_detection_tool/
    ├──data
        ├──Dataset.csv              # Dataset with URL features and labels
    ├── feature_extraction.py       # Extracts features from a given URL
    ├── train_model.py              # Trains and saves the ML model
    ├── app.py                      # Streamlit app for phishing detection
    ├── model.pkl                   # Saved machine learning model
    ├── scaler.pkl                  # Saved scaler for feature scaling
    └── README.md                   # Project documentation

**Requirements**

    Python 3.7 or higher
    streamlit
    pandas
    scikit-learn
    
**License**

This project is licensed under the MIT License.