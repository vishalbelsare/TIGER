import os
import subprocess
from setuptools import find_packages, setup

# run "git tag <version>" and then "git push origin master <version> when releasing a package to PyPi
version = "0.2.5"

subprocess.run(['pip', 'install', 'install', 'Cython', 'datashader', 'scikit-image', 'tqdm', 'stopit', 'matplotlib',
                'networkx', 'pillow', 'fa2', 'ffmpeg-python', 'pytest'])

keywords = ["data-science",
            "machine-learning",
            "networkx",
            "graph",
            "data-mining",
            "attack",
            "simulation",
            "vulnerability",
            "networks",
            "epidemics",
            "defense",
            "graph-mining",
            "diffusion",
            "robustness",
            "graph-attack",
            "adversarial-attacks",
            "network-attack",
            "cascading-failures",
            "netshield"]

cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="graph-tiger",
    packages=find_packages(),
    version=version,
    license="MIT",
    description="A general purpose library for graph vulnerability and robustness analysis.",
    author="Scott Freitas",
    author_email="safreita1@gmail.com",
    url="https://github.com/safreita1/TIGER",
    download_url="https://github.com/safreita1/TIGER/archive/{}.tar.gz".format(version),
    keywords=keywords,
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3.8"],
)
