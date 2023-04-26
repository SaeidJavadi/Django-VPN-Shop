from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser


class PartList(ListCreateAPIView):
    # queryset = ModelSerializer.objects.all()
    # serializer_class = ModelSerializer
    permission_classes = (IsAdminUser,)
    filterset_fields = ["id", "name"]  # Filter By value /api/servers?name="saeid"
    search_fields = ["id", "name"]     # Search ~ Lookup  # example.com/api/users?search=russell
    ordering_fields = '__all__'  # example.com/api/users?ordering=username   or  /users?ordering=-username
