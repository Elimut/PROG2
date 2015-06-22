#----SEARCH-CURSOR---------------------------------------------------------------------------
import arcpy as ap

# nastaveni licence
#gp.SetProduct("ArcView")

# Set the workspace.
#gp.Workspace = "E:\\Student\\PYTH\\Database\\Redlands.mdb"
ap.env.Workspace = "D:\\vyuka\\II - SKRI\\Cviceni\\Database\\Redlands.mdb"
gp.Workspace ="D:\\Vyuka\\II - SKRI\\Cviceni\\Database\\Redlands.mdb"
cur = gp.SearchCursor("Hospitals")

# Vypisuje nazvy nemocnic
print
row = cur.Next()
while row:
    #print "_______________________"
    print "Adresa je "+row.ARC_Street + " a nazev je " + row.Name + "."
    row = cur.Next()

# pruchod od prvniho zaznamu tabulky, nutny znovu Search kursor
##cur = gp.SearchCursor("Hospitals")
##row = cur.Next()
##while row:
##    print "_______________________"
##    print "Mesto je "+row.City
##    row = cur.Next()
print
print "abecedne podle nazvu nemocnice"

cur = gp.SearchCursor("Hospitals", "","","","Name")
#cur = gp.SearchCursor("Hospitals","")
row = cur.Next()
while row:

    print "nazev   " + row.Name + "."
    row = cur.Next()


#----Nahrazuje slovo INTERSTATE zkratkou INT---------------------------------------------------------------------------
# Purpose: Nahrazuje slovo INTERSTATE zkratkou INT
# Pred spustenim zalohujte data.

import arcgisscripting, string
# Create a variable to access the Geoprocessor.
gp = arcgisscripting.create(9.3)
# nastaveni licence
#gp.SetProduct("ArcView")

gp.Workspace ="D:\\Vyuka\\II - SKRI\\Cviceni\\Database\\SanDiego.mdb"

# Feature Class Freeways  with Attribute STREET_NAM
# select only row with INT* ... SQL condition

cur= gp.UpdateCursor("Freeways","[STREET_NAM] like 'INT*'")
row = cur.Next()
while row:
	row.STREET_NAM = string.replace(row. STREET_NAM, "INTERSTATE", "INT")
	cur.UpdateRow(row)
	row = cur.Next()


#----INSTERT-ROWS---------------------------------------------------------------------------
import arcpy as ap

# Create insert cursor for table
#
rows = ap.InsertCursor("D:/St_Johns/data.gdb/roads_lut")
x = 1

# Create 25 new rows. Set the initial row ID and distance values
#
while x <= 25:
    row = rows.newRow()
    row.rowid = x
    row.distance = 100
    rows.insertRow(row)
    x = x + 1


#----UPDATE HELP---------------------------------------------------------------------------
import arcpy

# Create update cursor for feature class
#
rows = arcpy.UpdateCursor("D:/St_Johns/data.gdb/roads")

for row in rows:
# Update the field used in buffer so the distance is based on the road
#   type. Road type is either 1, 2, 3, or 4. Distance is in meters.
#
    row.buffer_distance = row.road_type * 100
    rows.updateRow(row)


#----UPDATE-FIELD--------------------------------------------------------------------------
# Author: Zdena Dobesova
# Date: 2011
# Purpose: Adds a field to a feature class and updates that
#          field using the values from two other fields.

# Import the module.
import arcgisscripting

# Create a variable to access the Geoprocessor.
gp = arcgisscripting.create(10)

# Set the workspace.
gp.Workspace ="D:\\Vyuka\\II - SKRI\\Cviceni\\Database\\Redlands.mdb"

# Add a field to the Hospitals feature class.
gp.AddField_management("Hospitals", "Full_Address2", "Text")

# Place all the rows from the Hospitals feature class into
# an Update cursor.
cur = gp.UpdateCursor("Hospitals")

# Get the first row from the Hospitals feature class.
row = cur.Next()

# Loop through each row in the Hospitals feature class and update
# each row using the ARC_Street and CITY fields.
while row:
    row.Full_Address2 = row.ARC_Street + ", " + row.CITY
    cur.UpdateRow(row)
    row = cur.Next()

# Delete the cursor variable.
del cur


#----DELETE ROW HELP---------------------------------------------------------------------------
import arcpy

# Create update cursor for feature class
#
rows = arcpy.UpdateCursor("D:/St_Johns/data.gdb/roads")

for row in rows:
    # Delete all rows that have a roads type of 4
    if row.road_type == 4:
        rows.deleteRow(row)
#----SEARCH-CURSOR---------------------------------------------------------------------------
#----SEARCH-CURSOR---------------------------------------------------------------------------
#----SEARCH-CURSOR---------------------------------------------------------------------------
#----SEARCH-CURSOR---------------------------------------------------------------------------
