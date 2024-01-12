from template import Template

# TODO implement a way to use a txt file to compile rma table
# -----------------------------------------------------------
colorRGB = {
    "r": 93,
    "g": 129,
    "b": 1,
}
# create docx file
document = Template(297, 210, 10, 8)
# document.addImg("A.jpg", size=2, align="RIGHT")

document.run(
    text="NSC Maintenance Fault Logging Template",
    r=colorRGB["r"],
    g=colorRGB["g"],
    b=colorRGB["b"],
    size=26,
    font="Arial",
)

document.run(
    text="Customer Information",
    r=colorRGB["r"],
    g=colorRGB["g"],
    b=colorRGB["b"],
    size=18,
    font="Arial",
)
tb_1 = document.init_table(rw=1, cl=2, titles=["REQUESTED INFO", "DETAILS"], size=16)
tableRecords1 = (
    ("Customer Name", "Fastweb"),
    ("End Customer Name", "Fastweb VTS"),
    ("Customer internal reference number:", 0),
    ("Primary technical contact details:\nEngineer name, phone number, email", 0),
    ("Severity /Priority Level: P1 / P2 / P3", 0),
)
document.table_content(table=tb_1, records=tableRecords1, size=12)


document.run(
    text="Support Information",
    r=colorRGB["r"],
    g=colorRGB["g"],
    b=colorRGB["b"],
    size=18,
    font="Arial",
)
tb_2 = document.init_table(rw=1, cl=2, titles=["REQUESTED INFO", "DETAILS"], size=16)


tableRecords2 = (
    ("Device serial number", 0),
    ("Chassis Serial Number: ", 0),
    ("Site name and address", 0),
    ("Site contact details:\n (Customer - name, phone number, email)", 0),
    (
        """Site access:
    \n(Opening hours, please indicate onsite resource
     availability if parts are delivered
     outside of site operating hours)""",
        0,
    ),
    (
        """Additional Information:
    Including any special instructions for the
    on-site engineer when they arrive""",
        0,
    ),
)


document.table_content(table=tb_2, records=tableRecords2, size=12)

document.nextPage()

document.run(
    text="INV description",
    r=colorRGB["r"],
    g=colorRGB["g"],
    b=colorRGB["b"],
    size=18,
    font="Arial",
)


document.run(
    text=input("INV description "),
    r=colorRGB["r"],
    g=colorRGB["g"],
    b=colorRGB["b"],
    size=14,
    font="Arial",
)


# save the document
document.save()
