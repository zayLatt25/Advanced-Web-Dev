# START <<<

from django.contrib import admin
from .models import Case, CpuCooler, Cpu, InternalHardDrive, Memory, Motherboard, PowerSupply, SavedSelections

admin.site.register(Case)
admin.site.register(CpuCooler)
admin.site.register(Cpu)
admin.site.register(InternalHardDrive)
admin.site.register(Memory)
admin.site.register(Motherboard)
admin.site.register(PowerSupply)
admin.site.register(SavedSelections)

# username: zpl
# email: zpl@pc.com
# password: zplpc123

# END <<<