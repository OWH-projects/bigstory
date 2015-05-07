from django.contrib import admin
from django import forms
from django.forms import SelectMultiple
from bigstory.models import *
from django.forms import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from merged_inlines.admin import MergedInlineAdmin


class TextblockInline(admin.TabularInline):
    model = Textblock
    extra = 1
    fieldsets = (
		(None, {
			'fields': ('ranking', 'title', 'subhead', 'text' )
		}),

    )	
	

	
class bigImageInline(admin.TabularInline):
    model = bigImage
    extra = 1


	
	
class rightImageInline(admin.TabularInline):
    model = rightImage	
    extra = 1

	
class bigQuoteInline(admin.TabularInline):
    model = bigQuote	
    extra = 1

	
class extraHtmlInline(admin.TabularInline):
    model = extraHtml	
    extra = 1	
	
class factboxInline(admin.TabularInline):
    model = factbox	
    extra = 1	
	
class StoryAdmin(MergedInlineAdmin):
    ordering = [ 'date', ]
    list_filter = [ 'author', 'date' ]
    search_fields = ['label', 'author']
    readonly_fields=('link',)
    merged_inline_order = 'ranking'
    inlines = [
        TextblockInline, factboxInline, bigImageInline, rightImageInline, bigQuoteInline, extraHtmlInline
    ]	
def has_add_permission(self, request):
        return True
	

admin.site.register(Textblock)
admin.site.register(factbox)
admin.site.register(bigImage)
admin.site.register(rightImage)
admin.site.register(bigQuote)
admin.site.register(extraHtml)
admin.site.register(Story, StoryAdmin)



