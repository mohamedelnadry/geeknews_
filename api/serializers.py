from .models import Articles,Authors
from rest_framework import serializers



class SerialiserMyData(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Articles
        
        fields = ['items_id','title','contenttype','publicationdate','category','author']


class SerialiserData(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Articles
        fields = '__all__'


class serialiserauthor(serializers.ModelSerializer):
    articles_set = SerialiserMyData(many=True, read_only=True)

    class Meta:
        model = Authors
        fields = ['author_id','author_name','articles_set']