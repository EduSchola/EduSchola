# EduSchola Django Project

EduSchola is an educational platform aimed at connecting students, teachers, and parents. This Django project serves as the backend API for the EduSchola application.

## Getting Started

To run the EduSchola Django project locally, follow these steps:

1. Clone the repository: `$ git clone https://github.com/EduSchola/EduSchola.git`
2. Navigate to the project directory: `$ cd eduschola/backend`
3. Create a virtual environment: `$ python3 -m venv env`
4. Activate the virtual environment:
   - On macOS and Linux: `$ source env/bin/activate`
   - On Windows: `$ .\env\Scripts\activate`
5. Install the project dependencies: `$ pip install -r requirements.txt`
6. Run database migrations: `$ python manage.py migrate`
7. Start the development server: `$ python manage.py runserver`
8. Access the API at `http://localhost:8000/`

## Endpoints

Below are the available API endpoints for the EduSchola Django project:

### GET /students

- General:
  - Returns a list of student objects.

- Sample: $ curl http://127.0.0.1:8000/students/
{
    "success": true,
    "data": [
        {
            "student_id": "8fe4eb9b-9ce4-4cd2-837f-1b41ca80429e",
            "user": null,
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": null,
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        },
        {
            "student_id": "5b02014f-6a47-4bf7-95f5-24f3b998c674",
            "user": null,
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": null,
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        },
        {
            "student_id": "371661bd-34b8-4be0-b051-8bf3027708d3",
            "user": null,
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": null,
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        },
        {
            "student_id": "3cca7130-c9d8-47be-8262-990a4af0e366",
            "user": null,
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": null,
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        },
        {
            "student_id": "aa563bc1-48c2-4ad9-9dee-cb92ac2d570d",
            "user": {
                "username": "student07",
                "role": "student",
                "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
                "first_name": "John",
                "last_name": "Doe"
            },
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": {
                "user": "a12b95c6-062a-4e90-a773-53e0e38427d0",
                "tel": "1234567890",
                "email": "jane.smith@example.com",
                "address": "123 Street, City"
            },
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        }
    ]
}

### GET /students/{student_id}

- General:
  - Returns the details of a specific student.
  - Requires the `student_id` path parameter.

- Sample: $ curl http://127.0.0.1:8000/students/6b159344-d4fe-4862-82b1-aa0f33a5a398/
{
    "success": true,
    "data": {
        "student": {
            "student_id": "aa563bc1-48c2-4ad9-9dee-cb92ac2d570d",
            "user": {
                "username": "student07",
                "role": "student",
                "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
                "first_name": "John",
                "last_name": "Doe"
            },
            "date_of_birth": "2005-01-01",
            "phone_number": "9876543210",
            "address": "456 Avenue, City",
            "parent": {
                "user": "a12b95c6-062a-4e90-a773-53e0e38427d0",
                "tel": "1234567890",
                "email": "jane.smith@example.com",
                "address": "123 Street, City"
            },
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
        },
        "user": {
            "username": "student07",
            "role": "student",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "first_name": "John",
            "last_name": "Doe"
        }
    }
}

### POST /students

- General:
  - Creates a new student.
  - Requires a JSON object in the request body with the student details.
  - Returns details of student.

- Sample: $ curl http://127.0.0.1:8000/students -X POST -H "Content-Type:application/json" -d "{
  "user": {
    "username": "student08",
    "password": "password123",
    "role": "student",
    "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
    "first_name": "John",
    "last_name": "Doe"
  },
  "parent": {
    "user": {
      "username": "parent08",
      "password": "password456",
      "role": "parent",
      "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
      "first_name": "Jane",
      "last_name": "Smith"
    },
    "tel": "1234567890",
    "email": "jane.smith@example.com",
    "address": "123 Street, City"
  },
  "date_of_birth": "2005-01-01",
  "phone_number": "9876543210",
  "address": "456 Avenue, City",
  "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
}"

{
    "success": true,
    "data": {
        "student_id": "aa563bc1-48c2-4ad9-9dee-cb92ac2d570d",
        "user": {
            "username": "student07",
            "role": "student",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "first_name": "John",
            "last_name": "Doe"
        },
        "date_of_birth": "2005-01-01",
        "phone_number": "9876543210",
        "address": "456 Avenue, City",
        "parent": {
            "user": "a12b95c6-062a-4e90-a773-53e0e38427d0",
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
    }
}

### PATCH /students/{student_id}

- General:
  - Updates the details of a specific student.
  - Requires the `student_id` path parameter.
  - Requires a JSON object in the request body with the student details to be updated.
  - Returns the details of student modified with a success value of True.

- Sample: $ curl http://localhost:8000/students/6b159344-d4fe-4862-82b1-aa0f33a5a398/ -X PATCH -H "Content-Type: application/json" -d "{  
  "user": {
    "username": "new_username",
    "email": "new_email@example.com"
  },
  "date_of_birth": "2005-01-01",
  "phone_number": "9876543210",
  "address": "456 Avenue, City"
}"

{
    "success": true,
    "data": {
        "student_id": "02261438-9ce1-4069-bb90-3438a00cbf55",
        "user": {
            "username": "new_username",
            "role": "student",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "first_name": "John",
            "last_name": "Doe"
        },
        "date_of_birth": "2005-01-01",
        "phone_number": "9876543210",
        "address": "456 Avenue, City",
        "parent": {
            "user": "5a3b44f9-bcd6-4e8a-9156-c5a3178aa740",
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da"
    }
}

### GET /staff

- General:
  - Returns a list of staff objects.

- Sample: $ curl http://127.0.0.1:8000/staff/

{
    "success": true,
    "data": [
        {
            "staff_id": "11271bfb-79f3-4010-9659-9384179b4047",
            "user": {
                "username": "irakin",
                "role": "staff",
                "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
                "first_name": "Irene",
                "last_name": "Akinola"
            },
            "qualification": "M. Ed.",
            "tel": "09076587767",
            "email": "irakin@email.com",
            "address": "No 1 Nig rd",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "subjects": [
                "49c20d71-4522-465f-b2e3-3cd810c7be00"
            ],
            "staff_role": "Admin"
        },
        {
            "staff_id": "a0056a9a-b67e-48ad-a8ce-b5911bfb852c",
            "user": {
                "username": "updated_staff_user1",
                "role": "staff",
                "school": null,
                "first_name": "updated_staff_firstname",
                "last_name": "updated_staff_lastname"
            },
            "qualification": "Updated qualification",
            "tel": "9876543210",
            "email": "updated_staff@example.com",
            "address": "456 Updated Street",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "subjects": [],
            "staff_role": "Updated instructor"
        }
    ]
}

### GET /staff/{staff_id}

- General:
  - Returns the details of a specific staff.
  - Requires the `staff_id` path parameter.

- Sample: $ curl http://127.0.0.1:8000/staff/ed250428-0a7b-4845-84a2-ecb26696fea2/

{
    "success": true,
    "data": {
        "staff_id": "a0056a9a-b67e-48ad-a8ce-b5911bfb852c",
        "user": {
            "username": "updated_staff_user1",
            "role": "staff",
            "school": null,
            "first_name": "updated_staff_firstname",
            "last_name": "updated_staff_lastname"
        },
        "qualification": "Updated qualification",
        "tel": "9876543210",
        "email": "updated_staff@example.com",
        "address": "456 Updated Street",
        "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
        "subjects": [],
        "staff_role": "Updated instructor"
    }
}

### POST /staff

- General:
  - Creates a new staff.
  - Requires a JSON object in the request body with the teacher details.

- Sample: $ curl http://127.0.0.1:8000/staff -X POST -H "Content-Type:application/json" -d "{
  "user": {
    "username": "staff_user10",
    "first_name":"staff_firstname",
    "last_name":"staff_lastname",
    "password": "staff_password",
    "role": "staff"
  },
  "qualification": "Masters in Education",
  "tel": "1234567890",
  "email": "staff@example.com",
  "address": "123 Staff Street",
  "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
  "staff_role":"Instructor",
  "subjects": []
}"

{
    "success": true,
    "data": {
        "staff_id": "a0056a9a-b67e-48ad-a8ce-b5911bfb852c",
        "user": {
            "username": "staff_user1",
            "role": "staff",
            "school": null,
            "first_name": "staff_firstname",
            "last_name": "staff_lastname"
        },
        "qualification": "Masters in Education",
        "tel": "1234567890",
        "email": "staff@example.com",
        "address": "123 Staff Street",
        "school": null,
        "subjects": [],
        "staff_role": "Instructor"
    }
}

### PATCH /staff/{staff_id}

- General:
  - Updates the details of a specific teacher.
  - Requires the `staff_id` path parameter.
  - Requires a JSON object in the request body with the teacher details to be updated.

- Sample: $ curl http://localhost:8000/staff/ed250428-0a7b-4845-84a2-ecb26696fea2/ -X PATCH -H "Content-Type: application/json" -d "{
  "user": {
    "username": "updated_staff_user1",
    "first_name":"updated_staff_firstname",
    "last_name":"updated_staff_lastname",
    "password": "updated_staff_password",
    "role": "staff"
  },
  "qualification": "Updated qualification",
  "tel": "9876543210",
  "email": "updated_staff@example.com",
  "address": "456 Updated Street",
  "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
  "staff_role":"Updated instructor",
  "subjects": []
}"

{
    "success": true,
    "data": {
        "staff_id": "ed250428-0a7b-4845-84a2-ecb26696fea2",
        "user": {
            "username": "updated_staff_user1",
            "role": "staff",
            "school": null,
            "first_name": "updated_staff_firstname",
            "last_name": "updated_staff_lastname"
        },
        "qualification": "Updated qualification",
        "tel": "9876543210",
        "email": "updated_staff@example.com",
        "address": "456 Updated Street",
        "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
        "subjects": [],
        "staff_role": "Updated instructor"
    }
}

### GET /parents

- General:
  - Returns a list of parent objects.

- Sample: $ curl http://127.0.0.1:8000/parents/

{
    "success": true,
    "data": [
        {
            "parent_id": "df1c81be-1a2e-4d9b-a9dc-3aca925d0c67",
            "user": null,
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        {
            "parent_id": "b063036b-918b-47d0-b1f7-f7993fdcea56",
            "user": null,
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        {
            "parent_id": "124d6d81-ad3b-455c-9ad8-cd0a7e4eecbf",
            "user": null,
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        {
            "parent_id": "39c9d641-a2d2-4bae-b9dd-0eabff1a5ced",
            "user": null,
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        },
        {
            "parent_id": "63a078ca-1376-4bf8-b100-72c140857d61",
            "user": "a12b95c6-062a-4e90-a773-53e0e38427d0",
            "tel": "1234567890",
            "email": "jane.smith@example.com",
            "address": "123 Street, City"
        }
    ]
}

### GET /parents/{parent_id}

- General:
  - Returns the details of a specific parent.
  - Requires the `parent_id` path parameter.

- Sample: $ curl http://127.0.0.1:8000/parents/1a5ca628-b5cf-41ce-b6e2-39a18d2a24d0/

{
    "success": true,
    "data": {
        "parent_id": "63a078ca-1376-4bf8-b100-72c140857d61",
        "user": {
            "username": "parent07",
            "role": "parent",
            "school": "525567f2-c0bd-4caa-8d2f-e1d157ead4da",
            "first_name": "Jane",
            "last_name": "Smith"
        },
        "tel": "1234567890",
        "email": "jane.smith@example.com",
        "address": "123 Street, City"
    }
}

### PATCH /parents/{parent_id}

- General:
  - Updates the details of a specific parent.
  - Requires the `parent_id` path parameter.
  - Requires a JSON object in the request body with the parent details to be updated.

- Sample: $ curl http://localhost:8000/parents/1a5ca628-b5cf-41ce-b6e2-39a18d2a24d0/ -X PATCH -H "Content-Type: application/json" -d "{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "user": {
    "username": "johndoe",
    "password": "newpassword123"
  }
}"

{
    "success": true,
    "data": {
        "user": "5a3b44f9-bcd6-4e8a-9156-c5a3178aa740",
        "tel": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Street, City"
    }
}

## Error Handling

Errors are returned as JSON objects in the following format:

```json
{
  "success": false,
  "error": 404,
  "message": "Student not found"
}

The API may return the following error types:

- 404: Not Found
- 400: Bad Request
- 422: Unprocessable Entity
- 405: Method Not Allowed
- 500: Internal Server Error


## Postman Test Collection

We provide a Postman test collection that contains a set of preconfigured API tests for this project. You can use this collection to validate the API endpoints and their expected behavior.

### Importing the Test Collection

To import the Postman test collection into Postman, follow these steps:

1. Open Postman.
2. Click on the "Import" button in the top left corner.
3. Select the "Import From File" option.
4. Navigate to the `Eduschola_postman_tests` folder in this repository.
5. Choose the test collection file (`EduSchola.postman_collection.json`).
6. Click "Open" to import the collection.

### Running the Tests

Once you have imported the test collection, you can run the tests by selecting the desired request(s) or the entire collection and clicking the "Send" button. The tests will be executed, and the results will be displayed in the Postman interface.

Please note that some tests may require specific data to be set up or authentication to be provided. Refer to the test collection documentation for any additional instructions or prerequisites.


