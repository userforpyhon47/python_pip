from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register([Question, Choice])

class ChoiceInline(admin.StackedInline):
    model = Choice
    can_delete = False
    extra = 2
    verbose_name_plural = 'choices'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = (ChoiceInline,)
    list_display = ("question_text", "pub_date", "published_recently")
    #list_filter = ["pub_date"]
    search_fields = ["question_text"]