wine_list_categories = [
    (0, "white wine"),
    (1, "skin contact and amphora"),
    (2, "rose wine"),
    (3, "chilled red wine"),
    (4, "red wine"),
    (5, "sweet wine"),
    (6, "fortified wine"),
    (7, "sherry"),
]
white_wine_subcategories = [
    ("white wine", 0, "champagne"),
    ("white wine", 1, "sparkling"),
    ("white wine", 2, "riesling"),
    ("white wine", 3, "semillon and blends"),
    ("white wine", 4, "pinot gris"),
    ("white wine", 5, "sauvignon blanc and blends"),
    ("white wine", 6, "pinot blanc"),
    ("white wine", 7, "chenin blanc"),
    ("white wine", 8, "fiano"),
    ("white wine", 9, "viognier"),
    ("white wine", 10, "white varietals"),
    ("white wine", 11, "chardonnay"),
]

red_wine_subcategories = [
    ("red wine", 0, "pinot noir"),
    ("red wine", 1, "nebbiolo"),
    ("red wine", 2, "sangiovese"),
    ("red wine", 3, "gamay"),
    ("red wine", 4, "red varietals"),
    ("red wine", 5, "cabernet franc"),
    ("red wine", 6, "cabernet sauvignon and blends"),
    ("red wine", 7, "merlot"),
    ("red wine", 8, "grenache and blends"),
    ("red wine", 9, "touriga nacional and blends"),
    ("red wine", 10, "shiraz and blends"),
]

sweet_wine_subcategories = [
    ("sweet wine", 0, "australia"),
    ("sweet wine", 1, "rest of world"),
]

fortified_wine_subcategories = [
    ("fortified wine", 1, "sweet fortified wine"),
]

sherry_subcategories = [("sherry", 0, "dry"), ("sherry", 1, "sweet")]

subcategories = (
    white_wine_subcategories
    + red_wine_subcategories
    + sweet_wine_subcategories
    + fortified_wine_subcategories
    + sherry_subcategories
)
