# Steps to reproduce

1. Install deps `pipenv install --dev`
2. Run `./pants check ::`
   ```
   ./pants check ::
    17:05:59.97 [ERROR] Completed: Typecheck using MyPy - mypy failed (exit code 1).
    modules/validator.py:1: error: Skipping analyzing "email_validator": module is installed, but missing library stubs or py.typed marker
    modules/validator.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    Found 1 error in 1 file (checked 2 source files)
   ```


Running with mypy works as intended:
```
$ pipenv run mypy
Success: no issues found in 2 source files
```