# frontend-datascrape
A data-scrape tool written in Python to help me gather 40+ separate datasets for daily KPI reporting. This is one of four categories I track; and three of them (this one included) are glued together via Excel (VBA, M/PowerQuery, formulas) and then visualized via PowerBI.

The first iteration of this was the OCR-scrape.py. Took me a few years to get the time to, but I finally re-wrote the thing into autoselenium-scrape.py, using that nifty try/except clause I wrote a gist about, and the stability improvements are everything I hoped they would be. And it's 200-300% faster than the OCR version.

If you need a snippet outta here, go nuts.

## Road map:
 - openpyxl/pandas roll-up and THEN inject into the processing stack, ETC: 2023.
 - test the efficacy of skipping Excel and handling that processing in PowerBI via its Python stuff
