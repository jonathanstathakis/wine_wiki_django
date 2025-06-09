from wine_wiki.models import Wine
import os


def run():
    wine = Wine(
        wine_name="test",
        vintage="1991",
        region="South Australia",
        subregion="Clare Valley",
        description="a wine.",
        producer="jim barry",
    )
    wine.save()
