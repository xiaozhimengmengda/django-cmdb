from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class NameForm(forms.Form):
    your_name = forms.CharField(label='你的名字', max_length=100)
    your_age = forms.IntegerField(label="你的年龄")

    def clean(self):
        cleaned_data = super().clean()
        your_name = self.cleaned_data.get("your_name")
        if len(your_name) < 5:
            raise forms.ValidationError("用户名必须大于5个字符")
        return cleaned_data

    # def clean_your_name(self):
    #     your_name = self.cleaned_data.get("your_name")
    #     if len(your_name) < 5:
    #         raise forms.ValidationError("用户名必须大于5个字符")
    #     return your_name

    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)


class MentForm(forms.Form):

    sn = forms.CharField(label='sn码', max_length=64, error_messages={'required': 'sn不能为空'})
    ip = forms.CharField(label='ip地址', max_length=64, required=False)
    hostname = forms.CharField(label='主机名字', max_length=64,error_messages={'required': '主机名字不能为空'})
    mac = forms.CharField(label='mac地址',  max_length=64, required=False)
    addr = forms.CharField(label='网卡地址', max_length=66, required=False)
    admin = forms.CharField(label='管理员', max_length=64, required=False)
    user = forms.CharField(label='用户名', max_length=64, required=False)
    time = forms.CharField(label="创建时间", required=False)
    mem = forms.IntegerField(label="内存",required=False)

    #对username的长度进行验证
    def clean_username(self):
        hostname = self.cleaned_data.get('hostname')
        if len(hostname) < 2:
            raise forms.ValidationError("用户名不符合规范")
        return hostname


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', error_messages={'required':'不能为空'})
    password = forms.CharField(label='密码',widget=forms.PasswordInput, error_messages={'required':'不能为空'})

    def clean(self):
        #cleaned_data = super(LoginForm, self).clean() python 2.7
        cleaned_data = super().clean()
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')

        if username == '' or password == '':
            raise forms.ValidationError("用户或密码不正确")
        else:
            # user = authenticate(username=username, password=password)
            user = None
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist as e:
                    pass
            if user and user.check_password(password):
                self.cached_user = user
            else:
                raise forms.ValidationError("用户或密码不正确")

        return cleaned_data


# class AssetForm(forms.Form):
#     #username, mac, os_system 是前端form表单中的的输入框
#
#     username = forms.CharField(label="用户名", error_messages={'required':'用户名不能为空'})
#     mac = forms.CharField(label="mac", error_messages={'required':'mac地址不能为空'})
#     os_system = forms.CharField(label="系统版本", error_messages={'required':'系统版本不能为空'})
#
#     #对username的长度进行验证
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if len(username) < 2:
#             raise forms.ValidationError("用户名不符合规范")
#         return username
#
#     #对mac的长度进行验证
#     def clean_mac(self):
#         mac = self.cleaned_data.get('mac')
#         if len(mac) < 16:
#             raise forms.ValidationError("mac不符合规范")
#         return mac
#
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     username = self.cleaned_data.get('username')
#     #     if len(username) < 2:
#     #         raise forms.ValidationError("用户名不符合规范")
#     #     mac = self.cleaned_data.get('mac')
#     #     if len(mac) < 16:
#     #         raise forms.ValidationError("mac不符合规范")
#     #     return cleaned_data