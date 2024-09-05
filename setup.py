from setuptools import find_packages, setup

setup(
    name="firsttest",
    version="0.0.1",
    author="nadir haddadi",
    author_email="nadir.97@hotmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
)
