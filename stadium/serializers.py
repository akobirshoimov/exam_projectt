from rest_framework.serializers import ModelSerializer 
from .models import FieldsModel,BronModel

class FieldsSerializers(ModelSerializer):
    class Meta:
        model = FieldsModel
        fields = ('__all__')


class BronSerialozers(ModelSerializer):
    class Meta:
        model = BronModel
        fields = ('__all_')
