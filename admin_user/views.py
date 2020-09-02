from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import LoginForm
from .models import AdUser
from push_info.models import PushInfo

# Create your views here.
def index(request):
    num_deviceIds = PushInfo.objects.all().count()
    num_firebaseTokens = PushInfo.objects.all().count()
    num_messages = PushInfo.objects.all().count()
    num_authors = PushInfo.objects.all().count()

    context = {
        'num_deviceIds' : num_deviceIds,
        'num_firebaseTokens' : num_firebaseTokens,
        'num_messages' : num_messages,
        'num_authors' : num_authors,
        'user_id' : request.session.get('user'),
    }
    return render(request, 'index.html', context=context)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('user_id')
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
        
    return redirect('/')