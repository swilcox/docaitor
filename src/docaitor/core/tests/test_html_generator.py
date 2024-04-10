from pathlib import Path
from io import StringIO
from ..html_generator import HTMLGenerator


CURRENT_PATH = Path(__file__).parent


def test_html_generator():
    # set data / context
    # set template directory
    # generate
    context = {
        "skills": {
            "programming_languages": [
                "Python",
                "JavaScript",
                "Rust",
            ],
        },
        "overview": "A Test Overview",
    }
    expected_output = """
<h2>programming_languages</h2>

<li>Python</li>

<li>JavaScript</li>

<li>Rust</li>

"""
    f = StringIO("")
    hg = HTMLGenerator(
        context, "simple_template.html", CURRENT_PATH / "fixtures" / "templates", f
    )
    hg.generate()
    f.seek(0)
    assert f.read() == expected_output
