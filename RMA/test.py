from template import Template
# create docx file
document = Template(297, 210, 25.4, 12.7)
document.title("Maintenance Fault Logging Template", 0)
document.title("Customer Information ", 1)
table = document.table(rows= 1, cols= 2)
tableRecords = (
    ("REQUESTED INFORMATION","DETAILS"),
    ("Customer Name", "FASTWEB"),
    ("End Customer Name","Fastweb VTS"),
    ("Customer internal reference number:", 0),
    ("Primary technical contact details:\nEngineer name, phone number, email", 0),
    ("Severity /Priority Level: P1 / P2 / P3", 0),
    ("","")
)

# document.title("Customer Information", 0)

table = document.table(rows= 1, cols= 2)
tableRecords = (
    ("Device serial number", 0),
    ("Chassis Serial Number: ", 0),
    ("Site name and address", 0),
    ("Site contact details:\n (Customer - name, phone number, email)", 0),
    ('''Site access: 
    \n(Opening hours, please indicate onsite resource
     availability if parts are delivered 
     outside of site operating hours)''', 0),
    ('''Additional Information: 
    Including any special instructions for the 
    on-site engineer when they arrive''', 0),

)







document.table_content(table= table, records= tableRecords)


# save the document
document.save()    