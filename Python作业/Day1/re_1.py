department1 = "Security"
department2 = "Python"
depart1_m = "cq_bomb"
depart2_m = "qinke"
COURSE_FEES_SEC = 456789.123
COURSE_FEES_Python = 123456.789
#line1 = "Department1 name:%-12sManager:%-12sCOURSE_FEES:%-12.2fTHE END!"%(department1,depart1_m,COURSE_FEES_SEC)
line1 = "Department1 name:".ljust(20) + department1.ljust(15) + "Manager:" + depart1_m.ljust(10) + "COURSE:" + str(COURSE_FEES_Python).ljust(20) + "The End!"
line2 = "Department2 name:".ljust(20) + department2.ljust(15) + "Manager:" + depart2_m.ljust(10) + "COURSE:" + str(COURSE_FEES_SEC).ljust(20) + "The End!"

length = len(line1)
print ("="*length)
print (line1)
print (line2)
print ("="*length)