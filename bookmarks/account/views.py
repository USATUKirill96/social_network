from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

#
# def user_login(request):
#     # Функция authenticate проверяет идентификационные данные и возвращает объект User, если они корректны.
#     # Функция login сохраняет текущего пользователя в сессии.
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#         else:
#             user = None
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Успешная авторизация')
#             else:
#                 return HttpResponse('Пользователь заблокирован')
#         else:
#             return HttpResponse('Неправильный логин')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
