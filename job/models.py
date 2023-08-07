from django.db import models
from django.utils.text import slugify

# Create your models here.



def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return f"jobs/{instance.id}/{instance.last_edit}.{extention}"


class Job(models.Model):
    JOB_TYPE = (
        ("FT", "Full Time"),
        ("PT", "Part Time"),
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE, null= True, blank=True)
    discription = models.TextField(max_length=1000, null= True, blank=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    ex_years = models.IntegerField(default=0)
    image = models.ImageField(upload_to=image_upload)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
