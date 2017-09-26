from django.shortcuts import render

# Create your views here.
from .models import cmdb, idc, cabinet, people, container, vm_cluster, vm
from .forms import CmdbForm, IDCForm, CabinetForm, PeopleForm, ContainerForm, VmClusterForm, VmForm

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# limits
from django.contrib.auth.decorators import login_required,permission_required

# page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# for search
from django.db.models import Q


### for server
def index(request):
    return render(request, 'yto_cmdb/index.html')

@permission_required('yto_cmdb.delete_cmdb', 'yto_cmdb.add_cmdb','yto_cmdb.change_cmdb')
@login_required()
def server_new(request):
    if request.method != 'POST':
        form = CmdbForm()
    else:
        form = CmdbForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:server_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/server/new_item.html', content)

@permission_required('yto_cmdb.delete_cmdb', 'yto_cmdb.add_cmdb','yto_cmdb.change_cmdb')
@login_required()
def server_edit(request, item_id):
    entry = cmdb.objects.get(id=item_id)

    if request.method != 'POST':
        form = CmdbForm(instance=entry)
    else:
        form = CmdbForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:server_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/server/edit_item.html', content)

@permission_required('yto_cmdb.delete_cmdb', 'yto_cmdb.add_cmdb','yto_cmdb.change_cmdb')
@login_required()
def server_delete(request, item_id):
    cmdb.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:server_items'))

@permission_required('yto_cmdb.delete_cmdb', 'yto_cmdb.add_cmdb','yto_cmdb.change_cmdb')
@login_required()
def server_list(request):
    cmdb_list = cmdb.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/server/items.html', contents)

@permission_required('yto_cmdb.delete_cmdb', 'yto_cmdb.add_cmdb','yto_cmdb.change_cmdb')
@login_required()
def server_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = cmdb.objects.filter(
        Q(cabinet_name__cabinet_name__icontains=q) | Q(place_text__icontains=q) | Q(model_text__icontains=q) | Q(
            vender_text__icontains=q) | Q(sn_text__icontains=q) | Q(ip_text__icontains=q) | Q(
            mana_ip__icontains=q) | Q(app_text__icontains=q) | Q(
            order_text__icontains=q) | Q(people_name__people_name__icontains=q) | Q(
            container_name__container_name__icontains=q) | Q(ma_date__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/server/items.html', contents)


###for idc

@permission_required('yto_cmdb.delete_idc', 'yto_cmdb.add_idc','yto_cmdb.change_idc')
@login_required()
def idc_new(request):
    if request.method != 'POST':
        form = IDCForm()
    else:
        form = IDCForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:idc_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/idc/new_item.html', content)

@permission_required('yto_cmdb.delete_idc', 'yto_cmdb.add_idc','yto_cmdb.change_idc')
@login_required()
def idc_edit(request, item_id):
    entry = idc.objects.get(id=item_id)

    if request.method != 'POST':
        form = IDCForm(instance=entry)
    else:
        form = IDCForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:idc_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/idc/edit_item.html', content)

@permission_required('yto_cmdb.delete_idc', 'yto_cmdb.add_idc','yto_cmdb.change_idc')
@login_required()
def idc_delete(request, item_id):
    idc.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:idc_items'))

@permission_required('yto_cmdb.delete_idc', 'yto_cmdb.add_idc','yto_cmdb.change_idc')
@login_required()
def idc_list(request):
    cmdb_list = idc.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/idc/items.html', contents)

@permission_required('yto_cmdb.delete_idc', 'yto_cmdb.add_idc','yto_cmdb.change_idc')
@login_required()
def idc_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = idc.objects.filter(Q(idc_name__icontains=q) | Q(other__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/idc/items.html', contents)


### for cabinet

@permission_required('yto_cmdb.delete_cabinet', 'yto_cmdb.add_cabinet','yto_cmdb.change_cabinet')
@login_required()
def cabinet_new(request):
    if request.method != 'POST':
        form = CabinetForm()
    else:
        form = CabinetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:cabinet_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/cabinet/new_item.html', content)

@permission_required('yto_cmdb.delete_cabinet', 'yto_cmdb.add_cabinet','yto_cmdb.change_cabinet')
@login_required()
def cabinet_edit(request, item_id):
    entry = cabinet.objects.get(id=item_id)

    if request.method != 'POST':
        form = CabinetForm(instance=entry)
    else:
        form = CabinetForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:cabinet_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/cabinet/edit_item.html', content)

@permission_required('yto_cmdb.delete_cabinet', 'yto_cmdb.add_cabinet','yto_cmdb.change_cabinet')
@login_required()
def cabinet_delete(request, item_id):
    cabinet.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:cabinet_items'))

@permission_required('yto_cmdb.delete_cabinet', 'yto_cmdb.add_cabinet','yto_cmdb.change_cabinet')
@login_required()
def cabinet_list(request):
    cmdb_list = cabinet.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/cabinet/items.html', contents)

@permission_required('yto_cmdb.delete_cabinet', 'yto_cmdb.add_cabinet','yto_cmdb.change_cabinet')
@login_required()
def cabinet_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = cabinet.objects.filter(
        Q(cabinet_name__icontains=q) | Q(idc_name__idc_name__contains=q) | Q(other__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/cabinet/items.html', contents)


### for people

@permission_required('yto_cmdb.delete_people', 'yto_cmdb.add_people','yto_cmdb.change_people')
@login_required()
def people_new(request):
    if request.method != 'POST':
        form = PeopleForm()
    else:
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:people_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/people/new_item.html', content)

@permission_required('yto_cmdb.delete_people', 'yto_cmdb.add_people','yto_cmdb.change_people')
@login_required()
def people_edit(request, item_id):
    entry = people.objects.get(id=item_id)

    if request.method != 'POST':
        form = PeopleForm(instance=entry)
    else:
        form = PeopleForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:people_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/people/edit_item.html', content)

@permission_required('yto_cmdb.delete_people', 'yto_cmdb.add_people','yto_cmdb.change_people')
@login_required()
def people_delete(request, item_id):
    people.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:people_items'))

@permission_required('yto_cmdb.delete_people', 'yto_cmdb.add_people','yto_cmdb.change_people')
@login_required()
def people_list(request):
    cmdb_list = people.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/people/items.html', contents)

@permission_required('yto_cmdb.delete_people', 'yto_cmdb.add_people','yto_cmdb.change_people')
@login_required()
def people_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = people.objects.filter(
        Q(people_name__icontains=q) | Q(phone__icontains=q) | Q(zhiwei__icontains=q) | Q(other__icontains=q)).order_by(
        'date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/people/items.html', contents)


### for container
@permission_required('yto_cmdb.delete_container', 'yto_cmdb.add_container','yto_cmdb.change_container')
@login_required()
def container_new(request):
    if request.method != 'POST':
        form = ContainerForm()
    else:
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:container_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/container/new_item.html', content)

@permission_required('yto_cmdb.delete_container', 'yto_cmdb.add_container','yto_cmdb.change_container')
@login_required()
def container_edit(request, item_id):
    entry = container.objects.get(id=item_id)

    if request.method != 'POST':
        form = ContainerForm(instance=entry)
    else:
        form = ContainerForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:container_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/container/edit_item.html', content)

@permission_required('yto_cmdb.delete_container', 'yto_cmdb.add_container','yto_cmdb.change_container')
@login_required()
def container_delete(request, item_id):
    container.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:container_items'))

@permission_required('yto_cmdb.delete_container', 'yto_cmdb.add_container','yto_cmdb.change_container')
@login_required()
def container_list(request):
    cmdb_list = container.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/container/items.html', contents)

@permission_required('yto_cmdb.delete_container', 'yto_cmdb.add_container','yto_cmdb.change_container')
@login_required()
def container_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = container.objects.filter(
        Q(container_name__icontains=q) | Q(oa1__icontains=q) | Q(oa2__icontains=q) | Q(vc1__icontains=q) | Q(
            vc2__icontains=q) | Q(other__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/container/items.html', contents)


### for vm_cluster
@permission_required('yto_cmdb.delete_vm_cluster', 'yto_cmdb.add_vm_cluster','yto_cmdb.change_vm_cluster')
@login_required()
def vm_cluster_new(request):
    if request.method != 'POST':
        form = VmClusterForm()
    else:
        form = VmClusterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:vm_cluster_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/vm_cluster/new_item.html', content)

@permission_required('yto_cmdb.delete_vm_cluster', 'yto_cmdb.add_vm_cluster','yto_cmdb.change_vm_cluster')
@login_required()
def vm_cluster_edit(request, item_id):
    entry = vm_cluster.objects.get(id=item_id)

    if request.method != 'POST':
        form = VmClusterForm(instance=entry)
    else:
        form = VmClusterForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:vm_cluster_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/vm_cluster/edit_item.html', content)

@permission_required('yto_cmdb.delete_vm_cluster', 'yto_cmdb.add_vm_cluster','yto_cmdb.change_vm_cluster')
@login_required()
def vm_cluster_delete(request, item_id):
    vm_cluster.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:vm_cluster_items'))

@permission_required('yto_cmdb.delete_vm_cluster', 'yto_cmdb.add_vm_cluster','yto_cmdb.change_vm_cluster')
@login_required()
def vm_cluster_list(request):
    cmdb_list = vm_cluster.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/vm_cluster/items.html', contents)

@permission_required('yto_cmdb.delete_vm_cluster', 'yto_cmdb.add_vm_cluster','yto_cmdb.change_vm_cluster')
@login_required()
def vm_cluster_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = vm_cluster.objects.filter(
        Q(vm_cluster_name__icontains=q) | Q(other__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/vm_cluster/items.html', contents)


### for vms
@permission_required('yto_cmdb.delete_vm', 'yto_cmdb.add_vm','yto_cmdb.change_vm')
@login_required()
def vm_new(request):
    if request.method != 'POST':
        form = VmForm()
    else:
        form = VmForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:vm_items'))
    content = {'form': form}
    return render(request, 'yto_cmdb/vm/new_item.html', content)

@permission_required('yto_cmdb.delete_vm', 'yto_cmdb.add_vm','yto_cmdb.change_vm')
@login_required()
def vm_edit(request, item_id):
    entry = vm.objects.get(id=item_id)

    if request.method != 'POST':
        form = VmForm(instance=entry)
    else:
        form = VmForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yto_cmdb:vm_items'))
    content = {'entry': entry, 'form': form}
    return render(request, 'yto_cmdb/vm/edit_item.html', content)

@permission_required('yto_cmdb.delete_vm', 'yto_cmdb.add_vm','yto_cmdb.change_vm')
@login_required()
def vm_delete(request, item_id):
    vm.objects.get(id=item_id).delete()
    return HttpResponseRedirect(reverse('yto_cmdb:vm_items'))

@permission_required('yto_cmdb.delete_vm', 'yto_cmdb.add_vm','yto_cmdb.change_vm')
@login_required()
def vm_list(request):
    cmdb_list = vm.objects.all().order_by('date_added')
    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums}
    return render(request, 'yto_cmdb/vm/items.html', contents)

@permission_required('yto_cmdb.delete_vm', 'yto_cmdb.add_vm','yto_cmdb.change_vm')
@login_required()
def vm_search(request):
    q = request.GET.get('keyword')
    if not q:
        pass

    cmdb_list = vm.objects.filter(Q(vm_cluster_name__vm_cluster_name__icontains=q) | Q(ip_text__icontains=q) | Q(
            app_text__icontains=q) | Q(
            order_text__icontains=q) | Q(os_text__icontains=q) | Q(pool_text__icontains=q) | Q(
            user_text__icontains=q) | Q(cpu_text__icontains=q) | Q(mem_text__icontains=q) | Q(
            disk_text__icontains=q)).order_by('date_added')

    nums = len(cmdb_list)
    paginator = Paginator(cmdb_list, 10)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)

    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    contents = {'topics': content, 'nums': nums, 'keyword': q}
    return render(request, 'yto_cmdb/vm/items.html', contents)
