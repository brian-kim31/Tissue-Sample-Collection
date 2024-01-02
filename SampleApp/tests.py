import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer  
from django.test import RequestFactory
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from .views import CollectionCreateView, SampleCreateView
from .models import Collection, Sample

pytestmark = pytest.mark.django_db

class TestCollectionCreateView:

    def test_collection_create_view(self):
        user = mixer.blend(User)
        path = reverse('create_collection')
        request = RequestFactory().post(path, data={'disease_term': 'Test Disease', 'title': 'Test Title'})
        request.user = user

        # Add SessionMiddleware and MessageMiddleware
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        messages_middleware = MessageMiddleware(lambda request: None)
        messages_middleware.process_request(request)

        response = CollectionCreateView.as_view()(request)

        assert response.status_code == 302  # Redirects after successful form submission
        assert Collection.objects.filter(user=user, disease_term='Test Disease', title='Test Title').exists()

        # Check if success message is added
        storage = get_messages(request)
        assert any('Collection created successfully.' in message.message for message in storage)

    def test_collection_create_view_invalid_data(self):
        user = mixer.blend(User)
        path = reverse('create_collection')
        request = RequestFactory().post(path, data={})  # Invalid data
        request.user = user

        # Add SessionMiddleware and MessageMiddleware
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        messages_middleware = MessageMiddleware(lambda request: None)
        messages_middleware.process_request(request)

        response = CollectionCreateView.as_view()(request)

        assert response.status_code == 200  # Form submission failed, should return to the same page
        assert not Collection.objects.filter(user=user).exists()  # No collection should be created



class TestSampleCreateView:

    def test_sample_create_view(self):
        user = mixer.blend(User)
        collection = mixer.blend(Collection, user=user)
        path = reverse('add_sample', kwargs={'collection_id': collection.pk})
        request = RequestFactory().post(path, data={'donor_count': 10, 'material_type': 'Test Material'})
        request.user = user

        # Add SessionMiddleware and MessageMiddleware
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        messages_middleware = MessageMiddleware(lambda request: None)
        messages_middleware.process_request(request)

        response = SampleCreateView.as_view()(request, collection_id=collection.pk)

        assert response.status_code == 302  # Redirects after successful form submission
        assert collection.sample_set.filter(user=user, donor_count=10, material_type='Test Material').exists()

        # Check if success message is added
        storage = get_messages(request)
        assert any('Sample created successfully.' in message.message for message in storage)

    def test_sample_create_view_invalid_data(self):
        user = mixer.blend(User)
        collection = mixer.blend(Collection, user=user)
        path = reverse('add_sample', kwargs={'collection_id': collection.pk})
        request = RequestFactory().post(path, data={})  # Invalid data
        request.user = user

        # Add SessionMiddleware and MessageMiddleware
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        messages_middleware = MessageMiddleware(lambda request: None)
        messages_middleware.process_request(request)

        response = SampleCreateView.as_view()(request, collection_id=collection.pk)

        assert response.status_code == 200  # Form submission failed, should return to the same page
        assert not collection.sample_set.filter(user=user).exists()  # No sample should be created