from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import Project, Blog, Skill, SendMail,Experience,Profile
# Create your views here.
from .forms import UserSendMail
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError


def index(request):
    #template = loader.get_template("myportfolio/index.html")
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = Profile.objects.all().first()
    form = UserSendMail()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    #return HttpResponse(template.render(context, request))
    if request.method=='GET':
        return render (request,'myportfolio/index.html',context)

    if request.method == 'POST':
        # mail_form = UserSendMail(request.POST)
        if mail_form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            _from = 'rushikeshtole19@gmail.com'
            useremail = request.POST.get('useremail')
            mail_data = SendMail(subject=subject, message=message, useremail=useremail)
            mail_data.save()
            # msgm=msg.replace("<|message|>", message)
            # msgu=msgm.replace("<|NAME|>", useremail)
            # msgs=msgu.replace("|<topic|>", subject)

            send_mail(
                subject,
                message,
                _from,
                [useremail],
                fail_silently=False,
            )
            mail_form = UserSendMail(request.POST)
            return render (request,'myportfolio/index.html',context)
        
        else:
            mail_form = UserSendMail(request.POST)

            return render (request,'myportfolio/index.html', context)
    else:
        mail_form = UserSendMail(request.POST)
        return render (request,'myportfolio/index.html', context)

def experiences(request):
    return HttpResponse("you are in experience page")

def Blogs(request):
    blogs = Blog.objects.order_by('-published_on')
    return render (request, 'myportfolio/blog.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, id=id)
    return render (request, 'myportfolio/blog_details.html', {'blog':blog})    

msg = '''[<|message|>]'''

def contact_us(request):
    if request.method=='GET':
        #template = loader.get_template("myportfolio/index.html")
        projects = Project.objects.all()
        skills = Skill.objects.all()
        experiences = Experience.objects.all().order_by('-start_date')[:5]
        profile = Profile.objects.all().first()
        form = UserSendMail()
        context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
        return render (request,'myportfolio/index.html',context)
        
    if request.method == 'POST':
        mail_form = UserSendMail(request.POST)
        if mail_form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            _from = 'rushikeshtole19@gmail.com'
            useremail = request.POST.get('useremail')
            mail_data = SendMail(subject=subject, message=message, useremail=useremail)
            mail_data.save()
            # msgm=msg.replace("<|message|>", message)
            # msgu=msgm.replace("<|NAME|>", useremail)
            # msgs=msgu.replace("|<topic|>", subject)

            send_mail(
                subject,
                message,
                _from,
                [useremail],
                fail_silently=False,
            )
            mail_form = UserSendMail(request.POST)
            return render (request,'myportfolio/contact.html', {'messages':'Mail Send Successfully'})
        
        else:
            mail_form = UserSendMail(request.POST)

            return render (request,'myportfolio/contact.html', {'messages':'Mail Not Send','form':mail_form})
    else:
        mail_form = UserSendMail(request.POST)
        return render (request,'myportfolio/contact.html', {'messages':'Write','form':mail_form})