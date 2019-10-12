from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Post, Preference
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


@permission_classes([IsAuthenticated, ])
def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.author = request.user
            post.save()
            return Response(request)
    else:
        return Response(request)


def home(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return Response(request, context)


def detail_post_view(request, id=None):
    eachpost = get_object_or_404(Post, id=id)
    context = {'eachpost': eachpost}
    return Response(request, context)


@permission_classes([IsAuthenticated, ])
def postpreference(request, postid, userpreference):
    if request.method == "POST":
        eachpost = get_object_or_404(Post, id=postid)
        obj = ''
        valueobj = ''
        try:
            obj = Preference.objects.get(user=request.user, post=eachpost)
            valueobj = obj.value  # value of userpreference
            valueobj = int(valueobj)
            userpreference = int(userpreference)
            if valueobj != userpreference:
                obj.delete()
                upref = Preference()
                upref.user = request.user
                upref.post = eachpost
                upref.value = userpreference
                if userpreference == 1 and valueobj != 1:
                    eachpost.likes += 1
                    eachpost.dislikes -= 1
                elif userpreference == 2 and valueobj != 2:
                    eachpost.dislikes += 1
                    eachpost.likes -= 1
                upref.save()
                eachpost.save()
                context = {'eachpost': eachpost,
                           'postid': postid}
                return Response(request, context)
            elif valueobj == userpreference:
                obj.delete()
                if userpreference == 1:
                    eachpost.likes -= 1
                elif userpreference == 2:
                    eachpost.dislikes -= 1
                eachpost.save()
                context = {'eachpost': eachpost,
                           'postid': postid}
                return Response(request, context)




        except Preference.DoesNotExist:
            upref = Preference()
            upref.user = request.user
            upref.post = eachpost
            upref.value = userpreference
            userpreference = int(userpreference)
            if userpreference == 1:
                eachpost.likes += 1
            elif userpreference == 2:
                eachpost.dislikes += 1
            upref.save()
            eachpost.save()
            context = {'eachpost': eachpost,
                       'postid': postid}
            return Response(request, context)
    else:
        eachpost = get_object_or_404(Post, id=postid)
        context = {'eachpost': eachpost,
                   'postid': postid}
        return Response(request, context)
