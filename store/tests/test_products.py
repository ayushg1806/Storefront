from decimal import Decimal
import pytest
from model_bakery import baker
from rest_framework import status
from store.models import Product

@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product

@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_product):
        authenticate(is_staff=False)
        
        response = create_product({})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_product):
        authenticate(is_staff=True)
        
        response = create_product({
            'title': '',
            'unit_price': ''
        })
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_product):
        authenticate(is_staff=True)

        collection = baker.make('store.Collection')

        response = create_product({
            'title': 'a',
            'slug': 'a',
            'unit_price': Decimal('10.00'),
            'inventory': 10,
            'collection': collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == product.id
        assert response.data['title'] == product.title

@pytest.mark.django_db
class TestUpdateProduct:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        product = baker.make(Product)

        response = api_client.patch(
            f'/store/products/{product.id}/',
            {'title': 'Updated'}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
        product = baker.make(Product)
        authenticate(is_staff=False)

        response = api_client.patch(
            f'/store/products/{product.id}/',
            {'title': 'Updated'}
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_returns_200(self, authenticate, api_client):
        product = baker.make(Product)
        authenticate(is_staff=True)

        response = api_client.patch(
            f'/store/products/{product.id}/',
            {'title': 'Updated'}
        )

        assert response.status_code == status.HTTP_200_OK
        product.refresh_from_db()
        assert product.title == 'Updated'

@pytest.mark.django_db
class TestDeleteProduct:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        product = baker.make(Product)

        response = api_client.delete(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
        product = baker.make(Product)
        authenticate(is_staff=False)

        response = api_client.delete(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_returns_204(self, authenticate, api_client):
        product = baker.make(Product)
        authenticate(is_staff=True)

        response = api_client.delete(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Product.objects.count() == 0
