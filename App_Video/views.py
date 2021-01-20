from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Video.models import Video, Category, Feedback
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from App_Blog.forms import CommentForm
import uuid
# Create your views here.


# def Video_List(request):
#     return render(request,'App_Video/video_List.html',context = {})


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


class VideoList(ListView):
    context_object_name = 'videos'
    model = Video
    template_name = 'App_Video/video_list.html'
