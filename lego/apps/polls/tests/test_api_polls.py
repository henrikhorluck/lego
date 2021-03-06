from django.urls import reverse
from rest_framework import status

from lego.apps.polls.models import Poll
from lego.apps.users.models import AbakusGroup, User
from lego.utils.test_utils import BaseAPITestCase


def _get_list_url():
    return reverse("api:v1:polls-list")


def _get_detail_url(pk):
    return reverse("api:v1:polls-detail", kwargs={"pk": pk})


def _get_vote_url(pk):
    return _get_detail_url(pk) + "vote/"


class PollViewSetTestCase(BaseAPITestCase):
    fixtures = ["test_users.yaml", "test_abakus_groups.yaml", "test_polls.yaml"]

    def setUp(self):
        """Create test users"""
        self.admin = User.objects.get(username="test1")
        self.group = AbakusGroup.objects_with_text.get(name="PollAdminTest")
        self.group.add_user(self.admin)

        self.pleb = User.objects.get(username="test2")

        self.poll_data = {
            "title": "Hva mener du?",
            "description": "TestDescription",
            "pinned": True,
            "options": [{"name": "Ja"}, {"name": "Nei"}, {"name": "Tja"}],
        }

        self.poll_update_data = {
            "id": 1,
            "title": "New title",
            "description": "TestDescription1",
            "pinned": False,
            "options": [{"id": 1, "name": "Ja"}, {"name": "edit"}],
        }

    def test_create_poll_admin(self):
        """A user with permissions should be able to create a poll"""
        self.client.force_authenticate(self.admin)
        response = self.client.post(_get_list_url(), self.poll_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_poll_pleb(self):
        """A user without permissions should not be able to create a poll"""
        self.client.force_authenticate(self.pleb)
        response = self.client.post(_get_list_url(), self.poll_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_edit_poll_admin(self):
        """A user with permissions should be able to edit a poll"""
        self.client.force_authenticate(self.admin)
        response = self.client.patch(_get_detail_url(1), self.poll_update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_poll_pleb(self):
        """A user without permissions should not be able to edit a poll"""
        self.client.force_authenticate(self.pleb)
        response = self.client.post(_get_detail_url(1), self.poll_update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_poll_authenticated(self):
        """A user with permissions should be able to list all polls"""
        self.client.force_authenticate(self.pleb)
        response = self.client.get(_get_list_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_poll_unauthenticated(self):
        """A user with no permissions should not be able to list all polls"""
        response = self.client.get(_get_list_url())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detailed_poll_authenticated(self):
        """A user with permissions should be able to retrive the detailed poll view"""
        self.client.force_authenticate(self.pleb)
        response = self.client.get(_get_detail_url(1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detailed_poll_unauthenticated(self):
        """A user with no permissions should not be able to retrive the detailed poll view"""
        response = self.client.get(_get_detail_url(2))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_vote_poll_authenticated_unanswered(self):
        """A user with permissions should be able to vote on a poll that he has not answered"""
        self.client.force_authenticate(self.pleb)
        votes = Poll.objects.get(pk=2).total_votes
        user_count = Poll.objects.get(pk=2).answered_users.count()
        response = self.client.post(_get_vote_url(2), {"optionId": 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Poll.objects.get(pk=2).total_votes, votes + 1)
        self.assertEqual(Poll.objects.get(pk=2).answered_users.count(), user_count + 1)

    def test_vote_poll_authenticated_answered(self):
        """A user should not be able to vote on a poll more than once"""
        self.client.force_authenticate(self.pleb)
        self.client.post(_get_vote_url(2), {"optionId": 3})
        votes = Poll.objects.get(pk=2).total_votes
        user_count = Poll.objects.get(pk=2).answered_users.count()
        response = self.client.post(_get_vote_url(2), {"optionId": 4})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Poll.objects.get(pk=2).total_votes, votes)
        self.assertEqual(Poll.objects.get(pk=2).answered_users.count(), user_count)

    def test_vote_poll_unauthenticated(self):
        """A user with no permissions should not be able to vote on a poll"""
        votes = Poll.objects.get(pk=1).total_votes
        response = self.client.post(_get_vote_url(1), {"optionId": 1})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Poll.objects.get(pk=1).total_votes, votes)

    def test_vote_poll_not_valid(self):
        """A user should not be able to vote on a poll where valid_until is not in the future"""
        self.client.force_authenticate(self.pleb)
        votes = Poll.objects.get(pk=3).total_votes
        user_count = Poll.objects.get(pk=3).answered_users.count()
        response = self.client.post(_get_vote_url(3), {"optionId": 5})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Poll.objects.get(pk=3).total_votes, votes)
        self.assertEqual(Poll.objects.get(pk=3).answered_users.count(), user_count)
