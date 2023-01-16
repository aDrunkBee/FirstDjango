from django.shortcuts import render
from django.http import HttpResponse
user_info = {
    "name":"Максим",
    "surname":"Терентьев",
    "phone":"+7(123)456-78-90",
    "email":"somemail@somedomain.ru"
}

# Create your views here.
def home (request):
    res = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Терентьев М.В.</i>"""
    return HttpResponse(res)

def about(request):
    res = f"""
    Имя: <b>{user_info.get("name")}</b><br>
    Фамилия: <b>{user_info.get("surname")}</b><br>
    телефон: <b>{user_info.get("phone")}</b><br>
    email: <b>{user_info.get("email")}</b>"""
    return HttpResponse(res)