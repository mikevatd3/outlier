from pathlib import Path
import json
import logging
import logging.config

import tomli


with open("config.toml", "rb") as f:
    main_config = tomli.load(f)


logger = logging.getLogger(main_config["app"]["name"])


def setup_logging():
    with open(Path.cwd() / "logging_config.json") as f:
        logging_config = json.load(f)

    logging.config.dictConfig(logging_config)
