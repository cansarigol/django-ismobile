import nox

nox.options.stop_on_first_error = True

SOURCE_FILES = "ismobile", "tests", "noxfile.py"


@nox.session
def lint(session, reuse_venv=True):
    session.install("autoflake", "isort==5.*", "black")
    session.run("autoflake", "--in-place", "--recursive", *SOURCE_FILES)
    session.run("black", *SOURCE_FILES)
    session.run("isort", *SOURCE_FILES)


@nox.session
def check(session, reuse_venv=True):
    session.install("flake8", "isort==5.*", "black")
    session.run("flake8", *SOURCE_FILES)
    session.run("black", "--check", "--diff", *SOURCE_FILES)
    session.run("isort", "--check", "--diff", *SOURCE_FILES)


@nox.session
@nox.parametrize("django", ["2.0", "2.2", "3.0"])
def test(session, django, reuse_venv=True):
    session.install(f"django=={django}", "pytest", "pytest-django", "pytest-cov")
    session.run("pytest", "--cov-report", "term-missing", "--cov=ismobile", "tests")
