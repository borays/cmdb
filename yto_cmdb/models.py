from django.db import models

# Create your models here.


class idc(models.Model):
    idc_name=models.CharField(max_length=200)
    other=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idc_name

class cabinet(models.Model):
    cabinet_name=models.CharField(max_length=200)
    idc_name=models.ForeignKey(idc)
    other=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cabinet_name




class people(models.Model):
    people_name=models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    zhiwei = models.CharField(max_length=200)
    other=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.people_name

class container(models.Model):
    container_name=models.CharField(max_length=200)
    oa1=models.CharField(max_length=200,unique=True)
    oa1_pass=models.CharField(max_length=200)
    oa2 = models.CharField(max_length=200,unique=True)
    oa2_pass=models.CharField(max_length=200)
    vc1 = models.CharField(max_length=200,unique=True)
    vc1_pass=models.CharField(max_length=200)
    vc2 = models.CharField(max_length=200,unique=True)
    vc2_pass=models.CharField(max_length=200)
    other=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.container_name

class cmdb(models.Model):
    cabinet_name = models.ForeignKey(cabinet)
    place_text=models.CharField(max_length=200)
    model_text=models.CharField(max_length=200)
    vender_text = models.CharField(max_length=200)
    sn_text = models.CharField(max_length=200)
    ip_text=models.CharField(max_length=200,unique=True)
    user_text = models.CharField(max_length=200)
    pass_text=models.CharField(max_length=200)
    app_text=models.CharField(max_length=200)
    order_text=models.CharField(max_length=200)
    mana_ip=models.CharField(max_length=200,unique=True)
    mana_user = models.CharField(max_length=200)
    mana_pass=models.CharField(max_length=200)
    people_name=models.ForeignKey(people)
    container_name=models.ForeignKey(container)
    ma_date = models.DateField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_text


class vm_cluster(models.Model):
    vm_cluster_name=models.CharField(max_length=200)
    other=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vm_cluster_name

class vm(models.Model):
    vm_cluster_name = models.ForeignKey(vm_cluster)
    ip_text=models.CharField(max_length=200,unique=True)
    app_text = models.CharField(max_length=200)
    order_text = models.CharField(max_length=200)
    os_text = models.CharField(max_length=200)
    pool_text = models.CharField(max_length=200)
    user_text = models.CharField(max_length=200)
    pass_text = models.CharField(max_length=200)
    cpu_text = models.CharField(max_length=200)
    mem_text = models.CharField(max_length=200)
    disk_text = models.CharField(max_length=200)
    date_added=models.DateField()

    def __str__(self):
        return self.ip_text