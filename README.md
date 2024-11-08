# Website for rst2pdf

This repo holds the website content for https://rst2pdf.github.io.

## Contributing

To contribute to this repo, make sure that your master branch is up to date and create a new branch from there.

The website content is in `source/`.

### Develop locally

This Python-based project uses [uv](https://docs.astral.sh/uv/) and [make](https://www.gnu.org/software/make/), so install those first if you don't have them already.

1. Install dependencies

   ```
   uv sync
   ```

2. Build the site

   ```
   make html
   ```

   The output files are in the `build/` directory as HTML.

3. (optional) Preview the files with `python -m http.server`.
