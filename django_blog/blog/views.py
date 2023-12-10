from django.shortcuts import render
from django.http import HttpResponse

# Blog Post Definitions
posts = [
    {
        "title": "The Art of Effective Communication",
        "author": "John Smith",
        "content": "Mastering communication skills for success in personal and professional relationships.",
        "date": "2023-03-15"
    },
    {
        "title": "Mastering Time Management Techniques",
        "author": "Jane Doe",
        "content": "Boost productivity with proven time management strategies for ultimate efficiency.",
        "date": "2023-04-22"
    },
    {
        "title": "Navigating the World of Remote Work",
        "author": "Chris Johnson",
        "content": "Adapt to challenges and thrive in the era of remote work.",
        "date": "2023-05-10"
    }
]

# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')
