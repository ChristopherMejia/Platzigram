"""Views App Posts"""

from django.http import HttpResponse

#Utilities
from datetime import datetime

posts[
    {
        'name' : 'Sayulita',
        'user' : 'Yvonne Alonso',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1036'
    }
]

def list_posts(request):
    posts = [1,2,3]

    return HttpResponse(str(posts))



# Create your views here.
