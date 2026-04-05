from pathlib import Path
import os

def create_fragment_config(path: Path):
    """Creates a .fragment config folder at path"""
    os.mkdir(path / '.fragment')
    os.mkdir(path / '.fragment' / 'library')
    with open(path / '.fragment' / 'library' / 'recent_projects.json', 'w') as file:
        file.write('[]')
