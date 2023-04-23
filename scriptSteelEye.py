import xmltodict, csv

with open("DLTINS_20210117_01of01.xml") as xmlfile:
    xml = xmltodict.parse(xmlfile.read())

csvfile = open("records.csv", "w", encoding="utf-8")
csvfile_writer = csv.writer(csvfile)

csvfile_writer.writerow(
    [
        "FinInstrmGnlAttrbts.Id",
        "FinInstrmGnlAttrbts.FullNm",
        "FinInstrmGnlAttrbts.ClssfctnTp",
        "FinInstrmGnlAttrbts.CmmdtyDerivInd",
        "FinInstrmGnlAttrbts.NtnlCcy",
        "Issr",
    ]
)

records = xml["BizData"]["Pyld"]["Document"]["FinInstrmRptgRefDataDltaRpt"]["FinInstrm"]

attrs = ["Id", "FullNm", "ClssfctnTp", "CmmdtyDerivInd", "NtnlCcy"]


for record in records:
    val = list(record.values())[0]
    csv_line = []
    for attr in attrs:
        csv_line.append(val["FinInstrmGnlAttrbts"][attr])
    csv_line.append(val["Issr"])
    csvfile_writer.writerow(csv_line)


csvfile.close()
