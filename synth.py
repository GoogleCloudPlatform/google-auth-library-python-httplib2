import synthtool as s
from synthtool import gcp

common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(
    unit_cov_level=100, cov_level=100, unit_test_external_dependencies=["flask", "pytest-localserver"]
)

s.move(templated_files)

# Change coverage path
s.replace(
    "noxfile.py",
    """["']--cov=google/cloud["'],""",
    """"--cov=google_auth_httplib2",""",
)
