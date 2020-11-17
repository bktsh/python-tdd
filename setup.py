from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2", "pytesseract>=0.2.6", "tesseract>=0.1.3", "opencv-python>=4.1.0.25", "fpdf>=1.7.2"]

setup(
    install_requires=requirements,
    py_modules=['lib.calculator', 'lib.helloworld'],
    packages=find_packages(),
    # packages=['lib'],
    name = "lib",
    version = "1.0.0",
    description = "Learning python",
    author = "Hashem Baktash",
    author_email = "Hashem.Baktash@gmail.com",
    url = "http://example.com",
    download_url = "https://github.com/bktsh/python-tdd",
    keywords = ["encoding", "i18n", "xml"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: NONE for now",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: TDD :: Learning",
    ],
    long_description_content_type="text/markdown",
    long_description = """WELCOME TO PYTHON TDD"""
)
