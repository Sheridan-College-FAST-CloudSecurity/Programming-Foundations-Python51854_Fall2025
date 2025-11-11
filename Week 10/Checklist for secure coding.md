| Category                            | Action Item                                 | Notes / Tools                             |
| ----------------------------------- | ------------------------------------------- | ----------------------------------------- |
| **Input Validation & Sanitization** | Validate user inputs (length, type, format) | Regex, Pydantic models                    |
|                                     | Escape special characters                   | Prevent SQL Injection, XSS                |
|                                     | Use parameterized queries                   | e.g., SQLite `?` placeholders, SQLAlchemy |
| **Authentication & Authorization**  | Use strong password hashing                 | bcrypt, Argon2                            |
|                                     | Enforce strong password policies            | Min length, complexity                    |
|                                     | Implement MFA                               | Optional but recommended                  |
|                                     | Role-based access control (RBAC)            | Check roles on sensitive endpoints        |
| **Sensitive Data Protection**       | Encrypt data at rest                        | Fernet, AES, DB encryption                |
|                                     | Encrypt data in transit                     | HTTPS/TLS                                 |
|                                     | Use environment variables for secrets       | Never hardcode keys or tokens             |
| **Session & Token Management**      | Use secure tokens (JWT, opaque tokens)      | Store securely, validate on each request  |
|                                     | Set token expiry & implement revocation     | Prevent stolen token misuse               |
| **Error Handling & Logging**        | Avoid exposing sensitive info               | Use generic messages to client            |
|                                     | Log securely                                | Include timestamps, no secrets            |
| **Secure Coding Practices**         | Avoid `eval()` / `exec()` with user input   | Critical for Python security              |
|                                     | Keep dependencies updated                   | pip list --outdated, safety checks        |
| **Web Security Essentials**         | Prevent XSS & CSRF                          | Escape HTML, use CSRF tokens              |
|                                     | Set secure HTTP headers                     | CSP, HSTS, X-Frame-Options                |
|                                     | Secure cookies                              | `HttpOnly`, `Secure` flags                |
| **Database & File Security**        | Use least-privilege DB accounts             | Limit access to tables                    |
|                                     | Sanitize file paths                         | Prevent path traversal attacks            |
|                                     | Scan uploaded files                         | Optional malware scanning                 |
| **Network & API Security**          | Use HTTPS                                   | Encrypt all requests                      |
|                                     | Rate-limit APIs                             | Prevent brute force & abuse               |
|                                     | Validate tokens                             | JWT signature verification or DB check    |
| **Testing & Monitoring**            | Static code analysis                        | Bandit, pylint, mypy                      |
|                                     | Dynamic security testing                    | OWASP ZAP, penetration tests              |
|                                     | Unit & integration tests                    | Include security scenarios                |
|                                     | Monitor runtime for anomalies               | Logging & alerting                        |
