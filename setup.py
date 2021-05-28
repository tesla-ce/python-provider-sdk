import os
import setuptools

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md')), "r") as fh:
    long_description = fh.read()

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'requirements.txt')), "r") as fh:
    requirements_raw = fh.read()
    requirements_list = requirements_raw.split('\n')
    requirements = []
    for req in requirements_list:
        if not req.strip().startswith('#') and len(req.strip()) > 0:
            requirements.append(req)

requirements_test = requirements + ['pytest-mock', 'pytest-celery']

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "src/tesla_ce_provider/data/VERSION")), "r") as fh:
    version = fh.read()

setuptools.setup(
    name="tesla-ce-provider",
    version=version,
    author="Xavier Baro",
    author_email="xbaro@uoc.edu",
    description="TeSLA Python SDK for providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://tesla-ce.github.io",
    project_urls={
        'Documentation': 'https://tesla-ce.github.io/python-provider-sdk/',
        'Source': 'https://github.com/tesla-ce/python-provider-sdk',
    },
    packages=setuptools.find_packages('src', exclude='__pycache__'),
    package_dir={'': 'src'},  # tell distutils packages are under src
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Framework :: Pytest"
    ],
    python_requires='>=3.6',
    package_data={
        '': ['*.cfg', 'VERSION'],
        'tesla_ce_provider': [
            'data/*',
                    ],
    },
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements_test,
    entry_points={"pytest11": ["tesla_ce_provider_fixtures=tesla_ce_provider_fixtures.fixtures"]}
)
