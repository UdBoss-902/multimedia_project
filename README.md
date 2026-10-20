# Django Multimedia Web Application

A simple Django web application for uploading, storing, and viewing multimedia files (images, videos, and documents) with custom CSS styling.

## Features
- Multimedia file upload form (Title, Description, File).
- Dynamic file rendering (automatic image previews and video players).
- Persistent file storage and static asset handling.

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd bincom-python-assignments

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\Activate.ps1

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations and start server:
python manage.py migrate
python manage.py runserver