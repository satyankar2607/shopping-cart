from django.shortcuts import render

from .models import tbl_Employee
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def Import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file)
            empexceldata = pd.read_csv("." + excel_file, encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = tbl_Employee.objects.create(Empcode=dbframe.Empcode, firstName=dbframe.firstName,
                                                  middleName=dbframe.middleName,
                                                  lastName=dbframe.lastName, email=dbframe.email,
                                                  phoneNo=dbframe.phoneNo, address=dbframe.address,
                                                  exprience=dbframe.exprience, gender=dbframe.gender,
                                                  DOB=fromdate_time_obj,
                                                  qualification=dbframe.qualification)
                print(type(obj))
                obj.save()

            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:
        print(identifier)

    return render(request, 'importexcel.html', {})
