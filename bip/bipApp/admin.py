from django.contrib import admin
from django.utils.html import format_html
from dal import autocomplete

# Register your models here.


import bipApp.models as model

from .models import Question, Choice, Project, Task, Report, Time_Clock_Entry, Invoice_Line_Item, Invoice
from .forms import ItemForm

#admin.site.register(model.Question)


#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
Invoice_Line_Item

class TaskInLine(admin.TabularInline):
    model = Task
    show_change_link = True
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':
            ['name',
                'owner',
                'justification',
                'goals',
                'scope',
                'deliverables',
                'schedule',
                'risk_management',
                'roles',
                'quality_assurance',
                'communication',
                'resources',
                'account',
                'path',
                'complete',
            ]
        }),
        ('Date information', {'fields':
            ['pub_date',
                'start',
                'end',
            ], 'classes': ['collapse']}),
    ]
    inlines = [TaskInLine]
    list_display = ('name', 'complete', )
    readonly_fields = ('pub_date', )
    list_filter = ['complete','pub_date','owner']
    search_fields = ['name']


class ReportInLine(admin.TabularInline):
    model = Report
    show_change_link = True
    extra = 3

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'assignee', 'project', 'complete', 'opening', 'closing']}),
        ('Date information', {'fields': ['pub_date', 'start', 'end'], 'classes': ['collapse']}),
    ]
    inlines = [ReportInLine]
    list_display = ('name', 'complete', )
    readonly_fields = ('pub_date', )
    list_filter = ['complete','pub_date']
    search_fields = ['name']

class TCEInLine(admin.TabularInline):
    model = Time_Clock_Entry
    show_change_link = True
    extra = 3

class InvoiceInLine(admin.TabularInline):
    model = Invoice
    show_change_link = True
    extra = 1

class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['sub_date', 'subject', 'body', 'author', 'task', 'opening', 'closing']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [InvoiceInLine, TCEInLine]
    list_display = ('sub_date', 'subject',  'author', 'task')
    readonly_fields = ('pub_date', )
    list_filter = ['pub_date', 'sub_date']
    search_fields = ['subject', 'sub_date']


class ILIInLine(admin.TabularInline):
    model = Invoice_Line_Item
    form = ItemForm
    show_change_link = True
    extra = 3

class InvoiceAdmin(admin.ModelAdmin):
    form = ItemForm
    fieldsets = [
        (None,               {'fields': ['id', 'invoice_status', 'report', 'employee']}),
        ('Date information', {'fields': ['submitted_date', 'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ILIInLine]
    list_display = ('id', 'report',  'invoice_status')
    readonly_fields = ('pub_date', 'id')
    list_filter = ['pub_date']
    search_fields = ['report']




admin.site.register(Question, QuestionAdmin)

admin.site.register(model.Choice)

#Entity Model
admin.site.register(model.Entity)
admin.site.register(model.Contractor)
admin.site.register(model.Customer)
admin.site.register(model.Customer_Status)
admin.site.register(model.Employee)
admin.site.register(model.Vendor)
admin.site.register(model.Note)

#Project Model
admin.site.register(Project, ProjectAdmin)
admin.site.register(model.Project_Note)
admin.site.register(model.Project_Supporting_Doc)
admin.site.register(Task, TaskAdmin)
admin.site.register(model.Task_Note)
admin.site.register(model.Task_Supporting_Doc)
admin.site.register(model.Dependency_Type)
admin.site.register(model.Dependency)
admin.site.register(Report, ReportAdmin)
admin.site.register(model.Report_Note)
admin.site.register(model.Report_Supporting_Doc)
admin.site.register(model.Time_Clock_Entry)

#Account Model
admin.site.register(model.Ledger_Entry)
admin.site.register(model.Account)
admin.site.register(model.Transaction)

#Inventory Model
admin.site.register(model.Item)
admin.site.register(model.Item_Category)
admin.site.register(model.Item_Note)
admin.site.register(model.Item_Supporting_Doc)
admin.site.register(model.Invoice_Line_Item)
admin.site.register(model.Receipt_Line_Item)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(model.Invoice_Status)
admin.site.register(model.Receipt)
admin.site.register(model.Receipt_Status)
admin.site.register(model.Invoice_Transaction)
admin.site.register(model.Receipt_Transaction)
