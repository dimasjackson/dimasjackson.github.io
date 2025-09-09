# Dimas Jackson Documentation Site

This project uses [MkDocs](https://www.mkdocs.org/) to build and deploy a static documentation site.

## Local Build & Preview

1. **Install MkDocs** (if not installed):
   ```sh
   pip install mkdocs
   ```
2. **Serve Locally:**
   ```sh
   mkdocs serve
   ```
   This will start a local server (usually at http://127.0.0.1:8000) so you can preview your documentation.

## Build Static Site

To build the static site files into the `site/` directory:
```sh
mkdocs build
```

## Deploy to GitHub Pages

1. **Push your changes to GitHub.**
2. **Deploy using MkDocs:**
   ```sh
   mkdocs gh-deploy
   ```
   This will build and publish your site to the `gh-pages` branch, making it available at `https://<your-username>.github.io/<your-repo>/`.

### Notes
- Make sure your repository is public and GitHub Pages is enabled for the `gh-pages` branch.
- You can customize the site by editing `mkdocs.yml` and the files in the `docs/` folder.

---
For more details, see the [MkDocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/).
