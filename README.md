# IT Service Request Tracker (Flask)

A simple web application that allows staff to submit and track internal IT service requests.

This project fulfills the IT Officer assessment task: **Software Development and Systems Integration**.

---

## 🚀 Features
- Submit a new IT service request (name, department, issue category, description)
- View all submitted requests (admin/IT view)
- Default status: **Pending**
- Mark request as **Resolved**
- Department list loaded from an external JSON API (https://jsonplaceholder.typicode.com/users)
- Data stored in SQLite database
- Simple dashboard with total, pending, and resolved counts

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Flask**
- **SQLite**
- **Requests** library (for API integration)

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
Make sure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the application
```bash
python app.py
```
Now open your browser and go to:
```
http://127.0.0.1:5000
```

### 3️⃣ Test it locally
- Click “New Request” to add a ticket.
- Use the dropdown to select department (auto-fetched from API).
- After submission, view the list and mark requests as **Resolved**.

---

## 🧩 Project Files
```
it-service-tracker/
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
├── static/                # CSS styling
└── README.md              # Documentation
```

---

## 🌐 Optional Deployment

You can host this project for free using:
- [Render](https://render.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Deta Space](https://deta.space/)

Upload all project files and set the start command:
```
python app.py
```

---

## 🧾 GitHub Instructions
To submit the project as required in the test:

1. Initialize a Git repository
```bash
git init
git add .
git commit -m "Initial commit: IT Service Request Tracker"
```
2. Create a repository on GitHub called **it-service-tracker**.
3. Connect your local repo and push:
```bash
git remote add origin https://github.com/YOUR_USERNAME/it-service-tracker.git
git branch -M main
git push -u origin main
```

Then share your GitHub link along with:
- Your full name
- Years of experience

---

## 📘 Design Notes
- Default “Pending” status is assigned automatically.
- SQLite database created automatically when the app first runs.
- The department list is fetched dynamically from a public JSON API for system integration demonstration.

---

👨‍💻 Author: [Your Name]
📅 Experience: [X Years]
📧 Contact: [Your Email]

