from pathlib import Path

def create_chrysolite_project(path: Path, name: str):
    """Creates a blank chrysolite project at a given path."""
    (path / name).mkdir()
    (path / name / '.chrysolite').mkdir()
    (path / name / 'resources').mkdir()
    with open(path / name / 'project.chrysolite', 'w') as f:
        f.write('')
