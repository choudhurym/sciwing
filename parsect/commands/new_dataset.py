import questionary
from questionary.prompts.common import Choice
from parsect.commands.validators import is_valid_python_classname
from parsect.commands.file_gen_utils import ClassificationDatasetGenerator
import parsect.constants as constants
import wasabi
from typing import Dict, Optional, Any, List


PATHS = constants.PATHS
TEMPLATES_DIR = PATHS["TEMPLATES_DIR"]
DATASETS_DIR = PATHS["DATASETS_DIR"]


def create_new_dataset_interactive():
    msg_printer = wasabi.Printer()

    dataset_name = questionary.text(
        "Name of Dataset? [Please provide a valid python ClassName]",
        qmark="?",
        validate=is_valid_python_classname,
    ).ask()

    dataset_type = questionary.select(
        "Chose the type of dataset you are creating?",
        choices=[
            Choice(title="Classification", value="classification"),
            Choice(title="Sequence Labeling", value="seq_labeling"),
        ],
        default="classification",
    ).ask()

    if dataset_type == "classification":
        dataset_generator = ClassificationDatasetGenerator(dataset_name=dataset_name)
        dataset_generator.generate()
