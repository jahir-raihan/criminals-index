from django.shortcuts import render
from django.views import View
from .models import Criminal
from django.db.models import Q


class CriminalsList(View):

    """
    View for listing out criminals with filtering functionality
    """

    template_name = 'index.html'

    def get(self, request):

        """
        List out criminals with filtering functionality
        """
        q = Q()
        query = request.GET.get('query', '')
        q |= Q(criminal_name__icontains=query) | Q(crime_location__icontains=query)
        q |= Q(social_links__icontains=query)

        criminals = Criminal.objects.filter(q).order_by('-created_at')

        context = {
            'criminals': criminals
        }
        return render(request, self.template_name, context)
