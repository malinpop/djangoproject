from rest_framework import serializers
from appdemo02.models import Defect


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ('bug_code', 'bug_name', 'bug_desc',
                  'bug_priority', 'bug_state')
