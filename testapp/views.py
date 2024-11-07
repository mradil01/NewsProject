from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def family_view(request):
    head_msg='Srk Family Information'
    sub_msg1= ' Srk Father Name Meer Mohammad Khan'
    sub_msg2= 'Srk Mother Name Meer Lateef Fatima Khan'
    sub_msg3= 'Srk Wife Name is Gauri Khan'
    sub_msg4= ' Srk First Son Name is Aaryan Khan'
    sub_msg5= ' Srk Second Son Name is Abram Khan'
    sub_msg6= ' Srk Doughter Name is Suhana Khan'
    type = 'family'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'sub_msg6': sub_msg6,'type':type}
    return render(request,'testapp/news.html',my_dict)

def oldentime_view(request):
    head_msg='Srk All time Block Buster Movies'
    sub_msg1= 'Srk First Hit Movie is Deewana'
    sub_msg2= 'Srk First Movie in Lead Role is Baazigar'
    sub_msg3= 'Srk Second Most Popular Movie is DDLJ'
    sub_msg4= 'Srk Movies Most Directed By Yash raaj Films'
    sub_msg5= 'Srk Most Popular Movie is Devdas and So on..'
    sub_msg6= ' Srk 2nd Popular movie is Also MY Name Is Khan'
    type = 'oldentime'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'sub_msg6':sub_msg6,'type':type}
    return render(request,'testapp/news.html',my_dict)

def leatestmovie_view(request):
    head_msg='Srk All time Block Buster Movies Now a Days'
    sub_msg1= 'Srk leatest Hit Movie is Pathaan'
    sub_msg2= 'Srk Secon leatest Hit Movies is Jawan'
    sub_msg3= 'Srk All Time Block Buster Movie Also Brahmastr'
    sub_msg4= 'Srk Movies Most Romance and emptions and Thrill'
    sub_msg5= ' Srk Movie Don And Don 2 is Also Very Fameous'
    sub_msg6= ' Srk Got Named Badshah From his Badshah Movie'
    type = 'leatestmovie'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'sub_msg6':sub_msg6,'type':type}
    return render(request,'testapp/news.html',my_dict)

def hisawards_view(request):
    head_msg='Srk is The Only One Actor India who Has Won More Then 300 Awards '
    sub_msg1= 'Srk Has Won Padma Shree Award'
    sub_msg2= 'Srk Has Won FilmFare Awards he Bset Villion'
    sub_msg3= 'Srk Has Won FilmFare Awards he Bset Male Debut'
    sub_msg4= 'Srk Has Won IIFA Awards for Best Actor'
    sub_msg5= ' Srk Second Son Name is Abram Khan'
    sub_msg6= ' Srk Doughter Name is Suhana Khan'
    type = 'hisawards'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5,'sub_msg6':sub_msg6,'type':type}
    return render(request,'testapp/news.html',my_dict)
