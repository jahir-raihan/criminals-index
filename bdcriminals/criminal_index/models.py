from django.db import models


class Criminal(models.Model):
    criminal_name = models.CharField(max_length=50)
    criminal_category = models.CharField(max_length=50)
    crime_location = models.CharField(max_length=250)
    social_links = models.TextField()
    crime_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    default_image = models.FileField(upload_to='criminals_images/')

    def __str__(self):
        return f'{self.criminal_name} - Crime ID: {self.id}'


class Evidence(models.Model):
    criminal = models.ForeignKey(Criminal, related_name='evidences', on_delete=models.CASCADE)
    file = models.FileField(upload_to='evidences/')
    is_video = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.file:
            ext = self.file.name.split('.')[-1].lower()
            self.is_video = ext in ['mp4', 'mov', 'avi', 'flv', 'wmv', 'mkv']
        super(Evidence, self).save(*args, **kwargs)

    def __str__(self):
        return self.file.name

