from django.shortcuts import render

# Create your views here.
from quotes.models import Car, Driver, School, SchoolTrip, Student, StudentTrip, Trip
from rest_framework import routers, serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend


# CarSerializer and CarViewSet
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'value', 'licencePlate']

#Puedo modificar el viewset para que filtre por marca
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'licencePlate']

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'lastName', 'dateOfBirth', 'dni']

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'lastName','dni']

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'address', 'schoolCode']

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolCode']    

class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['driver', 'car', 'date']

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'driver', 'car']

class SchoolTripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolTrip
        fields = ['tripId', 'schoolId', 'tripSchoolCode']

class SchoolTripViewSet(viewsets.ModelViewSet):
    queryset = SchoolTrip.objects.all()
    serializer_class = SchoolTripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tripId', 'schoolId', 'tripSchoolCode']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'lastName', 'dateOfBirth', 'dni', 'studentCode', 'school']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'lastName', 'dni', 'studentCode', 'school']

class StudentTripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentTrip
        fields = ['studentId', 'tripId', 'studentTripCode']

class StudentTripViewSet(viewsets.ModelViewSet):
    queryset = StudentTrip.objects.all()
    serializer_class = StudentTripSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['studentId', 'tripId', 'studentTripCode']



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'trips', TripViewSet)
router.register(r'schoolstrips', SchoolTripViewSet)
router.register(r'students', StudentViewSet)
router.register(r'studenttrips', StudentTripViewSet)


