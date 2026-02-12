from django.db import models

# Create your models here
class Society(models.Model):
    societyName = models.CharField(max_length=100)
    address = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "society"

    def __str__(self):
        return self.societyName
    
class Flat(models.Model):
    societyId = models.ForeignKey(Society, on_delete=models.CASCADE)
    flatNumber = models.CharField(max_length=10)
    blockName = models.CharField(max_length=50)

    class Meta:
        db_table = "flat"

    def __str__(self):
        return f"{self.blockName}-{self.flatNumber}"
    
class Member(models.Model):
    ROLE_CHOICES = (('Admin','Admin'),('Resident','Resident'))

    societyId = models.ForeignKey(Society, on_delete=models.CASCADE)
    flatId = models.ForeignKey(Flat, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        db_table = "member"

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    flatId = models.ForeignKey(Flat, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    dueDate = models.DateField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "maintenance"

    def __str__(self):
        return f"{self.flatId} - {self.amount}"

class Complaint(models.Model):
    STATUS_CHOICES = (('Open', 'Open'),('In Progress', 'In Progress'),('Resolved', 'Resolved'))

    memberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "complaint"

    def __str__(self):
        return self.subject
    
class Notice(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishDate = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "notice"

    def __str__(self):
        return self.title
