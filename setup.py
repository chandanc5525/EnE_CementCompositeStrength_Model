from setuptools import setup, find_packages

setup(
    name='Machine Learning Model',
    version='0.1.0',
    author='Chandan Chaudhari',
    author_email='chaudhari.chandan22@gmail.com',
    description='An MLOps-ready package for Cement Composite Strength Prediction using ML',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/crop_recommendation',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib',
        'fastapi',
        'uvicorn',
        'pyyaml',
        'matplotlib',
        'seaborn',
        'pytest',
        'gunicorn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
