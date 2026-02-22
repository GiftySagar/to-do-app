from django.shortcuts import render,redirect

from .models import TaskModel,CompleteModel,TrashModel

# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)
        
        TaskModel.objects.create(
            title=title_data,
            desc=desc_data
        )
    return render(request,'add.html')

def completed(request,pk):
    #fletched the data from the taskmodel
    a = TaskModel.objects.get(id=pk)

    #created the same fletched records into the completeModel(newmodel)
    CompleteModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    #delete the record from the taskmodel
    a.delete()
    return redirect('complete')

    

def complete(request):
    a = CompleteModel.objects.all()
    return render(request,'complete.html',{'data':a})


def delete_(request,pk):

    a = TaskModel.objects.get(id=pk)

    TrashModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('home')


def trash(request):
    a = TrashModel.objects.all()
    return render(request,'trash.html',{'data':a})

def delete_all(request):
    #collected all the data from the task model
    a = TaskModel.objects.all()

    #we have to itterate in the querryset and we are creating the records in the trash model
    for i in a:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )

        #delete the record which is present in the taskmodel
        i.delete()
    return redirect('home')

def restore(request,pk):
    a = TrashModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('home')



def about(request):
    return render(request,'about.html')


# complete page - delete,delete_all,restore
# trash page - delete,delete_all


def update(request,a):
    data = TaskModel.objects.get(id=a)
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)
        data.title = title_data
        data.desc = desc_data
        data.save()
        return redirect('home')

    return render(request,'update.html',{'data':data})

def trestore(request):
    a = TrashModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title= i.title,
            desc= i.desc
        )
        i.delete()

    return redirect('home')




# home page - update,complete,delete,delete_all
# complete page - delete,delete_all,restore,restore_all
# trash page - delete,delete_all,restore,restore_all



def cdelete_all(request):
    a = CompleteModel.objects.all()
    for i in a:
        TrashModel.objects.create(
            title=i.title,
            desc=i.desc
        )
        i.delete()
    return redirect('complete')

def crestore_all(request):
    a = CompleteModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title= i.title,
            desc= i.desc
        )
        i.delete()

    return redirect('home')




def cdelete(request,pk):

    a = CompleteModel.objects.get(id=pk)

    TrashModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('complete')


def crestore(request,pk):

    a = CompleteModel.objects.get(id=pk)

    TaskModel.objects.create(
        title=a.title,
        desc=a.desc
    )
    a.delete()
    return redirect('complete')




def tdelete(request,a):

    a = TrashModel.objects.get(id=a)
    a.delete()
    return redirect('trash')


def tdelete_all(request):
    a  = TrashModel.objects.all()
    a.delete()
    return redirect('trash')


