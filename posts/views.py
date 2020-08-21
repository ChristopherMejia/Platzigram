"""Views App Posts"""

from django.http import HttpResponse

#Utilities
from datetime import datetime

posts = [

    {
        'name' : 'Sayulita',
        'user' : 'Yvonne Alonso',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1036',
    },
    
    {
        'name' : 'Via Lactea',
        'user' : 'Cesar Caton',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=903',
    },
    
    {
        'name' : 'Nuevo Auditorio',
        'user' : 'Thespianartist',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture' : 'https://picsum.photos/200/200/?image=1076',
    },
]

def list_posts(request):
    
    content = []
    for post in posts:
        content.append("""
           <p><strong>{name}</strong></p>
           <p><small>{user} - <i>{timestamp}</i></small></p> 
           <figure><img src="{picture}"/></figure> 
        """.format(**post) )
    return HttpResponse('<br>'.join(content) )



# Create your views here.
