from django.db import models



class Albums(models.Model):
    title = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100, null=True)
    publishDate = models.DateField(null=True)


    def __str__(self):
        return self.title

class Songs(models.Model):
    albumName = models.ForeignKey(Albums,on_delete=models.CASCADE,null=True )
    title = models.CharField(max_length=200, null=True)
  

