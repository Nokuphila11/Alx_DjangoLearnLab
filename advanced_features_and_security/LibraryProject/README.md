hello!

## Security Measures

- **CSRF Protection**: All forms include `{% csrf_token %}`.
- **SQL Injection Prevention**: Using Django ORM for all database queries.
- **Content Security Policy (CSP)**: Configured using `django-csp`.
- **Secure Cookies**: `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` are set to `True`.

