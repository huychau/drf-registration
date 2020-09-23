PACKAGE_DIR := drf_registration
TEST_DIR := tests

PYLINT := pylint
PYLINT_OPTS := --rcfile=setup.cfg

TEST := tox -e test ${ARGS}
DOCS := tox -e docs

# Build Docs
DOCS_SPHINXOPTS    ?=
DOCS_SPHINXBUILD   ?= sphinx-build
DOCS_SOURCEDIR     = ./docs
DOCS_BUILDDIR      = ${DOCS_SOURCEDIR}/_build

# Serve the docs
DOCS_PORT                   := 8080
DOCS_SPHINXAUTOBUILD        := sphinx-autobuild
DOCS_SPHINXAUTOBUILD_OPTS   := --watch ${PACKAGE_DIR} --port ${DOCS_PORT}

# Build directories
BUILD_DIRS := ${DOCS_BUILDDIR} *.egg-info dist build .tox .pytest_cache htmlcov .coverage
# Docs
.PHONY: build_docs
build_docs:
	${DOCS_SPHINXBUILD} ${DOCS_SPHINXOPTS} ${DOCS_SOURCEDIR} ${DOCS_BUILDDIR}/html ${ARGS}

.PHONY: serve_docs
serve_docs:
	${DOCS_SPHINXAUTOBUILD} ${DOCS_SPHINXAUTOBUILD_OPTS} ${DOCS_SOURCEDIR} ${DOCS_BUILDDIR}/html ${ARGS}

.PHONY: docs
docs:
	${DOCS}

# Linter
.PHONY: pylint
pylint:  ## run pylint
	${PYLINT} --disable=missing-module-docstring --disable=too-few-public-methods --disable=protected-access ${PYLINT_OPTS} ${PACKAGE_DIR} ${ARGS}

# Run test
.PHONY: test
test:
	${TEST}

.PHONY: clean
clean:
	@ find . -name '*.py[co]' -delete
	@ find . -name '__pycache__' -delete
	@ rm -rf ${BUILD_DIRS}
