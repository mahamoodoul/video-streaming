from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Video.models import Video, Category, Feedback
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Video.forms import CommentForm
import uuid
# Create your views here.


def video_list(request):
    videos = Video.objects.all()
    category = Category.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search', '')
        results = Video.objects.filter(vidoe_title__icontains=search)
    return render(request,'App_Video/video_List.html',context = {'videos': videos, 'search':search, 'results':results, 'category':category})


class PublishVideo(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'App_Video/publish_video.html'
    fields = ('vidoe_title','video_category','video_description', 'video_link',)

    def form_valid(self, form):
        video_obj = form.save(commit=False)
        video_obj.author = self.request.user
        title = video_obj.vidoe_title
        video_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        video_obj.save()
        return HttpResponseRedirect(reverse('index'))


# class VideoList(ListView):
#     context_object_name = 'videos'
#     model = Video
#     template_name = 'App_Video/video_list.html'


@login_required
def video_details(request, slug ):
    video = Video.objects.get(slug=slug)
    comment_form = CommentForm()
    category = Category.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            return HttpResponseRedirect(reverse('App_Video:video_details', kwargs={'slug':slug}))
    return render(request, 'App_Video/video_details.html', context={'video':video, 'comment_form':comment_form,'category':category })


def category_wise(request, pk):
    cat_wise_videos = Video.objects.filter(video_category=pk)
    category = Category.objects.all()
    return render(request,'App_Video/video_List.html',context = {'catgory_wise':True ,'cat_wise_videos':cat_wise_videos, 'category':category})
