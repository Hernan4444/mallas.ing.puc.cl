import logging
import re
from pathlib import Path

from app.plan.validation.curriculum.tree import MajorCode

log = logging.getLogger("plan-collator")

REGEX_MAJOR_CODE = re.compile(r"\((M\d{3})\)")

# Fix para permitir majors con el formato (MXXX-TX).
# Esto es para agregar majors con átras/track pero que no tiene un código
REGEX_MAJOR_CODE = re.compile(r"\((M\d{3})(-A\d)?\)")


def scrape_majors() -> set[MajorCode]:
    log.debug("scraping majors...")

    # Load raw pre-scraped text
    raw = Path("../static-curriculum-data/major-scrape.txt").read_text()
    return {MajorCode(code[0] + code[1]) for code in REGEX_MAJOR_CODE.findall(raw)}
