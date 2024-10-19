# Flask CRUD Application with MongoDB

This is a simple Flask application that provides CRUD operations (Create, Read, Update, Delete) on a User resource using a MongoDB database. The application uses a REST API that can be accessed via HTTP requests and tested using Postman.

Read Assignment : [Click Here](./SDE%20Intern%20Assignment.pdf)

## Features

- **Create** a new user
- **Read** all users or a specific user by ID
- **Update** user information
- **Delete** a user

## Requirements

To set up and run this application, you need the following installed:

- Docker

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone areeburrub/flask-crud-mongodb
cd flask-crud-mongodb
```

### 2. Build and Run the Docker Containers

To build and run the Flask application along with MongoDB inside Docker containers, run the following commands:

```bash
docker-compose build
docker-compose up
```

This will start both the Flask app and the MongoDB database inside their respective containers.

### 3. Access the Application

- The Flask API will be accessible at `http://localhost:5000`.
- MongoDB will be accessible inside the container at `mongodb://mongo:27017`.

### 4. Stopping the Containers

To stop the running containers, press `Ctrl+C` or use:

```bash
docker-compose down
```

This will stop and remove the containers.

## REST API Endpoints

The following API endpoints are available to perform CRUD operations:

### 1. **Create a User**

**POST** `/users`

- **Request Body** (JSON):

```json
{
    "id": "1",
    "name": "Areeb ur Rub",
    "email": "areeburrub@example.com",
    "password": "securePassword123"
}
```

- **Response** (Success - 201 Created):

```json
{
    "message": "User created successfully",
    "user": {
        "id": "1",
        "name": "Areeb ur Rub",
        "email": "areeburrub@example.com"
    }
}
```

### 2. **Get All Users**

**GET** `/users`

- **Response** (Success - 200 OK):

```json
[
    {
        "id": "1",
        "name": "Areeb ur Rub",
        "email": "areeburrub@example.com"
    }
]
```

### 3. **Get a User by ID**

**GET** `/users/<id>`

- **Response** (Success - 200 OK):

```json
{
    "id": "1",
    "name": "Areeb ur Rub",
    "email": "areeburrub@example.com"
}
```

### 4. **Update a User**

**PUT** `/users/<id>`

- **Request Body** (JSON):

```json
{
    "name": "John Updated",
    "email": "john.updated@example.com",
    "password": "newSecurePassword"
}
```

- **Response** (Success - 200 OK):

```json
{
    "message": "User updated successfully",
    "user": {
        "id": "1",
        "name": "John Updated",
        "email": "john.updated@example.com"
    }
}
```

### 5. **Delete a User**

**DELETE** `/users/<id>`

- **Response** (Success - 200 OK):

```json
{
    "message": "User deleted successfully"
}
```

## Testing with Postman

1. Open Postman and create a new request for each of the endpoints listed above.
2. Set the appropriate request method (GET, POST, PUT, DELETE) and enter the URL (`http://localhost:5000`).
3. For POST and PUT requests, set the request body to raw JSON.
4. Hit **Send** and verify the responses.

## Environment Variables

You can configure the MongoDB connection and other environment variables by editing the `.env` file or updating the `docker-compose.yml`.

---

### Example `.env` file

```env
MONGO_URI=mongodb://mongo:27017
FLASK_ENV=development
SECRET_KEY=your-secret-key
```
