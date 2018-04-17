from .models import Album
from django.shortcuts import render,get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #     url = "/music/{}".format(album.id)
    #     html += '<a href={}> {} </a> <br>'.format(url,album.album_title)
    # template = loader.get_template('music/index.html')

    # context = {'all_albums':all_albums}
    # return HttpResponse(template.render(context,request))
    # return render(request,'music/index.html',context)
    return render(request,'music/index.html',{'all_albums':all_albums})


def details(request,album_id):
    # return HttpResponse("<h2>Details for Album id {}</h2>".format(album_id))

    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album':album})




