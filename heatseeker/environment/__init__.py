from pathlib import Path

# directories
PROJECT_ROOT = Path.cwd() / '.heatseeker'

# files
PROJECT_CONFIG = PROJECT_ROOT / 'heatseeker.yml'

# templating
TEMPLATE_ROOT = Path(__file__).parent.parent / 'templates'
CONFIG_TEMPLATE = TEMPLATE_ROOT / 'template.heatseeker.yml'
