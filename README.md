# Gardevoir - Task Manager API

This project, **Gardevoir**, is a **Task Management API** built with Flask, designed to perform CRUD operations for task management. It includes automated tests and uses a simple model structure to manage tasks.

---

## 🚀 Features

- **Create Tasks**: Add new tasks with a title and description.
- **Read Tasks**: Retrieve all tasks or get details of a specific task by ID.
- **Update Tasks**: Modify the title, description, or completion status of a task.
- **Delete Tasks**: Remove tasks from the system.

---

## 🛠️ Technologies Used

- **Python**: Backend logic and data handling.
- **Flask**: Web framework for building the REST API.
- **Pytest**: For automated unit testing.
- **Requests**: Used in testing for simulating API calls.

---

## 📂 Project Structure
```bash
Gardevoir/ 
├── app.py # Main application file with API endpoints 
├── tasks.py # Task model definition 
├── tests.py # Automated test cases for API validation 
└── requirements.txt # Python dependencies
```
---

## 🧑‍💻 Getting Started

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GirardiMatheus/gardevoir.git
   cd gardevoir

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Access the API at:

```bash
http://127.0.0.1:5000
```

## 🧪 Testing the API
Run the automated tests using Pytest:

```bash
pytest tests.py
```

## 📖 API Endpoints

### Base URL:

```bash
http://127.0.0.1:5000
```
### Endpoints:
| Method  | Endpoint      | Description                     | 
| ------- | ------------- | --------------------------------| 
| POST    | /tasks        | Create a new task               | 
| GET     | /tasks        | Retrieve all tasks              | 
| GET     | /tasks/<id>   | Retrieve a specific task by ID  |
| PUT     | /tasks/<id>   | Update a task by ID             |
| DELETE  | /tasks/<id>   | Delete a task by ID             |

## 📋 Models

### Task
| Field       | Type          | Description                     | 
| -------     | ------------- | --------------------------------| 
| id          | Integer       | Unique identifier for the task  | 
| title       | String        | Task title                      | 
| description | String        | Task description                |
| completed   | Boolean       | Task completion status          |

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
