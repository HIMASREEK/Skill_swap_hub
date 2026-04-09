# 🤝 SkillSwap Hub

A Django-based web application where users can **share their skills, discover skills from others, and request skill exchanges** in a simple and interactive way.

## 🚀 Features

### 👤 User Authentication
- User Signup
- User Login
- User Logout

### 🧑 User Profile
- Create and manage profile
- Upload profile picture
- Add bio / personal details

### 🛠 Skill Management
- Add your own skills
- Edit your skills
- View all available skills
- See which user posted each skill

### 🔄 Skill Exchange System
- Request a skill exchange
- Offer one of your own skills in return
- Accept exchange requests
- Reject exchange requests
- View request details

### ⭐ Review System
- Leave a review after a successful exchange
- Rating + comment system

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3, Bootstrap
- **Backend:** Python, Django
- **Database:** SQLite

## 📌 Project Objective
The main objective of this project is to create a platform where users can **learn from each other by exchanging skills**, making learning more collaborative, accessible, and community-driven.

## 🎥 Project Demo
<img width="1902" height="851" alt="Screenshot 2026-04-09 001809" src="https://github.com/user-attachments/assets/e3f88a64-4983-4898-a38a-2aac66d2f0ff" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8a7d7b5b-b9e6-4a8f-b5f5-8267d3c07b02" />
<img width="1846" height="873" alt="image" src="https://github.com/user-attachments/assets/0566c5ed-1337-40e3-9464-051867b856da" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bae9f8a5-eb49-47eb-a4d3-a1a49bc75a2a" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7b24da23-1349-48f8-9c74-c1f8de95bd2d" />
<img width="1775" height="834" alt="image" src="https://github.com/user-attachments/assets/943aa94a-6ee4-442e-ac98-304e339a74ac" />
<img width="1688" height="747" alt="image" src="https://github.com/user-attachments/assets/1e01e858-8efe-4399-b213-cbde21d79944" />

[Click here to watch the SkillSwap Hub demo](

https://github.com/user-attachments/assets/4e8ffa82-8601-497a-bf42-e32d23685265

)

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/skillswaphub.git
```

### 2️⃣ Navigate to the project folder
```bash
cd skillswaphub
```

### 3️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 4️⃣ Activate the virtual environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Mac/Linux:
```bash
source venv/bin/activate
```

### 5️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Create superuser (optional)
```bash
python manage.py createsuperuser
```

### 8️⃣ Run the development server
```bash
python manage.py runserver
```

### 9️⃣ Open in browser
```bash
http://127.0.0.1:8000/
```

## 🔐 Admin Panel (Optional)
To access the Django admin panel, visit:

```bash
http://127.0.0.1:8000/admin/
```

## 📂 Project Structure

```bash
skillswaphub/
│
├── users/                  # User authentication & profile management
├── skills/                 # Skill add/edit/list functionality
├── exchanges/              # Exchange request & review system
├── media/                  # Uploaded profile pictures
├── static/                 # CSS and static assets
├── templates/              # HTML templates
├── db.sqlite3
├── manage.py
└── README.md
```

## 🎯 Future Improvements
- Add search and filter for skills
- Add skill categories
- Add chat system between users
- Add notifications for exchange requests
- Deploy the application online

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and improve the project.

## 📫 Contact
- **LinkedIn:** [www.linkedin.com/in/himasree28](https://www.linkedin.com/in/himasree28/)

---
⭐ If you like this project, don't forget to give it a star!
