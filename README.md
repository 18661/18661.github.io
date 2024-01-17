# 18-661/461 Website

Building the site:

- Any python installation with `jinja2` and `pyyaml` should work:
    ```sh
    pip install jinja2 pyyaml
    ```
- Populate/update files in `data/`. See the existing files for formatting.
- Only "structural" changes need to be made on `template.html`.
- Build the website:
    ```sh
    python render.py
    ```
