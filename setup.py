"""Setup the project for execution by using setuptools. 
Run this file using python and provide the develop argument."""
from setuptools import setup
setup(
    name="glance-a-lot",
    version="0.0.1",
    url="https://github.com/pupperemeritus/glance-a-lot",
    license="GPL-3.0",
    install_requires=["scikit-learn",
                      "datetime",
                      "requests",
                      "youtube-search-python",
                      "google-search",
                      "dotenv",
                      "pymongo",
                      "discord.py",
                      "pandas",
                      "seaborn",
                      "matplotlib",
                      "pickle",
                      "numpy",
                      "random"
                      ],
    packages=["glance-a-lot"],
    include_package_data=True,
    zip_safe=False
)