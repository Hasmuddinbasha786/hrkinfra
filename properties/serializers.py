from rest_framework import serializers
from .models import Property, Inquiry


class PropertySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        
        try:
            if obj.image and hasattr(obj.image, 'url') and request:
                return request.build_absolute_uri(obj.image.url)
        except:
            return None

        return None


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'