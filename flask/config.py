# config.py

import os

# Define the base paths for images and documents
IMAGE_PATH = "/static/images/"
DOCUMENT_PATH = "/static/documents/"

# Example image and document constants
PROFILE_IMAGE = f"{IMAGE_PATH}algadipe_joshua.jpeg"
RESUME_PDF = f"{DOCUMENT_PATH}joshua_algadipe.pdf"
CHAT_ICON = f"{IMAGE_PATH}chat.png"
# Define the path for the gallery JSON file
GALLERY_JSON_PATH = os.path.join("static", "json", "gallery.json")
# Define the path for the vlog JSON file
VLOG_JSON_PATH = os.path.join("static", "json", "vlog.json")

# pages
PROFILE_PAGE = "pages/profile.html"
GALLERY_PAGE = "pages/gallery.html"
VLOG_PAGE = "pages/vlog.html"
CONCERN_PAGE = "pages/concern.html"
ERROR_404_PAGE = "error/404.html"

# Configure available languages
LANGUAGES = {
    'en': 'English',
    'ceb': 'Cebuano',
    'fr': 'French',
    'fil_PH': 'Tagalog',
}

# Set the default locale
BABEL_DEFAULT_LOCALE = 'en'
EN_LOCALE = 'en'
CEB_LOCALE = 'ceb'
FR_LOCALE = 'fr'
TL_LOCALE = 'fil_PH'