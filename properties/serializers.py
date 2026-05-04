# Converts data → JSON
# JSON → used by frontend
# Serializer =
# “Take data from database → convert into JSON”

from rest_framework import serializers
from .models import *


class PropertySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'

    def get_image(self, obj):
        try:
            if obj.image:
                request = self.context.get('request')

                if request:
                    return request.build_absolute_uri(obj.image.url)

                return obj.image.url

            return None

        except:
            return None


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'
