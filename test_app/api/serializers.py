from rest_framework import serializers

from .models import *


class MailingCountSerializer(serializers.ModelSerializer):
    sent_messages = serializers.SerializerMethodField()
    not_sent_messages = serializers.SerializerMethodField()

    class Meta:
        model = MailingList
        fields = [
            'id', 'mailing_launch_datetime', 'mailing_end_datetime',
            'text', 'tag', 'code', 'sent_messages', 'not_sent_messages'
        ]

    def get_count_sent_messages(self, obj):
        return obj.messages.filter(status='S').count()

    def get_count_not_sent_messages(self, obj):
        return obj.messages.filter(status='F').count()


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MailingListSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    class Meta:
        model = MailingList
        fields = [
            'id', 'mailing_launch_datetime', 'mailing_end_datetime',
            'text', 'tag', 'code', 'messages'
        ]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_number(self, number):
        if  str(number)[0] != '7':
            raise serializers.ValidationError(
                'Номер должен начинаться с числа 7, без +.'
            )
        elif len(number) != 11:
            raise serializers.ValidationError(
                'Номер должен содержать 11 символов.'
            )
        else:
            return number