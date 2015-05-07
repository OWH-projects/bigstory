from models import *
from django.shortcuts import *
from django.db.models import *
from bigstory.models import *
from django.http import HttpResponse


def Main (request):

    archivelist = Story.objects.filter(published=True).order_by('-date')

    dictionaries = {'archivelist': archivelist}
    return render_to_response('bigstory/main.html', dictionaries)


def Storypage(request, storytitle, section_url):

    textbox = Textblock.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    bigimagebox = bigImage.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    rightimagebox = rightImage.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    bigquotebox = bigQuote.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    extrahtmlbox = extraHtml.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    factboxes = factbox.objects.filter(storylabel__labelslug=storytitle).order_by('ranking')
    story_title = Story.objects.filter(labelslug=storytitle)
    section_tag = Story.objects.filter(sectionslug=section_url)
	
    dictionaries = {'textbox':textbox, 'bigimagebox': bigimagebox, 'rightimagebox': rightimagebox, 'bigquotebox': bigquotebox, 'extrahtmlbox': extrahtmlbox, 'factboxes':factboxes, 'story_title': story_title, 'section_tag': section_tag }
    return render_to_response('bigstory/story.html', dictionaries)

	
	
### def Chunks(request, id):	
###    chunklet = Element.objects.filter(id=id)
    	
###    dictionaries = {'chunklet': chunklet}
###    return render_to_response('bigstory/chunks.html', dictionaries)
	