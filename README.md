# 🚀 FastAPI Testing Project  

## 📖 Overview  
This project demonstrates API testing for a FastAPI application using `pytest`. It includes automated test cases to validate API endpoints.

## 🛠️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/kuwar1269/Fast-api-testing.git
cd Fast-api-testing
```

### 2️⃣ Install Dependencies  
We use `pip` and `pytest` for testing. Ensure you have Python installed.  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server  
Start the FastAPI application using Uvicorn:  
```bash
uvicorn apiserver:app --host 127.0.0.1 --port 8000 --reload
```

### 4️⃣ Run the Automated Tests  
To execute the test cases, run:  
```bash
pytest testAutomationPytest.py
```

## 📷 Screenshots  
Here are some screenshots of the working API tests:

![Test Results](images\run-fast-api.png)
![Test Results](images\fast-api.png)
![FastAPI Docs](images\run-fast-api.png)
![FastAPI Docs](images\actions.png)

## 🛠️ CI/CD with GitHub Actions  
This repository is set up with GitHub Actions to automate the testing process. Every push triggers tests automatically.

## 💡 Contributing  
If you have suggestions or improvements, feel free to open an issue or submit a pull request!

---

📌 **Author:** [Kunwarjot Singh](https://github.com/kuwar1269)

