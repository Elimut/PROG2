#-------------------------------------------------------------------------------
# Name:        Skript
# Author:      efox 2015
# Created:     25.05.2015
#-------------------------------------------------------------------------------
import arcpy

from arcpy import env
arcpy.env.overwriteOutput = True
##env.workspace="D:\\users\\RailrZK.gdb"


try:
    databaza=arcpy.GetParameterAsText(0)
    base_features = arcpy.GetParameterAsText(1)
    test_features = arcpy.GetParameterAsText(2)
    sort_field = arcpy.GetParameterAsText(3)
    output_file = arcpy.GetParameterAsText(4)
    compare_type = "GEOMETRY_ONLY"

    arcpy.env.workspace = databaza

    compare_file = "D:\\users\\compare.txt"

    compare_result = arcpy.FeatureCompare_management(base_features, test_features, sort_field, compare_type,"#", "#", "#", "#", "#", "#", "#", output_file)

    print compare_result

##    print arcpy.GetMessages()

except:
    arcpy.AddMessage("Skript je vytvoreny")
    arcpy.AddWarning("Niekde nastala chyba")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Name:         Zkou?ka 2. 6.
# Purpose:
#
# Author:      EFOX 2015
#
# Created:     12.06.2015
# Copyright:   (c) student 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
try:
    import arcpy
    from arcpy import env                                                           #naimportovani knihoven arcpy a env

    arcpy.env.overwriteOutput = True                                                #nastaven? p?episov?n? v?sledk?

    #arcpy.env.workspace ="D:\\users\\vymetalikova\\prog2\\zkouska\\Emer"           #nastaven? adres??e, env n?m zajist?, ?e se v?sledn? rastry budou ukl?dat do stejn? datab?ze, ze kter? poch?z? rastry vstupn?
    arcpy.env.workspace = arcpy.GetParameterAsText(0)                               #nastaven? adres??e jako voliteln? parametr


    rList = arcpy.ListRasters()                                                     #p?e?ten? rastrov?ch dat
    #print rList                                                                    #tisk rastrov?ch vrstev, jen pto ov??en?

    for rLi in rList:                                                               #pro jednotliv? rastrov? vrsty prove?

        in_raster = rLi                                                             #zaveden? prom?nn? pro vstupn? parametr
        out_raster = rLi + "_r"                                                     #zaveden? prom?nn? pro n?zev v?stupn?ho parametru
        #cell_size = 50  #velikost bu?ky                                            #zaveden? prom?nn? pro velikost bu?ky
        cell_size = arcpy.GetParameterAsText(1)                                     #nastaven? velikost bu?ky jako voliteln? parametr

        print ("parametry nastaveny" +  out_raster)                               #ov??en?, zda byly prom?nn? nastaveny

        arcpy.AddMessage("Parametry nastaveny " + out_raster)


    #Resample_management (in_raster, out_raster, {cell_size}, {resampling_type})
        arcpy.Resample_management (in_raster, out_raster,cell_size)                 #proveden? samotn? operace
        print ("prevzorkovani probehlo pro vrstvu" +out_raster)                    #ov???n? zda prob?hla operace pro jednotliv? vrstvy

        arcpy.AddMessage("Rastry prevzorkovany " + out_raster)

    arcpy.AddWarning("------")
except:
    arcpy.AddError("Doslo k chybe")



#-------------------------------------------------------------------------------
#------CREATE RANDOM POINTS-------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import arcpy

try:
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace=arcpy.GetParameterAsText(0)
    if arcpy.Exists (arcpy.env.workspace):
            print("Databaze prvku existuje")
            arcpy.AddMessage("Databaze prvku existuje")
            #prikaz pro seznam feature class
            fcs = arcpy.ListFeatureClasses()
            for fc in fcs:
                #vypis prochazeni listu
                arcpy.AddMessage(fc)
                desc=arcpy.Describe(fc)
                if(desc.shapeType=="Polyline"):
                    arcpy.CreateRandomPoints_management(arcpy.GetParameterAsText(0),fc+"_RANDOM_POINTS_",fc,"",25)
                else:
                    arcpy.Addmessage("Neni linii")
            else:
                arcpy.Addmessage("Zadne vrstvy")
            arcpy.AddMessage("Vse probehlo uspesne")


    else:
        print("Databaze prvku neexistuje")
        arcpy.AddMessage("Databaze prvku neexistuje")
except:
    arcpy.AddMessage("Nekde se to pokazilo")
    arcpy.AddWarning("Nekde se to pokazilo")

#-------------------------------------------------------------------------------
#------CREATE RANDOM POINTS-------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#---------------------------------------------------------
import arcpy

try:
    arcpy.env.workspace=arcpy.GetParameterAsText(0)
    if arcpy.Exists (arcpy.env.workspace):
            print("Databaze prvku existuje")
            arcpy.AddMessage("Databaze prvku existuje")
            #prikaz pro seznam feature class
            fcs = arcpy.ListFeatureClasses()
            for fc in fcs:
                #vypis prochazeni listu
                arcpy.AddMessage(fc)
                desc=arcpy.Describe(fc)
                if(desc.shapeType=="Polyline"):
                    arcpy.CreateRandomPoints_management(arcpy.GetParameterAsText(0),fc+"_RANDOM_POINTS_",fc,"",25)
            else:
                arcpy.Addmessage("Zadne vrstvy")
            arcpy.AddMessage("Vse probehlo uspesne")


    else:
        print("Databaze prvku neexistuje")
        arcpy.AddMessage("Databaze prvku neexistuje")
except:
    arcpy.AddMessage("Nekde se to pokazilo")
    arcpy.AddWarning("Nekde se to pokazilo")

#-------------------------------------------------------------------------------
#------zkouska prvni termin-------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#---------------------------------------------------------
#promene pro SVN server
__author__ = 'Hittl Roman'
__editor__ = "PyCharm Community Edition 3.4.1"

#import knihovny pro praci z geodaty od arcgis
import arcpy

try:
    #cteni parametru arcgisu
    db = arcpy.GetParameterAsText(0)
    base_feature = arcpy.GetParameterAsText(1)
    sort_field = arcpy.GetParameterAsText(2)
    output_text_file = arcpy.GetParameterAsText(3)
    #porovnavaci typ
    compare_type = "GEOMETRY_ONLY"
    #set workspace
    arcpy.env.workspace = db
    #pole feature classes
    fcList = arcpy.ListFeatureClasses()
    #cyklus prochazejici jednotlive feature class
    for fc in fcList:
        # Process: FeatureCompare
        try:
            #porovnani
            compare_result = arcpy.gp.FeatureCompare_management(base_feature, fc, sort_field, compare_type, "#", "#", "#", "#", "#", "#", "#", output_text_file)
        except Exception,e:
            #pripadny error vypis
            err = "Neumim porovnat"+e.message
            arcpy.AddError(err)
        #vypis message o ulozeni
        arcpy.AddMessage("Ulozeno do "+str(compare_result))
    #vypis kdyz skonci
    arcpy.AddMessage("Vse probehlo")

except Exception, e:
    #pripadna chyba
    arcpy.AddError(e.message)


#-------------------------------------------------------------------------------
#------zkouska druhy termin-------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#---------------------------------------------------------
#promene pro SVN server
__author__ = 'Hittl Roman'
__editor__ = "PyCharm Community Edition 3.4.1"

#import knihovny pro praci z geodaty od arcgis
import arcpy

try:
    #cteni parametru arcgisu
    db = arcpy.GetParameterAsText(0)
    #velikost_bunky = "50"
    velikost_bunky = arcpy.GetParameterAsText(1)

    #nastaveni workspace
    arcpy.env.workspace = db
    #pole rastru
    fcList = arcpy.ListRasters()

    #cyklus prochazejici jednotlive rastry
    for raster in fcList:
        # Process: FeatureCompare
        try:
            #prevzorkovani
            new_raster="r_"+raster
            print(raster, new_raster)
            arcpy.Resample_management(raster, new_raster,
                          velikost_bunky)
            #vypis message o ulozeni
            arcpy.AddMessage("Novy rastr "+new_raster)
            print("Novy rastr "+new_raster)
        except Exception,e:
            #pripadny error vypis
            err = "Neumim prevzorkovat: "+e.message
            print(err)
            arcpy.AddError(err)

    #vypis kdyz skonci
    arcpy.AddMessage("Vse probehlo")

except Exception, e:
    #pripadna chyba
    arcpy.AddError(e.message)
    print(e.message)