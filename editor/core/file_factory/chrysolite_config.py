from pathlib import Path

def create_chrysolite_config(path: Path):
    """Creates a .chrysolite config folder at path"""
    (path / '.chrysolite').mkdir()
    (path / '.chrysolite' / 'library').mkdir()
    with open(path / '.chrysolite' / 'library' / 'recent_projects.json', 'w') as file:
        file.write('[]')
