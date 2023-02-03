# My Professional Data Stack
This is part of my professional portfolio data engineering for the metrology wing of Tektronix (calibrations; not weather). These are non-live iterations of the tools I wrote. They contain absolutely no confidential information or any access to internal tools.

So, if you need a code snippet or two out of here for your own project, go nuts! It's MIT Licensed for a reason. If you need to build similar tools and you're having a hard time, reach out, let's compare notes!

## Definition & Acronyms:
 - Metrology: the science and study of measurement; as opposed to meteorology, of which I am a hobbyist.
 - SC: "Standards Compliance"; is the asset in cal or not? If not, is it less than 30 days overdue?
 - IC: "Intermediate Checks"; a 17025-required spot check, half way through the assets' cal cycle.
 - OOTs: "Out of Tolerance"; Tek-owned standards that did not pass calibration require analysis for potential customer impact (see Impact Analysis Template.xlsm)

## Impact Analysis Template.xlsm
Authored and maintained the North American standard tool for OOT Impact Analysis at Tek. VBA- and Formula-powered sheet analyzes potential customer impact of OOT standards, for the purpose of warranty recall recalibration. Written in 2018 and solely maintained since, up to the current Rev 21 (with 3 "PRs" from my mentor in VBA, actually. Thanks again, Mike!)

## Dashboard.pbix
Visualizations for everything related to standards compliance across three categories. Sent daily to VP, Regional Managers, Lab managers, Supervisors.

## SCOOTIC.xlsx
Middleware for the stack. Does some concatenation and analysis that can't be done in PowerBI. Contains two mini-reports for Support staff, sent weekly.

## *-scrape.py
Two data-scraper tools written in Python to help me gather 40+ separate datasets for the daily KPI reporting described above. The first iteration of this was the OCR-scrape.py. Took me a few years to get the time to, but I finally re-wrote the thing into autoselenium-scrape.py, using that nifty try/except clause I wrote a gist about, and the stability improvements are everything I hoped they would be. And it's 200-300% faster than the OCR version, as nifty as it was getting a computer to see, per se.

## Road map:
 - post-scrape openpyxl/pandas roll-up and THEN inject into the processing stack, ETC: 2023.
 - test the efficacy of skipping Excel and handling that processing in PowerBI via its Python stuff

