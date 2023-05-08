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


# The fix

1. Make sure the mypy_stubs are included in your sources, so in my case, I needed to remove `ignore_paths = ["mypy_stubs/**"]` in the `[tailor]` goal in the `pants.toml` file.

2. Generate BUILD files via `./pants tailor ::`. This should create a BUILD file for the mypy_stubs now.

3. Run `./pants check ::` again to see the desired behavior, where the mypy_stubs are recognized.