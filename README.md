# README

Based on [this tutorial](https://books.agiliq.com/projects/djenofdjango/en/latest/chapter5.html).

## Development Status

As of 2025-06-09 this project has stalled due to the lack of consistency of the bepoz data. Several solutions exist, such as refactoring the Wine model to mimic the bepoz model and use 'comment' field as the wine.html header, curating a complex etl pipeline, correcting the source data, or configuring an llm model to clean/fill the data within a csv. Or manually entering the data. The point is that we need to reconcile the data on the on-site database and the webapp database. Unfortunately, personal matters demand attention, and I will shelf this project for two weeks or o, to be resumed on the 23rd if possible.

## Notes

### Wine List Structure

Rules:

- Categories appear as titles with a horizontal line
- principal varieties (Chardonnay, Pinot Noir etc.) are displayed as follows:
  - subheading country
  - Vintage \t Producer 'Name' \t Subregion Region \t Price
  - each section under the subheading is structured as a 4 column table with varying width
- Red and white varietals are formatted slightly differently:
  - Heading
  - Vintage \t Variety Producer 'Name' \t Subregion Region \t Price
- Champagne is again different:
  - subheadings is village.

As of 2025-05-29

- Wine by the Glass
- White Wine:
  - Champagne:
    - Côte des Bar (Aube)
    - Côte des Blancs
    - Côte de Sézanne
    - Montagne de Reims
    - Vallée de la Marne
  - Sparkling (Australia)
  - Riesling:
    - Australia
    - New Zealand
    - France
    - Austria
    - Germany
  - Semillon and Blends:
    - Australia
  - Pinot Gris:
    - Australia
    - France
  - Sauvignon Blanc and blends:
    - Australia
    - France
  - Pinot Blanc:
    - Australia
  - Chenin Blanc
  - Fiano
  - Viognier
  - White Varietals
  - Chardonnay
- Skin Contact and Amphora
- Rosé Wine
- Chilled Red Wine
- Red Wine:
  - Pinot Noir
  - Nebbiolo
  - Sangiovese
  - Gamay
  - Red Varietals
  - Cabernet Franc
  - Cabernet Sauvignon and blends
  - Merlot
  - Grenache and blends
  - Touriga Nacional and blends
  - Tempranillo
  - Shiraz and blends
- Sweet Wine
- Fortified Wine
  a. Dry Fortified Wine, Sweet Fortified Wine
- Sherry
  - Dry Sherry, Sweet Sherry

## Design

### User Management

See the following: <https://learndjango.com/tutorials/django-login-and-logout-tutorial> for basic setup of user accounts.
