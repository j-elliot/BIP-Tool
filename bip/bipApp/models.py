#import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

### ### ### Account Model ### ### ###

class Ledger_Entry(models.Model):
    description = models.TextField(blank=True)
    transaction_date = models.DateTimeField('date transacted')
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.transaction_date

    class Meta:
        verbose_name_plural = "Ledger_Entries"

class Account(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.FloatField(blank=True)
    debit = models.BooleanField('date transacted')
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Ledger_Entry, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount

### ### ### Entity Model ### ### ###

class Entity(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    companyname = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    interests_dep = models.CharField(max_length=255, null=True, blank=True)
    birthdate_dep = models.DateField('birthday', null=True, blank=True)
    spouse_dep = models.CharField(max_length=255, null=True, blank=True)
    children_dep = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Entities"

class Contractor(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.entity.name

class Customer_Status(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Customer_Status, on_delete=models.CASCADE)
    interest = models.CharField(max_length=255,blank=True, null=True)
    birthdate = models.DateField('birthdate', blank=True, null=True)
    spouse = models.ForeignKey(Entity, related_name='spouse', on_delete=models.CASCADE, blank=True, null=True)
    path = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.entity.name

class Employee(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    date_hired = models.DateField('date hired', blank=True, null=True)
    ssn = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.entity.name

class Vendor(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    tin = models.CharField(max_length=255, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.entity.name

class Note(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    subject = models.TextField(blank=True)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject



### ### ### Project Model ### ### ###


class Project(models.Model):
    owner = models.ForeignKey(Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    plan_ref = models.CharField(max_length=255, null=True, blank=True)
    justification = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    deliverables = models.TextField(blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    risk_management = models.TextField(blank=True, null=True)
    roles = models.TextField(blank=True, null=True)
    quality_assurance = models.TextField(blank=True, null=True)
    communication = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    start = models.DateTimeField('start date', blank=True, null=True)
    end = models.DateTimeField('end date', blank=True, null=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, blank=True)
    path = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Project_Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject


class Project_Supporting_Doc(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    path = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    filetype = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    start = models.DateTimeField('start date')
    end = models.DateTimeField('end date')
    assignee = models.ForeignKey(Entity, on_delete=models.CASCADE)
    opening = models.BooleanField(blank=True, null=True, default=False)
    closing = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.name


class Dependency_Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dependency(models.Model):
    predecessor = models.ForeignKey(Task, related_name='predecessors', on_delete=models.CASCADE)
    successor = models.ForeignKey(Task, related_name='successors', on_delete=models.CASCADE)
    type = models.ForeignKey(Dependency_Type, on_delete=models.CASCADE)




class Task_Note(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject


class Task_Supporting_Doc(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(Entity, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    sub_date = models.DateField('date referenced', blank=True)
    opening = models.BooleanField(blank=True, null=True, default=False)
    closing = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.subject


class Report_Note(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject


class Report_Supporting_Doc(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Time_Clock_Entry(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    start = models.DateTimeField('start date', blank=True, null=True)
    end = models.DateTimeField('end date', blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    ledger_entry = models.ForeignKey(Ledger_Entry, null=True, blank=True, on_delete=models.CASCADE)
    worker = models.ForeignKey(Entity, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.report.subject

    class Meta:
        verbose_name_plural = "Time_Clock_Entries"



### ### ### Inventory Model ### ### ###

class Item_Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    markup = models.FloatField(blank=True, null=True)
    vendor = models.ForeignKey(Entity, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(null=True, blank=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Item_Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Item_Note(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject


class Item_Supporting_Doc(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    path = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    filetype = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Invoice_Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    submitted_date = models.DateTimeField('date submitted', blank=True, null=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    invoice_status = models.ForeignKey(Invoice_Status, on_delete=models.CASCADE)
    employee = models.ForeignKey(Entity, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.report.subject

class Invoice_Transaction(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.report.subject

class Invoice_Line_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    price = models.FloatField(blank=True)
    quantity = models.FloatField(blank=True)

    def __str__(self):
        return self.invoice.report.subject

class Receipt_Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    purchase_date = models.DateTimeField('date purchased')
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Entity, on_delete=models.CASCADE)
    total = models.FloatField(blank=True)
    description = models.TextField(blank=True)
    receipt_status = models.ForeignKey(Receipt_Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.report.subject

class Receipt_Transaction(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return self.report.subject

class Receipt_Line_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    price = models.FloatField(blank=True)
    quantity = models.FloatField(blank=True)

    def __str__(self):
        return self.receipt.report.subject
