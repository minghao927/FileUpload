from django.shortcuts import render,render_to_response
from django import forms
#重点要导入,使用 Django 的 表单 
from django.http import HttpResponse
from app.models import User

# Create your views here.
# 用Form创建一个简单的表单
class UserForm(forms.Form):
    username = forms.CharField()
    #字符串
    headImg = forms.FileField()
    #文件

#函数register里面的形参request是必须要填的
#render()和render_to_response()均是django中用来显示模板页面的

'''
register函数判断用户的是否为POST请求，如果是并验证是有效的，然后就返回upload ok!，在验证正确和返回OK的中间放我们的上传文件代码，因为只有文件上传成功能返回OK，我们一会说，如果是GET请求，就直接显示一个空表单，让用户输入。
'''
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES) #还没有查到是什么意思
        #判断是否为有效的
        if uf.is_valid():
            #获取表单元素
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            # 写入数据库
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload success!')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})
