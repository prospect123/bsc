from django import urls
from django.contrib.auth import get_user_model
import pytest
@pytest.mark.parametrize('param',[
    ('user_create'),
    ('user_list'),
    ('user_retrieve'),
    ('user_delete'),
    ('user_update'),
])
def test_views(client,param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


