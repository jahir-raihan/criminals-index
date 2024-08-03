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


class CriminalsDetails(View):

    """
    View for criminal details with all evidences
    """

    template_name = 'viewcriminaldata.html'

    def get(self, request, pk):

        """
        Get given primary key criminals details
        """

        criminal_details = Criminal.objects.filter(pk=pk).prefetch_related('evidences').first()
        context = {
            "criminal_details": criminal_details
        }

        return render(request, self.template_name, context)

