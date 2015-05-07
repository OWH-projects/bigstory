from django.db import models
from django.db.models import *
from django.template.defaultfilters import slugify


		
class Story(models.Model):
    section = models.CharField(help_text="For analytics purposes", max_length=200, editable=True, blank=True)
    sectionslug = models.CharField(max_length=200, editable=False, null=True, blank=True)	
    seolabel = models.CharField(max_length=300, editable=True, null=True, blank=True)
    label = models.CharField(help_text="This will also be your headline", max_length=300, editable=True)
    labelslug = models.CharField("URL", max_length=500, editable=False)
    published = models.NullBooleanField(null=True, blank=True)
    link = models.TextField(blank=True)
    author = models.CharField(help_text="Just the name. Don't put 'By'", max_length=100, blank=True, null=True)	
    summary = models.TextField(blank=True)	
    headerimage = models.ImageField(help_text="Image at the top", upload_to="bigstoryphotos/", blank=True)
    caption = models.CharField(help_text="Cutline under photo if needed", max_length=500, blank=True, null=True)	
    headermargin = models.PositiveIntegerField(help_text="Can change how far the headline is from the top of the window. Default is 33%. Use numbers only", blank=True, null=True)
    blacktext = models.CharField(blank=True, null=True, max_length=5, help_text="Put the word black in this box, and the headline will be black.")
    smallerheader = models.BooleanField(help_text="For a different header appearance with smaller photo", default=False, blank=True)
    teaserimage = models.ImageField(help_text="Image for big story archive", upload_to="bigstoryphotos/", blank=True)
    date = models.DateTimeField(null=True, blank=True)
    priority = models.PositiveIntegerField(help_text="For archive page", null=True, blank=True, editable=False)	

	
    def __unicode__(self):
        return self.label
 
    def save(self):
        self.labelslug = slugify(self.label)
        self.sectionslug = slugify(self.section)		
        self.link = 'http://dataomaha.com/bigstory/%s/%s' % (self.sectionslug, self.labelslug)
        super(Story, self).save()

		
		
class Textblock(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    subhead = models.CharField(max_length=300, editable=True, blank=True)
    text = models.TextField(blank=True)	

	
    def __unicode__(self):
        return self.title
		
    def save(self):
       super(Textblock, self).save()
	   
	   
	   
class bigImage(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    subhead = models.ImageField(help_text="Big image", upload_to="bigstoryphotos/", blank=True)
    text = models.TextField(help_text="Cutline", blank=True)	
	
    def __unicode__(self):
        return self.title
		
    def save(self):
       super(bigImage, self).save()
	   	   
	   
	   
class rightImage(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    header = models.CharField(blank=True, null=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    subhead = models.ImageField(help_text="Image float right", upload_to="bigstoryphotos/", blank=True)
    text = models.TextField(help_text="Cutline", blank=True)
    diffwidth = models.CharField(help_text="Changes pixel width of floating image. Just use number; no need for 'px'", max_length=4, blank=True )


    def __unicode__(self):
        return self.title
		
    def save(self):
       super(rightImage, self).save()
	   
	   
class bigQuote(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    text = models.TextField(blank=True)	

    def __unicode__(self):
        return self.title
		
    def save(self):
       super(bigQuote, self).save()	   

	   
class extraHtml(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    text = models.TextField(help_text="Any other HTML elements", blank=True)	

    def __unicode__(self):
        return self.title
		
    def save(self):
       super(extraHtml, self).save()	   
	   
class factbox(models.Model):
    ranking = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(blank=True, max_length=300)
    storylabel = models.ForeignKey(Story)
    subhead = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)	

    def __unicode__(self):
        return self.title
		
    def save(self):
       super(factbox, self).save()		   
	   

	   
