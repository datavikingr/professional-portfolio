# My Portfolio
This is my professional portfolio for data analysis/engineering and software development. The tools found in Tek directory are for the metrology wing of Tektronix. These are non-live iterations of the tools & they contain absolutely no confidential information or any access to internal tools. 

## Definition & Acronyms:
 - Metrology: the science and study of measurement; as opposed to meteorology, of which I am a hobbyist.
 - SC: "Standards Compliance"; is the asset in cal or not? If not, is it less than 30 days overdue?
 - IC: "Intermediate Checks"; a 17025-required spot check, half way through the assets' cal cycle.
 - OOTs: "Out of Tolerance"; Tek-owned standards that did not pass calibration require analysis for potential customer impact (see Impact Analysis Template.xlsm)
 - 17025: Like ISO:9001, it's another standard by which calibrations are held to and audited. Latest edition is 17025:2017.

## Tek/CalWebScrape.py
This is a professional datascraper to work around the lack of API endpoints for a critical dataset, and the Angular framework chosen doesn't play nice with Selenium (even XPath). Instead it uses a hybrid approach, with Computer Vision and Selenium in tandem to operate the front end of internal tool. It writes logs for unsupervised runs and sources its error-handling from corelib.py

## Tek/corelib.py
Computer vision error handling for CalWebScrape.py. Uses recursion to double check the UI hasn't moved significantly from draw to when it needs to click the element. 

## Tek/Standards Compliance KPIs.pbix
SC Dashboard pulling directly from an internal MS Dynamics tool for our calibration management software. More of these will follow as I build the 2024 version of reporting stack for the other KPIs I monitor.

## Tek/Analysis Tools/Impact Analysis Template.xlsm
Authored and maintained the North American standard tool for OOT Impact Analysis at Tek. VBA- and Formula-powered sheet analyzes potential customer impact of OOT standards, for the purpose of warranty recall recalibration. Written in 2018 and solely maintained since. Current Revision inside the document.

## Tek/Analysis Tools/TORQUE Impact Analysis Template.xlsm
Same as the above, but with additional cross-reference tooling to semi-automate the OOT analysis process for the highest volume domain in metrology. 

## Personal/hugin.py
A script to build a programmatic newspaper from RSS and send it to your kindle.

## Personal/oldnorsetoYFrunesconverter.py
This is a tool for converting ancient texts (the eddas, the sagas, et al) into their period-appropriate runic script (younger futhark) by cross-referencing available inscription databases.

## Personal/English-ASFtransliteration.py
Simple letter swapper using json.

## Personal/updaterunicspelling.py
This tool helps me update the runic spelling of every single text in the repository-directory, as I discover better spelling for specific Old Norse words. I'm working with a dead language, and routinely check academic sources for newer, better spellings. I don't want to update each file by hand, so instead I update them all at once.

## Personal/gsw.sh
A polling git helper for bash. I use it at work regularly and at home, to manage various repos as I build them out.
