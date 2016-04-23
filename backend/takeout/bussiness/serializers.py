from rest_framework import serializers
from models.seller import Seller
from models.store import Store


class SellerSerializer(serializers.ModelSerializer):
    #store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = Seller
        fields = (
            'username', 'password', 'account_type', 'nickname', 'store_id'
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            'name', 'address', 'phone', 'announcement',
            'description', 'is_banned', 'owner'
        )
