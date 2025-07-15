from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)
    
    songs = serializers.SerializerMethodField(read_only =True)
    
    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        tag = instance.tags.all()
        return [t.name for t in tag]
    class Meta:
        model = Singers
        fields = '__all__'
    
    image = serializers.ImageField(use_url=True, required=False)

    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs, many = True)
        return serializers.data
    
    class Meta:
        model = Singers
        fields = '__all__'
        
class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source='singer.name', read_only=True)
    
    class Meta:
        model = Songs
        fields = ['id', 'singer', 'singer_name', 'title', 'release', 'content']
        read_only_fields = ['singer']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'