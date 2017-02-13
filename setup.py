from setuptools import setup
from setuptools.command.install import install
import os
import tarfile
import shutil
import subprocess

MITIE_FEATURE_URL = "https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2"
MITIE_FEATURE_LOCAL_PATH = "data/total_word_feature_extractor.dat"


def download_mitie_feature_files(url):
    print("Downloading MITIE model file")
    import wget
    local_filename = wget.download(url)

    tar = tarfile.open(local_filename, "r:bz2")
    tar.extractall()
    os.rename('MITIE-models/english/total_word_feature_extractor.dat', MITIE_FEATURE_LOCAL_PATH)
    shutil.rmtree('MITIE-models')
    os.remove(local_filename)


def download_spacy_language_model():
    print("Installing spacy language models")
    subprocess.check_call(["pip", 'install', 'spacy'])
    subprocess.check_call(['python', '-m', 'spacy.en.download'])


class MITIEInstallCommand(install):
    """MITIE install"""
    def run(self):
        if not os.path.exists(MITIE_FEATURE_LOCAL_PATH):
            download_mitie_feature_files(MITIE_FEATURE_URL)
        install.run(self)


class SpacyInstallCommand(install):
    "Download Spacy models"
    def run(self):
        download_spacy_language_model()
        install.run(self)


setup(
name='rasa_nlu',
    packages=[
        'rasa_nlu',
        'rasa_nlu.classifiers',
        'rasa_nlu.emulators',
        'rasa_nlu.extractors',
        'rasa_nlu.featurizers',
        'rasa_nlu.interpreters',
        'rasa_nlu.trainers',
        'rasa_nlu.tokenizers'
    ],
    cmdclass={'install': MITIEInstallCommand},
    package_dir={'rasa_nlu': 'src'},
    version='0.6-beta',
    install_requires=[],
    description="rasa NLU a natural language parser for bots",
    author='Alan Nichol',
    author_email='alan@golastmile.com',
    url="https://rasa.ai",
    keywords=["NLP", "bots"],
    download_url="https://github.com/golastmile/rasa_nlu/tarball/0.6-beta"
)
