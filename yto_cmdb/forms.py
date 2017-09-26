from django import forms

from .views import cmdb
from .models import people, container, cabinet, cmdb, idc, vm_cluster, vm


class CmdbForm(forms.ModelForm):
    class Meta:
        model = cmdb
        fields = ['cabinet_name', 'place_text', 'model_text', 'vender_text', 'sn_text', 'ip_text', 'user_text',
                  'pass_text', 'app_text', 'order_text', 'mana_ip', 'mana_user', 'mana_pass', 'people_name',
                  'container_name', 'ma_date']
        labels = {'cabinet_name': '机柜', 'place_text': '设备位置', 'model_text': '型号', 'vender_text': '厂商', 'sn_text': '序列号',
                  'ip_text': 'IP地址:', 'user_text': '用户名', 'pass_text': '密码:', 'app_text': '应用',
                  'order_text': '负责人',
                  'mana_ip': '管理IP', 'mana_user': '管理用户名', 'mana_pass': '管理密码', 'people_name': '维护人',
                  'container_name': '容器', 'ma_date': '维保日期'}


class IDCForm(forms.ModelForm):
    class Meta:
        model = idc
        fields = ['idc_name', 'other']
        labels = {'idc_name': '机房名称', 'other': '备注'}


class CabinetForm(forms.ModelForm):
    class Meta:
        model = cabinet
        fields = ['cabinet_name', 'idc_name', 'other']
        labels = {'cabinet_name': '机柜名称', 'idc_name': '所属机房', 'other': '备注'}


class PeopleForm(forms.ModelForm):
    class Meta:
        model = people
        fields = ['people_name', 'phone', 'zhiwei', 'other']
        labels = {'people_name': '姓名', 'phone': '手机号', 'zhiwei': '职位', 'other': '备注'}


class ContainerForm(forms.ModelForm):
    class Meta:
        model = container
        fields = ['container_name', 'oa1', 'oa1_pass', 'oa2', 'oa2_pass', 'vc1', 'vc1_pass', 'vc2', 'vc2_pass', 'other']
        labels = {'container_name': 'C7000名称', 'oa1': 'OA1 IP', 'oa1_pass': 'OA1密码', 'oa2': 'OA2 IP',
                  'oa2_pass': 'OA2密码', 'vc1': 'VC1 IP', 'vc1_pass': 'VC1密码', 'vc2': 'VC2 IP', 'vc2_pass': 'VC2密码',
                  'other': '备注'}


class VmClusterForm(forms.ModelForm):
    class Meta:
        model = vm_cluster
        fields = ['vm_cluster_name', 'other']
        labels = {'vm_cluster_name': '集群', 'other': '用途'}


class VmForm(forms.ModelForm):
    class Meta:
        model = vm
        fields = ['vm_cluster_name', 'ip_text', 'app_text', 'order_text', 'os_text', 'pool_text', 'user_text',
                  'pass_text', 'cpu_text', 'mem_text', 'disk_text', 'date_added']
        labels = {'vm_cluster_name': '集群', 'ip_text': 'IP', 'app_text': '应用', 'order_text': '负责人', 'os_text': '操作系统',
                  'pool_text': '资源池', 'user_text': '用户名', 'pass_text': '密码', 'cpu_text': 'CPU', 'mem_text': 'MEM',
                  'disk_text': 'DISK', 'date_added': '建立时间'}
