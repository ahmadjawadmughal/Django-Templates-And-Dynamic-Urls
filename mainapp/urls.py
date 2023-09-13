from django.urls import path
#from .views import main,get_name,get_song,login,success,files,submission,html,template_view,pass_dict
from mainapp.views import *

urlpatterns = [

    path("mysite/production/mainapp/main/", main, name= "main"),
    path("name/<name>/<int:age>/", get_name, name = "get_name"),
    path("songs/<str:song_name>/<str:singer_name>/", get_song, name= "get_song"),
    path("login/<str:username>/<password>/", login, name="login"),
    path("success/<str:username>/<password>/", success, name="success"),
    path("files/<str:username>/<password>/",files, name= "files"),
    path("submission/<str:username>/<password>/", submission, name="submission"),
    path("portfolio/", html, name="html"),
    path("template_view/", template_view, name="template_view"),
    path("pass_dict/", pass_dict, name="pass_dict"),
   # path("student/", Student, name="Student"),
    path("class_dict/",class_dict, name="class_dict"),
    path("color_view/", color_view, name="color_view"),
    path("template_filter/", template_filter, name="template_filter"),
  #  path("counter/", counter, name="counter"),
    path("text_for_template/", text_for_template, name="text_for_template"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    
]