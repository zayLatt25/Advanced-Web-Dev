from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Case, CpuCooler, Cpu, InternalHardDrive, Memory, Motherboard, PowerSupply, GPU

def TechNest(request):
    return render(request, 'Tech_Nest.html')

@login_required
def GearGallery(request):
    return render(request, 'Gear_Gallery.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('techNest')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'Login.html')

def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')
    return render(request, 'Sign_Up.html')

def Logout(request):
    logout(request)
    request.session.flush()
    messages.success(request, "You have been logged out and your session has been cleared.")
    return redirect('Login')

@login_required
def PCAssembly(request):
    parts = {
        'Case': Case.objects.all(),
        'CPU Cooler': CpuCooler.objects.all(),
        'CPU': Cpu.objects.all(),
        'Internal Hard Drive': InternalHardDrive.objects.all(),
        'Memory': Memory.objects.all(),
        'Motherboard': Motherboard.objects.all(),
        'Power Supply': PowerSupply.objects.all(),
        'GPU': GPU.objects.all(),
    }

    for part_name, items in parts.items():
        for item in items:
            if hasattr(item, 'case_id'):
                item.id = item.case_id
            elif hasattr(item, 'cpu_cooler_id'):
                item.id = item.cpu_cooler_id
            elif hasattr(item, 'cpu_id'):
                item.id = item.cpu_id
            elif hasattr(item, 'internal_hard_drive_id'):
                item.id = item.internal_hard_drive_id
            elif hasattr(item, 'memory_id'):
                item.id = item.memory_id
            elif hasattr(item, 'motherboard_id'):
                item.id = item.motherboard_id
            elif hasattr(item, 'power_supply_id'):
                item.id = item.power_supply_id
            elif hasattr(item, 'gpu_id'):
                item.id = item.gpu_id
    return render(request, 'PC_Assembly.html', {'parts': parts})

def Parts(request):
    parts = {
        'Case': Case.objects.all(),
        'CPU Cooler': CpuCooler.objects.all(),
        'CPU': Cpu.objects.all(),
        'Internal Hard Drive': InternalHardDrive.objects.all(),
        'Memory': Memory.objects.all(),
        'Motherboard': Motherboard.objects.all(),
        'Power Supply': PowerSupply.objects.all(),
        'GPU': GPU.objects.all(),
    }
   
    for part_category, items in parts.items():
        for item in items:
            if hasattr(item, 'case_id'):
                item.id = item.case_id
            elif hasattr(item, 'cpu_cooler_id'):
                item.id = item.cpu_cooler_id
            elif hasattr(item, 'cpu_id'):
                item.id = item.cpu_id
            elif hasattr(item, 'internal_hard_drive_id'):
                item.id = item.internal_hard_drive_id
            elif hasattr(item, 'memory_id'):
                item.id = item.memory_id
            elif hasattr(item, 'motherboard_id'):
                item.id = item.motherboard_id
            elif hasattr(item, 'power_supply_id'):
                item.id = item.power_supply_id
            elif hasattr(item, 'gpu_id'):
                item.id = item.gpu_id

    return render(request, 'Parts.html', {'parts': parts})

def Part_Det(request, part_category, part_id):
    model_map = {
        'Case': Case,
        'CPU Cooler': CpuCooler,
        'CPU': Cpu,
        'Internal Hard Drive': InternalHardDrive,
        'Memory': Memory,
        'Motherboard': Motherboard,
        'Power Supply': PowerSupply,
        'GPU': GPU,
    }

    model = model_map.get(part_category)
    if not model:
        raise ValueError("Invalid model name")

    part = get_object_or_404(model, pk=part_id)
    return render(request, 'Part_Det.html', {'part': part, 'part_category': part_category})

def Main(request):
    return render(request, 'Main.html')