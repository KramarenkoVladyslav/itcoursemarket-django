## Project Description

The **ITCourseMarket** is a Django-based RESTful API designed for managing courses and their categories. It provides CRUD operations (Create, Read, Update, Delete) on courses and categories with secure API Key authentication for restricted operations.

### Key Features:
- API Key authentication for secure access.
- Full CRUD support for:
  - **Courses**: Add, view, update, and delete courses.
  - **Categories**: Manage and organize categories.
- Seamless integration with Django's admin panel for easier management.

---

## Installation Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment using Python 3.11:

```bash
python3.11 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

Install all required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run database migrations to set up the initial database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Start the server locally:

```bash
python manage.py runserver
```

### 7. Access the Application

Open your web browser and navigate to:

- **Frontend**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## API Endpoints

### Courses

| Method | Endpoint                 | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `/api/v1/courses/`       | Retrieve all courses             |
| GET    | `/api/v1/course/<id>/`   | Retrieve a single course by ID   |
| POST   | `/api/v1/courses/`       | Create a new course              |
| DELETE | `/api/v1/course/<id>/`   | Delete a course by ID            |

## Testing the API

- Use tools like Postman or similar software.
- Test each endpoint with the appropriate HTTP method (GET, POST, DELETE).
- Ensure to include the Authorization header for secure endpoints.

## Authentication

The API uses API Key Authentication for secure access to certain operations (POST, DELETE):

1. Navigate to the Django Admin Panel at `/admin/`.
2. Generate an API Key for your user in the **Tastypie** section under **Api keys**.

Add API Key:

- **User**: Write your username.
- **Key**: Create your custom API key.

#### Create a Course (POST)

To create a course, send a POST request to `/api/v1/courses/` with the following JSON body:

```json
{
    "title": "Complete Python Guide",
    "price": 99.99,
    "students_qty": 100,
    "reviews_qty": 50,
    "category_id": 1
}
```

**Headers:**

In the headers section of your tool (e.g., Postman):

- **Key**: `Authorization`
- **Value**: `ApiKey <username>:<api_key>`

### Categories

| Method | Endpoint                 | Description                      |
|--------|--------------------------|----------------------------------|
| GET    | `/api/v1/categories/`    | Retrieve all categories          |

---


### Notes from the Author

- This project was developed using Python 3.11 to ensure compatibility and performance.
- Please make sure to use a properly configured virtual environment to avoid dependency conflicts.

With ❤️ author Vladyslav Kramarenko
