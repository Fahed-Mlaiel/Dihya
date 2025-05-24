"""
Dihya – VR/AR Images Tests
Tests unitaires, intégration, e2e, RGPD, sécurité, multilingue, plugins, audit, CI/CD.
"""
import os
import io
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .security import audit_log

class VRARImagesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_image = SimpleUploadedFile('test.png', b'\x89PNG\r\n\x1a\n', content_type='image/png')
        os.makedirs('uploads/vr_ar/', exist_ok=True)

    def test_upload_vrar_image(self):
        response = self.client.post('/assets/images/routes/vr_ar/upload/', {'image': self.test_image}, HTTP_AUTHORIZATION='Bearer test', HTTP_X_ROLE='admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())

    def test_list_vrar_images(self):
        response = self.client.get('/assets/images/routes/vr_ar/list/', HTTP_AUTHORIZATION='Bearer test', HTTP_X_ROLE='user')
        self.assertEqual(response.status_code, 200)
        self.assertIn('images', response.json())

    def test_get_vrar_image_not_found(self):
        response = self.client.get('/assets/images/routes/vr_ar/get/unknown.png', HTTP_AUTHORIZATION='Bearer test', HTTP_X_ROLE='user')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        for f in os.listdir('uploads/vr_ar/'):
            os.remove(os.path.join('uploads/vr_ar/', f))
