from setuptools import setup, find_packages

setup(
    name='google-maps-scraper',
    version='0.1.0',
    author='Mukhtar ul Islam',
    author_email='Mukhtarulislam88@hotmail.com',
    description='A fast business scraper for Google Maps using Selenium',
    url='https://github.com/mukhtar-ul-islam88/google_map_scraper',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'selenium-wire',
        'webdriver-manager',
    ],

    
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
        
    ],
    python_requires='>=3.6',
)
