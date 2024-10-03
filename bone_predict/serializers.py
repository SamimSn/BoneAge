from rest_framework import serializers
from .models import BoneImage


class BoneImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoneImage
        fields = "__all__"
        extra_kwargs = {
            "result": {"read_only": True}
        }
