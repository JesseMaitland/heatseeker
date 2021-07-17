import shutil
from argparse import Namespace
from heatseeker.environment import PROJECT_ROOT, PROJECT_CONFIG, CONFIG_TEMPLATE


def init(cmd: Namespace) -> None:

    if cmd.destroy and PROJECT_ROOT.exists():
        shutil.rmtree(PROJECT_ROOT)

    # dirs
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    # files
    if not PROJECT_CONFIG.exists():
        PROJECT_CONFIG.touch(exist_ok=True)
        shutil.copy(CONFIG_TEMPLATE, PROJECT_CONFIG)
