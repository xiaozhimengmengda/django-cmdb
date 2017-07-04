from django import forms


class AssetForm(forms.Form):
    #username, mac, os_system 是前端form表单中的的输入框

    username = forms.CharField(label="用户名", error_messages={'required':'用户名不能为空'})
    mac = forms.CharField(label="mac", error_messages={'required':'mac地址不能为空'})
    os_system = forms.CharField(label="系统版本", error_messages={'required':'系统版本不能为空'})
   
    #对username的长度进行验证
    def clean_username(self):
       username = self.cleaned_data.get('username')
       if len(username) < 2:
          raise forms.ValidationError("用户名不符合规范")
       return username
   
    #对mac的长度进行验证
    def clean_mac(self):
       mac = self.cleaned_data.get('mac')
       if len(mac) != 17:
          raise forms.ValidationError("mac不符合规范")
       return mac

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={'required':'用户名不能为空'})
    password = forms.CharField(label="密码", widget=forms.PasswordInput, error_messages={'required':'密码不能为空'})

