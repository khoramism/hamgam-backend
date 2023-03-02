from rest_framework import serializers
from .models import Skill
from account.serializers import JustEmailSerializer
#from idea.serializers import IdeaSkillSerializer
from idea.models import Category, Comment, Idea
from account.models import Account
from account.serializers import CreaterIdeaSerializer, JustEmailSerializer

class CategorySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('updated', 'created', 'active')
        optional_fields = ['publish', 'slug', 'summary', 'id']

class IdeaSkillSerializer(serializers.ModelSerializer):
    creator = CreaterIdeaSerializer(read_only=True, many=False)
    class Meta:
        model = Idea
        fields = ('id', 'title', 'creator')

class SkillIdeaSerializer(serializers.ModelSerializer):
    users = JustEmailSerializer(read_only=True, many=True)
    #ideas = IdeaSkillSerializer(read_only=True, many=True)
    categories = CategorySkillSerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        fields = ('id', 'users', 'name', 'categories')


class SkillDetailSerializer(serializers.ModelSerializer):
    owner = CreaterIdeaSerializer(read_only=True, many=False)
    users = JustEmailSerializer(read_only=True, many=True)
    ideas = IdeaSkillSerializer(read_only=True, many=True)
    categories = CategorySkillSerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        fields = '__all__'



class SkillCreateSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), many=False)
    #owner = serializers.RelatedField(queryset=Account.objects.all(), many=False)
    #users = serializers.RelatedField(queryset=Account.objects.all(), many=True)
    #users = JustEmailSerializer(read_only=False, many=True, required=False)
    #ideas = IdeaSkillSerializer(read_only=True, many=True, required=False)
    #categories = CategorySerializer(read_only=False, many=True, required=False)
    class Meta:
        model = Skill
        fields = '__all__'



class SkillUpdateSerializer(serializers.ModelSerializer):
    #owner = JustEmailSerializer(read_only=False, many=False)
    #users = JustEmailSerializer(read_only=False, many=True)
    #ideas = IdeaSkillSerializer(read_only=True, many=True)
    #categories = CategorySerializer(read_only=False, many=True)
    class Meta:
        model = Skill
        exclude = ('owner',)

class SkillListSerializer(serializers.ModelSerializer):
    categories = CategorySkillSerializer(read_only=True, many=True)
    class Meta:
        model = Skill
        #fields = '__all__'
        exclude = ('owner', 'users', 'ideas')