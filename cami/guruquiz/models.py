from django.db import models


class Blogger(models.Model):
    """
    Each row represents a blogger who has her own page.
    """
    yt_username = models.CharField(max_length=200)
    yt_display_name = models.CharField(max_length=200)
    yt_id = models.CharField(max_length=200)
    yt_home_url = models.CharField(max_length=200)


class Quiz(models.Model):
    """
    Each row represents a possible answer to a question on the beauty quiz.
    """
    answer_text = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    respondents = models.ManyToManyField(Blogger, through='BloggerToQuiz')


class BloggerToQuiz(models.Model):
    """
    Each row represents a quiz response associated with a given blogger.
    """
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    last_modified = models.DateTimeField('last modified at')


class Video(models.Model):
    """
    Each row represents a video published by a blogger.
    """
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    transcript = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')


class Product(models.Model):
    """
    Each row represents a product listed in the description section of a video.
    """
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True)
    source_videos = models.ManyToManyField(Video, through='ProductToVideo')


class ProductToVideo(models.Model):
    """
    Each row represents a product mentionned in the description section of
    a given video.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_modified = models.DateTimeField('last modified at')
