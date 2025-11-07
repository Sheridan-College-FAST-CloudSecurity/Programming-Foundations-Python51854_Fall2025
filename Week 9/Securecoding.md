**Introduction to Secure coding**
Secure coding is required to reduce vulnerabilities in coding. 
**Common Security Risks in python**:
**Code Injection**:
An injection attack happens when an application includes untrusted input in a command, query, or interpreter without properly validating or escaping it — letting an attacker alter the meaning of that command. The result can be data theft, privilege escalation, remote code execution, or service disruption.

Common types (relevant to Python)

SQL injection — malicious input changes SQL queries.

Command injection — attacker manipulates shell commands (os.system, subprocess).

Code injection / eval injection — dangerous use of eval, exec, pickle.loads.

Template injection — user input rendered inside templates (e.g., Jinja2) that allows expression execution.

NoSQL / MongoDB injection — building query objects from untrusted input.

LDAP / XPath injection — similar issues in LDAP/XPath queries.

OS path / path traversal — e.g., ../../etc/passwd in file paths.
1) SQL injection — unsafe vs parameterized (psycopg2 / sqlite)

Unsafe:

query = "SELECT * FROM users WHERE username = '" + username + "';"
cursor.execute(query)    # DANGEROUS


Safe (parameterized):

cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
# or for sqlite: cursor.execute("SELECT * FROM users WHERE username = ?", (username,)) OR USE named parameters.
****cursor.execute("SELECT * FROM users WHERE username = :username",{"username":"username"})**
**NoSQL (MongoDB) injection**:
Unsafe:
# if user_input is {"$gt": ""}
db.users.find_one({"age": user_input})
Safer:
Validate types and values. Only accept expected types (e.g., ints for age).
Do not accept raw query operators from clients.
**Practical mitigation checklist**

1. Never use eval() / exec() on untrusted input. Use ast.literal_eval() or JSON.

2. Avoid pickle on untrusted data. Prefer JSON or other safe formats.

3. Call subprocess with argument lists (no shell-string concatenation). Validate/whitelist inputs.

4. Validate and sanitize input: prefer whitelists (allowed characters/types) over blacklists.

5. Least privilege: DB user should only have the minimum permissions required.

6. Escape output for the target context (HTML, JS, shell, SQL — context matters).

7. Use templating engines safely (auto-escaping, sandbox if evaluating templates).

8. Log and alert on suspicious inputs and errors (don’t leak sensitive data in logs).

9. Run static analysis (Bandit), dependency scanning (pip-audit), and regular dynamic tests.
10. Use parameterized queries
**Common File Handling Risks in Python**
**Path Traversal**

Attackers use special characters like ../ or absolute paths to “traverse” directories and read files outside allowed folders.
filename = input("Enter filename: ")
with open("/var/www/uploads/" + filename, "r") as f:
    data = f.read()
If a user enters ../../etc/passwd, it reads system files!
import os

base_path = "/var/www/uploads/"
filename = os.path.basename(filename)  # strips directory path
safe_path = os.path.join(base_path, filename)

with open(safe_path, "r") as f:
    data = f.read()
**Insecure Temporary Files**
Using predictable temp file names or not setting permissions correctly can expose data to other users on the system.
open("/tmp/temp.txt", "w").write("Sensitive info")
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"Sensitive info")
 **Improper Permissions**:
Giving files or folders overly broad permissions can let other users modify or read sensitive data.
**File Disclosure via Errors**:
Printing full paths or error messages can reveal internal file structures.
**Mitigation:**
Catch exceptions and show user-friendly messages.
Log full details internally (not to the user).
****Quick Security Checklist
****:
 1. Validate and sanitize filenames

2.  Restrict file access to specific directories

 3. Use secure temporary files

 4. Limit upload types and sizes

 5. Use exception handling and logging

 6. Never trust user-provided file paths
**Hardcoded Secrets**:
Storing sensitive information like passwords or API keys in source code.
 **Principles of Secure Coding**:
Secure coding means writing software that continues to function correctly under malicious or unexpected conditions.
These principles help ensure confidentiality, integrity, and availability of data and systems.
**1. Validate All Inputs**:

Treat all external input as untrusted — whether from users, files, APIs, or databases.

Validate type, length, format, and range.

Use whitelists (allowed values) instead of blacklists.

Sanitize inputs before using them in SQL queries, file paths, or shell commands.

**2. Use Safe APIs and Libraries**:

Prefer parameterized APIs that handle escaping automatically.

Avoid dangerous functions like eval(), exec(), and pickle.loads().

Keep third-party libraries up to date to patch known vulnerabilities.
**3. Handle Authentication and Authorization Properly**

Use strong, salted password hashing (bcrypt, argon2).

Never hardcode credentials in code or config files.

Implement role-based access control (RBAC).

Verify both authentication (who the user is) and authorization (what they can do).
**4. Principle of Least Privilege**

Give users, processes, and database accounts only the permissions they need — nothing more.

Don’t run your app as root or an admin user unnecessarily.

Use read-only access where possible.
**5. Fail Securely**

Handle errors and exceptions gracefully.

Don’t reveal sensitive system details in error messages.

Log errors securely for internal analysis.

**6. Protect Sensitive Data**

Encrypt sensitive data both at rest and in transit (use HTTPS/TLS).

Use secure random number generation (secrets module in Python).

Don’t store unnecessary personal or financial information.
**7. Avoid Security by Obscurity**

Don’t rely on hiding code, URLs, or credentials for security.

Real security comes from proper design, validation, and encryption.
**8. Use Defense in Depth**

Combine multiple layers of protection:

Input validation

Authentication

Encryption

Logging and monitoring

Regular patching and updates

Even if one layer fails, others still protect the system.
**9. Log and Monitor**

Record authentication attempts, access violations, and unexpected errors.

Protect logs from tampering.

Monitor logs for suspicious activities.

**Defensive Programming Techniques**

**Definition:**

Defensive programming is a practice of anticipating problems before they occur and writing code that handles unexpected inputs or failures safely without crashing or exposing vulnerabilities.

The goal is robust, secure, and reliable software — even when faced with invalid data, user errors, or attacks.
| Technique            | Goal                               |
| -------------------- | ---------------------------------- |
| Input Validation     | Prevent invalid or malicious input |
| Error Handling       | Graceful recovery and safety       |
| Safe Defaults        | Avoid unsafe assumptions           |
| Encapsulation        | Limit access to sensitive data     |
| Fail Securely        | No leaks or crashes                |
| Logging & Monitoring | Detect issues early                |
| Least Privilege      | Limit damage from exploits         |
| Defensive Testing    | Handle edge and error cases        |

**Tools for secure coding:**
**1. Static Code Analysis Tools**

These tools scan your code without running it to find potential vulnerabilities such as insecure imports, hardcoded credentials, or unsafe function calls.
Example Bandit:Scans Python code for common security issues (e.g., eval, pickle, weak cryptography).
**2. Dependency and Vulnerability Scanners:**

These tools analyze your libraries and dependencies for known vulnerabilities (e.g., in requirements.txt).
Example:audit:Official Python tool to check for vulnerabilities in dependencies.
