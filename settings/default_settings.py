import os
import json

from pathlib import Path

# ############## Common settings #############
DEFAULT_LOG_FILE = "/var/log/enterprise_cloud_admin.log"
MODULE_ROOT_DIR = Path(__file__).resolve().parent.parent
TERRAFORM_BINARY_PATH = MODULE_ROOT_DIR / "terraform"


# ############## Builder settings ##############
DEFAULT_GITHUB_API_URL = "https://api.github.com"
DEFAULT_PROJECT_NAME = "my-gcp-project"
DEFAULT_PROJECT_ID = "my-gcp-project"
DEFAULT_CODE_ORG = "my-code-org"
DEFAULT_CONFIG_ORG = "my-config-org"
PROJECT_DATA_DIR = (
    MODULE_ROOT_DIR / "resources/project_data/" / DEFAULT_PROJECT_ID
)
DEFAULT_TOKEN_FILE = MODULE_ROOT_DIR / "/resources/token.json"
DEFAULT_GIT_REF = "master"
DEFAULT_TOKEN = (
    json.load(open(DEFAULT_TOKEN_FILE))["token"]
    if os.path.exists(DEFAULT_TOKEN_FILE)
    else ""
)
SUPPORTED_CLOUDS = ["aws", "gcp", "triton"]
SUPPORTED_VCS_PLATFORMS = ["github"]
SUPPORTED_ORCHESTRATORS = ["terraform"]
VALID_PROJECT_ID_FORMAT = "^[a-z]{4}-[a-z0-9]{4,31}-(?:dev|prod|test)$"


# ############## Code control settings ##############
DEFAULT_GITHUB_API_URL = "https://api.github.com"
ADMIN_TEAM = "gcp-admin-team"
STANDARD_TEAM_ATTRIBUTES = {
    "name": DEFAULT_PROJECT_ID,
    "permission": "push",
    "description": "Standard team for " + DEFAULT_PROJECT_ID + " project",
    "privacy": "closed",
}
PRIV_TEAM_ATTRIBUTES = {
    "name": DEFAULT_PROJECT_ID + "-priv",
    "permission": "push",
    "description": "Privileged team for " + DEFAULT_PROJECT_ID + " project",
    "privacy": "secret",
}
PROJECT_DATA_DIR = (
    MODULE_ROOT_DIR / "resources/project_data/" / DEFAULT_PROJECT_ID
)
PROTECTED_BRANCH = {
    "enforce_admins": True,
    "dismiss_stale_reviews": True,
    "require_code_owner_reviews": False,
    "required_approving_review_count": 1,
}
HIGHLY_PROTECTED_BRANCH = {
    "enforce_admins": True,
    "dismiss_stale_reviews": True,
    "require_code_owner_reviews": True,
    "required_approving_review_count": 2,
}
LOCAL_FILES = {
    "readme_file": MODULE_ROOT_DIR / "resources/templates/README.md",
    "apis_file": MODULE_ROOT_DIR / "resources/templates/gcp_enabled_apis.auto.tfvars.json",
    "project_settings_file": MODULE_ROOT_DIR
    / "resources/templates/gcp_project_settings.auto.tfvars.json",
    "role_bindings_file": MODULE_ROOT_DIR
    / "resources/templates/gcp_role_bindings.auto.tfvars.json",
    "service_accounts_file": MODULE_ROOT_DIR
    / "resources/templates/gcp_service_accounts.auto.tfvars.json",
}
REMOTE_FILES = {
    "readme_file": "README.md",
    "apis_file": "gcp/gcp_enabled_apis.auto.tfvars.json",
    "project_settings_file": "gcp/gcp_project_settings.auto.tfvars.json",
    "role_bindings_file": "gcp/gcp_role_bindings.auto.tfvars.json",
    "service_accounts_file": "gcp/gcp_service_accounts.auto.tfvars.json",
}


# ############## Deployer settings ##############
WORKING_DIR_BASE = Path("/tmp")


# ############## Reporter settings ##############
DEFAULT_MONITORING_PROJECT = "gb-me-services"
