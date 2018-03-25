from rest_framework import serializers
from .models import Movie, Person, Role


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')
    # movie_id = serializers.IntegerField(source='movie.id')
    class Meta:
        model = Role
        fields = ['id', 'name', 'role']


class MovieSerializer(serializers.ModelSerializer):
    actor = RoleSerializer(many=True, source='role_set')

    director = serializers.StringRelatedField()
    # actor = serializers.StringRelatedField(many=True,)
    class Meta:
        model = Movie
        fields = '__all__'

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actor')
        movie = super().update(instance, validated_data)
        for actor_data in actors_data:
            ActorInMovie.objects.get_or_create(
                person_id=actor_data['id'],
            )


class PersonSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(source=Role.role)
    class Meta:
        model = Person
        fields = '__all__'
