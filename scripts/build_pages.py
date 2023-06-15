from pathlib import Path
import subprocess
import yaml
from markdown_toolkit import MarkdownDocument, link
from typing import Union
from textwrap import dedent

import unicodedata
import re


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


ENTITIES_ROOT_DIR = Path(Path(__file__) / "../../docs/entities").resolve()
ACCOUNT_LIST_PATH = Path(Path(__file__) / "../../accounts.yaml").resolve()

CURRENT_ENTITY_LIST = ENTITIES_ROOT_DIR.glob("*.md")

# Wipe existing list before
for entity in CURRENT_ENTITY_LIST:
    if entity.is_file():
        entity.unlink()

with open(ACCOUNT_LIST_PATH, "r", encoding="UTF-8") as account_file:
    entity_list = yaml.safe_load(account_file)


def render_sources(document: MarkdownDocument, entity: dict):
    if "sources" in entity:
        with document.heading("Sources"):
            for source in entity["sources"]:
                document.list(link(uri=source))
        document.linebreak()


def render_accounts(document: MarkdownDocument, entity: dict):
    with document.heading("Known Accounts"):
        for account_id in entity["accounts"]:
            document.list(account_id)


def build_page(entity: dict, base_dir: Path):
    account_page = MarkdownDocument()
    account_page.add(
        dedent(
        """\
        ---
        hide:
        - toc
        ---
        """)
    )
    with account_page.heading(entity["name"]):
        render_sources(account_page, entity)
        render_accounts(account_page, entity)

    output_file_path = ENTITIES_ROOT_DIR / Path(slugify(entity["name"])).with_suffix(
        ".md"
    )
    with open(output_file_path, "w", encoding="utf-8") as page:
        page.write(account_page.render())


for entity in entity_list:
    build_page(entity, ENTITIES_ROOT_DIR)
