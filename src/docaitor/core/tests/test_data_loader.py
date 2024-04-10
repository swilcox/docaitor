from pathlib import Path
from ..data_loader import DataLoader


CURRENT_PATH = Path(__file__).parent
FIXTURES_PATH = CURRENT_PATH / "fixtures"


def test_nothing():
    assert True


def test_data_loader_toml():
    sample_resume_toml = str(FIXTURES_PATH / "sample_resume.toml")
    dl = DataLoader(sample_resume_toml)
    assert dl._file_name == sample_resume_toml
    data = dl.load()
    assert data["skills"]["programming_languages"] == ["Python", "JavaScript", "Rust"]


def test_data_loader_yaml():
    sample_resume_yaml = str(FIXTURES_PATH / "sample_resume.yaml")
    dl = DataLoader(sample_resume_yaml, "yaml")
    assert dl._file_name == sample_resume_yaml
    data = dl.load()
    assert data["skills"]["programming_languages"] == ["Python", "JavaScript", "Rust"]
