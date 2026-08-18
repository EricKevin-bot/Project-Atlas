"""
Project Atlas configuration.
"""

# ==========================================
# Application
# ==========================================

APP_NAME = "Project Atlas"
ATLAS_VERSION = "1.2.0"

# ==========================================
# Runtime
# ==========================================

DEVELOPMENT_MODE = True
DEBUG_MODE = True
LOGGING_ENABLED = True

# ==========================================
# AI Provider
# ==========================================

AI_PROVIDER = "anthropic"
CLAUDE_MODEL = "claude-sonnet-4-6"

# ==========================================
# Image Provider
# ==========================================

IMAGE_PROVIDER = "openai"
IMAGE_MODEL = "gpt-image-1-mini"
IMAGE_QUALITY = "low"
IMAGE_SIZE = "1536x1024"
IMAGE_FORMAT = "png"
IMAGE_COUNT = 1
GENERATE_THUMBNAIL_IMAGE = True

# ==========================================
# Token Limits
# ==========================================

RESEARCH_MAX_TOKENS = 1200
TITLE_MAX_TOKENS = 500
SCRIPT_MAX_TOKENS = 2500
DESCRIPTION_MAX_TOKENS = 700
TAGS_MAX_TOKENS = 300
QUALITY_MAX_TOKENS = 800

# ==========================================
# Budget Controls
# ==========================================

MAX_RETRIES = 1
RETRY_FAILED_AGENTS = True

GENERATE_MULTIPLE_TITLES = True
TITLE_CANDIDATE_LIMIT = 3

# ==========================================
# Quality Thresholds
# ==========================================

MIN_OVERALL_SCORE = 8.0
MIN_TITLE_SCORE = 8.0
MIN_SCRIPT_SCORE = 8.0
MIN_DESCRIPTION_SCORE = 7.0
MIN_TAGS_SCORE = 7.0