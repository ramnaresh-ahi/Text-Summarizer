import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    


__version__ = "0.1.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Ramnaresh Ahirwar"
SRC_REPO = "https://github.com/ramnaresh-ahi/Text-Summarizer.git"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    description = "A Python package for summarizing large text documents.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = SRC_REPO,
    project_uris = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages = setuptools.find_packages(where="src")
    
) 
    
    
