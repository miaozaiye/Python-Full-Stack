
from django.shortcuts import render,redirect,HttpResponse,Http404
from firstapp.models import People,Article,Topics,Tag,Comment,Ticket,Ilike,User,UserProfile
from django.template import Context,Template
from django import forms
from firstapp.form import CommentForm
from firstapp.aheadline import trans_headline
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login
from firstapp.form import LoginForm,personalform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist,FieldDoesNotExist

# Create your views here.


def index(request):

    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    queryset = request.GET.get('tag')
    print(queryset)
    orderset = request.GET.get('order')
    print(orderset)
    dateset = request.GET.get('pubdate')

    if queryset:
        article_list = Article.objects.filter(tag=queryset)
    else:
        article_list = Article.objects.all()

    if orderset:
        article_list = Article.objects.order_by('-watchnumber')
    else:
        pass

    if dateset:
        article_list = Article.objects.order_by('-pub_date')
    else:
        pass


    for article in article_list: #将文件名中的空格替换为-, 并储存在 headline_2 字段
        if article.headline_2:
            pass
        else:
            article.headline_2 = article.headline.replace(' ','-')
            # print ('headline_2 is: ',article.headline_2)
            article.save()

    # for article in article_list:
    #     print (article.headline, ' transfer to' ,article.headline_2)

    context = {}

    topic_list = Topics.objects.all()
    tag_list = Tag.objects.all()

    context['article_list'] = article_list
    context['topic_list']= topic_list
    context['tag_list']= tag_list

    index_page = render(request,'huoyan_homepage.html',context)
    return index_page


def detail(request,head_line,error_form = None):
    print('get head_line:', head_line)
    context = {}
    form = CommentForm
    article = Article.objects.get(headline_2 = head_line)
    print ('article is:',article.content)
    print ('comment is:',article.under_comments)
    tags = article.tag.all
    print('tags are:',tags)
    voter_id = request.user.profile.id
    user_ticket_for_this_article = []
    user_ilike_for_this_article = []
    best_comment = []
    print ('voter_id is:',voter_id)



    try:
        print ('this is detail try')
        user_ilike_for_this_article = Ilike.objects.get(voter_id=voter_id,article=article)
        print('Ilike is:',user_ilike_for_this_article)
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id,article=article)
        user_ticket_for_this_article.save()
        user_ilike_for_this_article.save()
    except :
        print ('iLike does not exist, this is detail except')
        new_ticket = Ticket(voter_id = voter_id,article = article,choice = request.POST.get('vote','None'))
        new_ilike = Ilike(voter_id = voter_id,article = article,choice = request.POST.get('vote','None'))
        if new_ticket.choice == 'None':
            pass
        else:
            new_ticket.save()
        if new_ilike.choice == 'None':
            print ('new_ilike is None')
            pass
        else:
            print ('new _ilike is saved')
            new_ilike.save()

    try:
        best_comment = Comment.objects.filter(is_best = 'True',belong_to=article)
    except:
        None


    ilike_for_this_article = Ilike.objects.filter(article = article).filter(choice = 'like')
    print ('ilike_for_this_article:',ilike_for_this_article)
    print('Ilike for this article is:',len(ilike_for_this_article))
    context['article']= article
    context['user_ticket']=user_ticket_for_this_article
    context['user_ilike']=user_ilike_for_this_article
    context['ilike_count']=len(ilike_for_this_article)
    print ('user_ilike is',user_ilike_for_this_article)
    if best_comment:
        context['best_comment']=best_comment[0]
    if error_form is not None:
        context['form']= error_form
    else:
        context['form'] = form

    return render(request,'huoyan_article.html',context)

def detail_comment(request,head_line):
    print ('type is post')
    form = CommentForm(request.POST)
    print(form)
    # 把通过验证的信息储存为Comment 实例
    if form.is_valid():

        speaker = request.user.profile
        print('speaker is:',speaker.belong_to)
        comment = form.cleaned_data['comment']
        article = Article.objects.get(headline_2 = head_line)
        # article = Article.objects.get(headline = head_line)
        c = Comment(speaker= speaker, comment = comment,belong_to=article)
        c.save()
        print ('c is :',c)
    else:
        return detail(request,head_line,error_form = form)
    return redirect(to='detail',head_line= head_line)


def detail_vote(request,head_line):
    voter_id = request.user.profile.id
    article = Article.objects.get(headline_2 = head_line)
    print ('request is:',request)


    try:
        user_ticket_for_this_article = Ticket.objects.get(voter_id = voter_id,article = article)
        user_ticket_for_this_article.choice = request.POST.get['vote']
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:

        new_ticket = Ticket(voter_id = voter_id,article = article, choice = request.POST.get['vote'])
        new_ticket.save()

    return redirect(to = 'detail',head_line = head_line)

def detail_ilike(request,head_line):
    voter_id = request.user.profile.id
    article = Article.objects.get(headline_2 = head_line)
    print('this is detail_ilike')

    try:
        print('detail_ilike try')
        user_ilike_for_this_article = Ilike.objects.get(voter_id = voter_id,article = article)
        user_ilike_for_this_article.choice = request.POST['likevote']
        user_ilike_for_this_article.save()
    except Ilike.DoesNotExist:
        print('detail_ilike except')
        new_ilike = Ilike(voter_id = voter_id,article = article,choice = request.POST['likevote'])
        print ('new_ilike is:', new_ilike)
        new_ilike.save()

    return redirect(to = 'detail',head_line = head_line)


def form(request):

    form_page = render(request,'form.html')
    return form_page

def listing(request,tag=None):

    context = {}
    if tag is None:
        article_list = Article.objects.all()
        user_ticket = Ticket.objects.all()
    else :
        article_list = Article.objects.filter(tag = tag)


    page_robot = Paginator(article_list,5)
    page_num = request.GET.get('page')
    try:
         article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
        # raise Http404('EmptyPage!')
    except PageNotAnInteger:
        article_list = page_robot.page(1)



    context['page_robot']=page_robot
    context['article_list']= article_list

    return render (request,'listing.html',context)

def listingTag(request,tag):
    print ('tag is:',tag)
    context = {}
    if tag is None:
        article_list = Article.objects.all()
        user_ticket = Ticket.objects.all()
    else :
        article_list = Article.objects.filter(tag__name = tag)


    page_robot = Paginator(article_list,5)
    page_num = request.GET.get('page')
    try:
         article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
        # raise Http404('EmptyPage!')
    except PageNotAnInteger:
        article_list = page_robot.page(1)



    context['page_robot']=page_robot
    context['article_list']= article_list

    return render (request,'listing.html',context)

# 登录表单
def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            login(request,form.get_user())
            return redirect(to='listing')

        else:
            return HttpResponse('<h1>NOT A USER!</h1>')

    context['form']=form
    return render(request,'login_register.html',context)

# 注册表单

def index_register(request):
    print ('this is register')
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        print ('test if form is valid...',form.is_valid())
        print(form)
        if form.is_valid():
            print(' form is valid')
            form.save()
            return redirect(to='login')
        else:
            print('form is not valid...')

    context['form']=form

    return render(request,'register.html',context)

def personal_page(request):
    user = request.user
    context = {}
    print ('profile is:',request.user.profile.id)
    context['user'] = user

    return render(request,'personal_page.html',context)

def renew(request):
    #先整理装载好提交的内容
    # 判断如果上传的文件中有文件，则赋值给image
    if 'file' in request.FILES:
        new_image = request.FILES['file']
    else:
        new_image = None


    form1 = personalform(request.POST) #将表单提交的字符等内容储存到form1
    new_username = form1['username'].value() #取得提交更改的 username
    new_userpassword = form1['password'].value() #取得提交更改的 password 内容
    user = request.user
    userprofile = request.user.profile

    user1 = User.objects.get(username = request.user) #获得目前登录的User对象
    userprofile1 = UserProfile(belong_to = request.user) #获得该用户的User profile 对象

    #将提交的信息更新到user, 以及 user profile 中。
    user1.username = new_username
    user1.password = new_userpassword
    userprofile1.belong_to = user1
    userprofile1.profile_image = new_image

    print('userprofile1.belong_to is:',userprofile1.belong_to)

    user1.save()
    userprofile1.save()

    context = {}

    context['user'] = user1
    context['userprofile']=userprofile1
    # context['userprofile'] = userprofile
    return render(request,'personal_page.html',context)