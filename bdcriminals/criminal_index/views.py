from django.shortcuts import render, redirect
from django.views import View
from .models import Criminal, Evidence
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


class CreateCriminalRecord(View):

    """
    Create a new record with all necessary data and evidences
    """

    template_name = 'form.html'

    def get(self, request):

        """
        Render the template
        """

        return render(request, self.template_name, {})

    def post(self, request):

        """
        Store the record and redirect to details page of the new record
        """

        try:
            criminal_name = request.POST.get('criminal_name')
            criminal_category = request.POST.get('criminal_category')
            crime_location = request.POST.get('crime_location')
            social_links = request.POST.get('social_links')
            crime_details = request.POST.get('crime_details')

            images = request.FILES.getlist('image')
            videos = request.FILES.getlist('video')

            # Create and save Criminal instance
            criminal = Criminal.objects.create(
                criminal_name=criminal_name,
                criminal_category=criminal_category,
                crime_location=crime_location,  # Add location if available
                social_links=social_links,
                crime_details=crime_details,
                default_image=images[0] if images else None
            )

            # Save remaining images and videos as Evidence
            for file in images[1:]:  # Skip the first image
                Evidence.objects.create(
                    criminal=criminal,
                    file=file,
                    is_video=False
                )

            for file in videos:
                Evidence.objects.create(
                    criminal=criminal,
                    file=file,
                    is_video=True
                )

            return redirect('criminal_details', pk=criminal.pk)
        except:
            return render(request, self.template_name, {})

