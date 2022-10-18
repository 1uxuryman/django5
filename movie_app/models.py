from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=500)

    @property
    def movie_count(self):
        return self.movie_set.all().count()

    def __str__(self):
        return self.name

        # all_movies = self.movie_set.all().count()
        # for i in self.movie_set.all():
        #     all_movies += i.title
        #     return all_movies




class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey("Director", on_delete=models.PROTECT, null=True)




    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount


    def __str__(self):
        return self.title



    # @property
    # def rating(self):
    #     reviews = self.reviews.all()
    #     count = reviews.count()
    #     average = 0
    #     for i in reviews:
    #         average += i.stars
    #     try:
    #         return average / count
    #     except:
    #         return 0
    #
    # @property
    # def filter_reviews(self):
    #     return [{'id': i.id, 'text': i.text, 'stars': i.stars}
    #             for i in self.reviews.filter(stars__gt=3)]





class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name='reviews',null=True)
    stars = models.IntegerField(default=1)





    # stars = models

    def __str__(self):
        return self.text

