from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.urls import reverse

# Create your views here.

def main(request):

    return HttpResponse("<strong>This is the mainapp view.py message.</strong>")

# dynamic urls

def get_name(request,name,age):

    return HttpResponse(f"Hi, my name is {name} and age is {age}.")

def get_song(request,song_name,singer_name):

    return HttpResponse(f"<h1>{song_name} is the song of {singer_name}</h1>.")  


# Redirects

def login(request,username,password):    
    
    # return redirect(success,username,password)
    return redirect (f"/success/{username}/{password}/")

def success(request,username,password):

    return HttpResponse(f"{username} are logged in successfully.")


# Redirect

def files(request,username,password):

    #return redirect (f"/submission/{username}/{password}/")
    #return redirect (submission,username,password)
    # return redirect ('https://google.com')
    #return redirect (f"/submission/{username}/{password}/")

    # Reverse

    return redirect(reverse("submission", args=[username,password]))
    #return redirect(reverse("submission"))
   

def submission(request,username,password):

    return HttpResponse(f"<h1>{username}, your submission has been done!</h1>")

# Return HTML directly

def html(request):

    text = """
<!DOCTYPE html>   
<html>
    <head>
        <title>Portfolio</title>
    
        <div><h1>Ahmad Jawad Mughal</h1><address><h4>Email:ahmedjawwad02@gmail.com, Ph#+923261606606</h4></address></div>
       
    </head>
    <style>
            body{background-color: rgb(28, 50, 51);
                color: #fefefe;
                margin: 0 20%;
                font-family: serif;
                }   
            div h4{color:#808080;
                font-family: serif;
                 text-align: center;}
            div h1{text-align: center;}
            img{height: 100px; 
                width: 100px;
                object-fit: cover;
                border-radius: 50px;
            }
            h1{border-bottom:  2px solid #000000;font-family: serif}
            
    </style>
    <body>
        <img src="1680431432640.jpg" alt ="Personal Photo" style="width;16px:height;16px"/>
    
        <p>
        <h2>My Education</h2>
        <h3>BS-eCommerce</h3>
        <em>Hailey College of Commerce, University of the Punjab (2021-2025)</em>
        <h3>FSc.Pre-engineering</h3>
        <em>Government College University,Lahore (2019-2021)</em>
        </p>
        
        <p>
        <h2>My Skill</h2>
        <h4>Python  &emsp;SQL  &emsp;Accounting   &emsp;HTML5    &emsp;CSS   &emsp;Javascript<br />Probability and Statistics &emsp;Principle of Economics &emsp;Operating System Concepts</h4></p>

        
        <p>
        <h2>Certification</h2>
        <h3>Programming for Everybody (Getting Started with Python)</h3>
        <em>University of Michigan,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/4XQTGUVPNQR4</a>
        <h3>What is Data Science?</h3>
        <em>IBM,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/6EQ7SMRCEUTQ</a>
        <h3>Responsive Website Basics: Code with HTML, CSS,
            and JavaScript</h3>
        <em>UNIVERSITY OF LONDON,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/2ZCZ9VTPC3SB</a>
        <h3>Tools for Data Science</h3>
        <em>IBM,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/2HY4BAFAJMHJ</a>
        <h3>Python for Data Science, AI & Development</h3>
        <em>IBM,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/HZLZV95ZBZJ9</a>
        <h3>Python for Data Science, AI & Development</h3>
        <em>IBM,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/HZLZV95ZBZJ9</a>
        <h3>Introduction to HTML5</h3>
        <em>UNIVERSITY OF MICHIGAN,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/3M5ZJZKBUVTC</a>
        <h3>Introduction to CSS3</h3>
        <em>UNIVERSITY OF MICHIGAN,Coursera</em>
        &emsp;<a href="url">https://coursera.org/verify/XU3J8RETSUC5</a> 
        </p>
        
        <p>
        <h2>Entrolled In</h2>
        <h3>Data Science</h3>
        <em>IBM, Coursera</em>
        </p>
        <p>
        <h2>Languages</h2>
        <h4>Urdu &emsp;Punjabi &emsp;French (Beginners-level) &emsp;English (Intermediate-level)</h4></p>
        <p>
            <h2>Interest</h2>
            <h4>Movies &emsp;Snooker &emsp;Amazon &emsp;Ecommerce</h4>
        </p>
    </body>   
    
</html>
"""

    return HttpResponse(text, content_type="text/html")
    

# for template

def template_view(request):

    return render(request, "mainapp/index.html")

# passing dictionary in template

def pass_dict(request):

    #context = {"username":"AJM!","arr":["first","second"]}

    #context = {"dict1":{"username":"Ahmad!"},"age":10}

    dict1 = {"name":"AJM!","age":11}
    dict2 = {"colors":["blue","white","grey"]}
    context = {"d1":dict1,"d2":dict2}

    return render(request,"mainapp/index.html",context)


"""
# creating class

class Student:

    def __init__(self,name,age,school,student_class):

        self.name = name
        self.age = age
        self.school = school
        self.student_class = student_class


student1 = Student("Harry",10,"Kingston",4)
student2 = Student("Kate",11,"Kingston",4)
student3 = Student("Henry",14,"LS",7)
student4 = Student("Alison",16,"LS",10)
student5 = Student("William",9,"NY",3)
"""


def class_dict(request):

    array = [student1,student2,student3,student4,student5]
    

    context = {"s":array}

    return render(request,"mainapp/",context)

def color_view(request):

    context = {
        "colors":["blue", "gray", "orange"]
    }

    return render(request,"mainapp/index.html",context)

# text

def text_for_template(request):

    context = {
        "text" : "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facilis odio mollitia error illo libero eaque ducimus, nemo!"
    }


    return render(request,"mainapp/for_template.html",context)


# for template filter

def template_filter(request):
    
    context = {
        "name" : "Ahmad Jawad Mughal"
    }
    return render(request,"mainapp/for_template.html",context)

"""
# for word_counter

def counter(request):
    
    text = request.GET['text']
    amount_of_word_count = len(text.split())

    return render(request,"mainapp/counter.html",{"amount":amount_of_word_count})
"""
# for home.html & about us.html

def home(request):

    return render(request,"mainapp/home.html")

def about(request):

    return render(request,"mainapp/about_us.html")    