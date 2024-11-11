from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy


class BirthdayCreateView(CreateView):
    form_class = BirthdayForm
    model = Birthday

class BirthdayUpdateView(UpdateView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context