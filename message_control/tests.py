from rest_framework.test import APITestCase
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from six import BytesIO
from PIL import Image
import json


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class TestFileUpload(APITestCase):
    file_upload_url = "/message/file-upload"

    def test_file_upload(self):
        # definition

        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front1.png', avatar.getvalue())
        data = {
            "file_upload": avatar_file
        }

        # processing
        response = self.client.post(self.file_upload_url, data=data)
        result = response.json()

        # assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["id"], 1)

class TestMessage(APITestCase):
    message_url = "/message/message"

    def setUp(self):
        from user_control.models import CustomUser, UserProfile

        payload_sender = {
            "username": "sender",
            "password": "sender123",
            "email": "adefemigreat@yahoo.com"
        }

        payload_receiver = {
            "username": "payload_receiver",
            "password": "payload_receiver123",
            "email": "dineshgreat@yahoo.com"
        }

        # sender
        self.sender = CustomUser.objects.create_user(**payload_sender)
        UserProfile.objects.create(
            first_name="sender", last_name="sender", user=self.sender, caption="sender", about="sender")

        # receiver
        self.receiver = CustomUser.objects.create_user(**payload_receiver)
        UserProfile.objects.create(
            first_name="receiver", last_name="receiver", user=self.receiver, caption="receiver", about="receiver")

        # login
        self.client.force_authenticate(user=self.sender)

    def test_post_message(self):

        payload = {
            "sender_id": self.sender.id,
            "receiver_id": self.receiver.id,
            "message": "test message",

        }

        # processing
        response = self.client.post(self.message_url, data=payload)
        result = response.json()
        print(result)

        # assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["message"], "test message")
        self.assertEqual(result["sender"]["user"]["username"], "sender")
        self.assertEqual(result["receiver"]["user"]["username"], "payload_receiver")