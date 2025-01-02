from django.db import models
from django.contrib.auth.models import User

# Extend the default User model to include additional fields if needed
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# 1. Case model
class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True, blank=True)
    psu = models.CharField(max_length=255, null=True, blank=True)
    side_panel = models.CharField(max_length=50, null=True, blank=True)
    external_525_bays = models.IntegerField(null=True, blank=True)
    internal_35_bays = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# 2. CpuCooler model
class CpuCooler(models.Model):
    cpu_cooler_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    rpm_min = models.IntegerField(null=True, blank=True)
    rpm_max = models.IntegerField(null=True, blank=True)
    noise_level_min = models.FloatField(null=True, blank=True)
    noise_level_max = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# 3. Cpu model
class Cpu(models.Model):
    cpu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    core_count = models.IntegerField(null=True, blank=True)
    core_clock = models.FloatField(null=True, blank=True)
    boost_clock = models.FloatField(null=True, blank=True)
    tdp = models.IntegerField(null=True, blank=True)
    graphics = models.CharField(max_length=255, null=True, blank=True)
    smt = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name

# 4. InternalHardDrive model
class InternalHardDrive(models.Model):
    internal_hard_drive_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    price_per_gb = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    cache = models.IntegerField(null=True, blank=True)
    form_factor = models.CharField(max_length=50)
    interface = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 5. Memory model
class Memory(models.Model):
    memory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    speed_min = models.IntegerField(null=True, blank=True)
    speed_max = models.IntegerField(null=True, blank=True)
    module_count = models.IntegerField()
    module_size = models.IntegerField()
    price_per_gb = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    first_word_latency = models.FloatField()
    cas_latency = models.FloatField()

    def __str__(self):
        return self.name

# 6. Motherboard model
class Motherboard(models.Model):
    motherboard_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    socket = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    max_memory = models.IntegerField(null=True, blank=True)
    memory_slots = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

# 7. PowerSupply model
class PowerSupply(models.Model):
    power_supply_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=50)
    efficiency = models.CharField(max_length=50, null=True, blank=True)
    wattage = models.IntegerField(null=True, blank=True)
    modular = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
# 8. GPU model
class GPU(models.Model):
    gpu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    chipset = models.CharField(max_length=255, null=True, blank=True)
    memory = models.PositiveIntegerField(help_text="Memory size in GB", null=True, blank=True)
    core_clock = models.PositiveIntegerField(help_text="Core clock speed in MHz", null=True, blank=True)
    boost_clock = models.PositiveIntegerField(help_text="Boost clock speed in MHz", null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    length = models.PositiveIntegerField(help_text="Length in mm", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.chipset})"
    

class SavedSelections(models.Model):
    saved_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_selections"
    )
    case_id = models.IntegerField(null=True, blank=True)  
    cpu_cooler_id = models.IntegerField(null=True, blank=True)  
    cpu_id = models.IntegerField(null=True, blank=True)  
    internal_hard_drive_id = models.IntegerField(null=True, blank=True)  
    memory_id = models.IntegerField(null=True, blank=True) 
    motherboard_id = models.IntegerField(null=True, blank=True) 
    power_supply_id = models.IntegerField(null=True, blank=True)  
    gpu_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saved Selection by {self.user.username} at {self.created_at}"