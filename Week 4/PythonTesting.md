
What is Unit Testing?

Unit testing tests the smallest parts of code—usually functions or classes—in isolation.

Goal: Verify that each “unit” behaves as expected.

Helps catch bugs early, ensures code reliability, and supports refactoring safely.

2. Why Unit Testing is Important

Detects errors early in development.

Makes code more maintainable.

Provides documentation of expected behavior.

Enables safe refactoring because tests catch regressions.

Supports automation in CI/CD pipelines.

3. Python Unit Testing Frameworks
a) unittest (built-in)
b) pytest (modern alternative)

Simple, flexible, and widely used.

Supports fixtures, parameterization, and plugins.
Unit Testing Best Practices

Test one thing at a time – keep tests focused.

Name tests clearly – e.g., test_add_with_positive_numbers.

Isolate tests – no dependencies on other tests.

Use fixtures for setup/teardown – avoid repetitive code.

Automate tests – integrate with CI/CD pipelines.

Use mocks/stubs for external dependencies (files, DB, APIs).
Part of the Python standard library.

Uses TestCase classes, assertions, and test suites.
