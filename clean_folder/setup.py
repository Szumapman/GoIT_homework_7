from setuptools import setup, find_namespace_packages

setup(name="clean_folder",
      version="1.0",
      description="Organizing files by categories.",
      long_description="The program organizes files in the user-specified directory and moves them to appropriate category directories.",
      url="http",
      author="Paweł Szumański",
      author_email="pawel.szumanski@tuta.io",
      packages=find_namespace_packages(),
      install_requires=["cowsay"],
      entry_points={"console_scripts":["clean-folder = clean_folder.clean:main"]},
)
