**Structured Logging**
What is Structured Logging?

Structured logging is a way of recording log messages in a consistent, machine-readable format (usually JSON or key-value pairs) instead of plain text.

Key Idea: Instead of just writing a string message:
2025-10-06 11:00:00 - INFO - User logged in: user123
You log structured data:
{
  "timestamp": "2025-10-06T11:00:00",
  "level": "INFO",
  "event": "user_login",
  "user_id": "user123",
  "ip": "192.168.1.10"
}
**Why Use Structured Logging?**

Advantages:

Machine-readable – Easy to parse with tools (ELK, Splunk, Graylog).

Queryable – Search, filter, and aggregate logs by fields.

Consistent – All logs have same fields for easy analysis.

Supports automation – Good for monitoring, alerts, and dashboards.

**When to Use Structured Logging:
**
Microservices architectures.

Cloud-native applications.

Systems with centralized log collection and analysis.
**What Are JSON-Formatted Logs?**

JSON logs are log messages written in JSON (JavaScript Object Notation) instead of plain text.

They are structured and machine-readable, making it easier to parse, analyze, and send to log management tools like ELK stack, Splunk, or Graylog.

Applications needing detailed metrics or observability.
**Why Use JSON Logs?

Advantages:**

Machine-readable – easy to parse programmatically.

Queryable – search/filter by fields like user_id or event.

Consistent structure – every log has same fields.

Supports monitoring and alerting – integrates well with dashboards.

Machine-readable – easy to parse programmatically.

Queryable – search/filter by fields like user_id or event.

Consistent structure – every log has same fields.

Supports monitoring and alerting – integrates well with dashboards.
**What are Handlers?**

In Python logging, a handler decides where the log messages go.

Handlers receive the log records from a logger and send them to a destination (console, file, network, etc.).

You can attach multiple handlers to a single logger to send logs to different places simultaneously.
Common handlers:

StreamHandler → Console or standard output

FileHandler → Log file

RotatingFileHandler → File with rotation (when file gets big, new one starts)

TimedRotatingFileHandler → New file every time interval (e.g., daily)

SMTPHandler → Send logs via email

HTTPHandler → Send logs via HTTP POST/GET

NullHandler → Ignores logs (useful for libraries)

