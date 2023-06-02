# Assignment Model

The `Assignment` model is used to represent assignments in the application. It has the following fields:

- `title`: The title of the assignment. (CharField)
- `description`: A description of the assignment. (TextField)
- `issue_date`: The date and time when the assignment was issued. (DateTimeField)
- `due_date`: The date and time when the assignment is due. (DateTimeField)
- `course`: The course to which the assignment belongs. (ForeignKey to Course model)

The `Assignment` model has a many-to-one relationship with the `Course` model, meaning each assignment belongs to a specific course.

Two validations are implemented on the `Assignment` model:
1. The `issue_date` cannot be in the past.
2. The `due_date` must be after the `issue_date`.

If these validations fail, an error message is displayed.
