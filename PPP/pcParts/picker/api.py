from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from .forms import PCAssemblyForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class PartsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        parts = {
            'Case': CaseSerializer(Case.objects.all(), many=True).data,
            'CPU Cooler': CpuCoolerSerializer(CpuCooler.objects.all(), many=True).data,
            'CPU': CpuSerializer(Cpu.objects.all(), many=True).data,
            'Internal Hard Drive': InternalHardDriveSerializer(InternalHardDrive.objects.all(), many=True).data,
            'Memory': MemorySerializer(Memory.objects.all(), many=True).data,
            'Motherboard': MotherboardSerializer(Motherboard.objects.all(), many=True).data,
            'Power Supply': PowerSupplySerializer(PowerSupply.objects.all(), many=True).data,
            'GPU': GPUSerializer(GPU.objects.all(), many=True).data,
        }
        return Response(parts, status=200)

class PartDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, part_category, part_id):
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
            return Response({"error": "Invalid category"}, status=400)

        part = get_object_or_404(model, pk=part_id)
        serializer_map = {
            'Case': CaseSerializer,
            'CPU Cooler': CpuCoolerSerializer,
            'CPU': CpuSerializer,
            'Internal Hard Drive': InternalHardDriveSerializer,
            'Memory': MemorySerializer,
            'Motherboard': MotherboardSerializer,
            'Power Supply': PowerSupplySerializer,
            'GPU': GPUSerializer,
        }

        serializer = serializer_map[part_category](part)
        return Response(serializer.data, status=200)

class PCAssemblyAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        parts = {
            'Case': CaseSerializer(Case.objects.all(), many=True).data,
            'CPU Cooler': CpuCoolerSerializer(CpuCooler.objects.all(), many=True).data,
            'CPU': CpuSerializer(Cpu.objects.all(), many=True).data,
            'Internal Hard Drive': InternalHardDriveSerializer(InternalHardDrive.objects.all(), many=True).data,
            'Memory': MemorySerializer(Memory.objects.all(), many=True).data,
            'Motherboard': MotherboardSerializer(Motherboard.objects.all(), many=True).data,
            'Power Supply': PowerSupplySerializer(PowerSupply.objects.all(), many=True).data,
            'GPU': GPUSerializer(GPU.objects.all(), many=True).data,
        }
        return Response(parts, status=200)
    
class SaveCustomizations(APIView):
    permission_classes = [IsAuthenticated]

   # Post request to save the customizations
    def post(self, request):

        # Prevent mismatch of entry data
        mapped_data = {
            'case_id': request.data.get('Case', None),
            'cpu_cooler_id': request.data.get('CPU Cooler', None),
            'cpu_id': request.data.get('CPU', None),
            'internal_hard_drive_id': request.data.get('Internal Hard Drive', None),
            'memory_id': request.data.get('Memory', None),
            'motherboard_id': request.data.get('Motherboard', None),
            'power_supply_id': request.data.get('Power Supply', None),
            'gpu_id': request.data.get('GPU', None),
        }
            
        form = PCAssemblyForm(data=mapped_data)
        if form.is_valid():
            # Save the customization with the authenticated user
            customization = form.save(commit=False)
            customization.user = request.user
            customization.save()
            return Response({"message": "Customizations saved successfully!"}, status=status.HTTP_201_CREATED)
        else:
            # Return form errors if invalid
            return Response({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)
     
    # Get request to retrieve all saved customizations
    def get(self, request):
        # Retrieve all saved customizations for the logged-in user
        saved_selections = SavedSelections.objects.filter(user=request.user)
        response_data = []
        
        for selection in saved_selections:
            # Build a dictionary of the saved parts' details
            saved_data = {
                "saved_id": selection.saved_id,
                "case": Case.objects.filter(case_id=selection.case_id).first(),
                "cpu_cooler": CpuCooler.objects.filter(cpu_cooler_id=selection.cpu_cooler_id).first(),
                "cpu": Cpu.objects.filter(cpu_id=selection.cpu_id).first(),
                "internal_hard_drive": InternalHardDrive.objects.filter(internal_hard_drive_id=selection.internal_hard_drive_id).first(),
                "memory": Memory.objects.filter(memory_id=selection.memory_id).first(),
                "motherboard": Motherboard.objects.filter(motherboard_id=selection.motherboard_id).first(),
                "power_supply": PowerSupply.objects.filter(power_supply_id=selection.power_supply_id).first(),
                "gpu": GPU.objects.filter(gpu_id=selection.gpu_id).first(),
                "created_at": selection.created_at
            }
            
            # Serialize the details if they exist
            response_data.append({
                "saved_id": saved_data["saved_id"],
                "case": CaseSerializer(saved_data["case"]).data if saved_data["case"] else None,
                "cpu_cooler": CpuCoolerSerializer(saved_data["cpu_cooler"]).data if saved_data["cpu_cooler"] else None,
                "cpu": CpuSerializer(saved_data["cpu"]).data if saved_data["cpu"] else None,
                "internal_hard_drive": InternalHardDriveSerializer(saved_data["internal_hard_drive"]).data if saved_data["internal_hard_drive"] else None,
                "memory": MemorySerializer(saved_data["memory"]).data if saved_data["memory"] else None,
                "motherboard": MotherboardSerializer(saved_data["motherboard"]).data if saved_data["motherboard"] else None,
                "power_supply": PowerSupplySerializer(saved_data["power_supply"]).data if saved_data["power_supply"] else None,
                "gpu": GPUSerializer(saved_data["gpu"]).data if saved_data["gpu"] else None,
                "created_at": saved_data["created_at"],
            })

        return Response(response_data, status=status.HTTP_200_OK)
    
class DeleteCustomizations(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, saved_id):
        print(saved_id)
        try:
            # Retrieve the saved customization belonging to the authenticated user
            saved_selection = SavedSelections.objects.get(saved_id=saved_id, user=request.user)
            saved_selection.delete()
            return Response({"message": "Customization deleted successfully!"}, status=status.HTTP_200_OK)
        except SavedSelections.DoesNotExist:
            return Response({"error": "Customization not found or does not belong to the user."}, status=status.HTTP_404_NOT_FOUND)