from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        #fields = ('id', 'name', 'email', 'message')
        fields = '__all__'   # 所有欄位