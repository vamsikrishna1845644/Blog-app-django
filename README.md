# Django Blog Project 📖

A full-featured Django blog application with user authentication, CRUD operations, and a responsive interface. Built for learning and demonstration purposes.

## Features ✨

* User Authentication: Signup, login, logout, and password management.
* CRUD Operations: Create, read, update, and delete blog posts. Edit and delete only allowed for the post author.
* User Profiles: View and update your profile.
* Responsive Design: Works on desktop and mobile.


## Tech Stack 🛠️

* Backend: Django
* Frontend: HTML, CSS, Bootstrap
* Database: SQLite (default, can be switched to PostgreSQL)
* Authentication: Django’s built-in auth system

## Installation 🚀

1. Clone the repository

```
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply migrations

```
python manage.py migrate
```

5. Run the server

```
python manage.py runserver
```

6. Open your browser
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage 🖱️

* Register a new account or login with existing credentials.
* Create new blog posts using the Create Post button.
* Edit or delete posts you authored.
* Browse other users’ posts.

## Screenshots 📸
<img width="1881" height="912" alt="image" src="https://github.com/user-attachments/assets/ad7b51fa-28d5-4ea0-a81c-26dd3b5bc627" />


## Contributing 🤝

* Fork the repository.
* Create a new branch: `git checkout -b feature/YourFeature`.
* Commit your changes: `git commit -m 'Add some feature'`.
* Push to the branch: `git push origin feature/YourFeature`.
* Open a pull request.

## License 📜

This project is licensed under the copyright.
