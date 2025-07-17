
# Copilot Instructions for todolist Project

## Project Overview
This project is a simple Todo List application built with Django, intended for beginners. The focus is on clean architecture, maintainable code, and a user-friendly design.

## Architecture & Structure
- Use Django's standard project/app structure. Keep business logic in `services` or `usecases` modules, not in views.
- Follow Clean Architecture principles: separate concerns between models, views, templates, and business logic.
- Example structure:
  - `todolist/` (project root)
  - `app/` (main Django app)
    - `models.py` (data models)
    - `views.py` (request handlers)
    - `services/` or `usecases/` (business logic)
    - `templates/` (HTML templates)
    - `static/` (CSS/JS)

## Developer Workflows
- **Run server:** `python manage.py runserver`
- **Migrate DB:** `python manage.py makemigrations && python manage.py migrate`
- **Create superuser:** `python manage.py createsuperuser`
- **Run tests:** `python manage.py test`

## Coding Conventions
- Keep views thin; delegate logic to service/usecase layers.
- Use class-based views for CRUD where possible.
- Use Django forms for input validation.
- Keep templates simple and beginner-friendly.
- Use descriptive names for models, fields, and functions.

## Integration & Dependencies
- Use only Django and standard Python libraries unless otherwise required.
- Document any third-party packages in `requirements.txt`.

## Examples
- To add a new feature, create a service in `services/`, then call it from the view.
- For a new page, add a template in `templates/` and a corresponding view.

## References
- [Django Documentation](https://docs.djangoproject.com/)

---
If you add new conventions or patterns, update this file with clear, concrete examples.

## Implementation Process
- For every new feature or change, write out every step required to implement it before coding.
- Steps should be clear, actionable, and reproducible, so any developer or AI agent can follow them.
- Example:
  1. Define the model in `models.py`.
  2. Create a service in `services/` for business logic.
  3. Add a form in `forms.py` if user input is needed.
  4. Implement a view to handle requests.
  5. Add or update templates for UI.
  6. Update URLs as needed.
  7. Write or update tests.
  8. Document the workflow in the relevant files or in this instruction file.