# Recreate the CSS file due to reset

# Define the path for the CSS file
import os

css_path = "/Users/dimasjackson/blog/docs/styles/custom.css"

# Create the styles directory if it doesn't exist
os.makedirs(os.path.dirname(css_path), exist_ok=True)

# Write modern CSS content to the file
modern_css = """\
/* General styles */
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
    background-color: #f9f9f9;
}

/* Header styles */
header {
    background: linear-gradient(90deg, #4CAF50, #81C784);
    color: white;
    padding: 1rem 0;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

header h1 {
    margin: 0;
    font-size: 2.5rem;
}

/* Navigation styles */
nav {
    background: #333;
    color: white;
    display: flex;
    justify-content: center;
    padding: 0.5rem;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 1rem;
    font-weight: bold;
    transition: color 0.3s ease;
}

nav a:hover {
    color: #4CAF50;
}

/* Content styles */
main {
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
    background: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

/* Image styles */
img {
    max-width: 100%;
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Footer styles */
footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

footer a {
    color: #4CAF50;
    text-decoration: none;
    font-weight: bold;
}

footer a:hover {
    text-decoration: underline;
}
"""

# Write the CSS content to the file
with open(css_path, "w") as file:
    file.write(modern_css)

"Arquivo CSS criado com sucesso."
