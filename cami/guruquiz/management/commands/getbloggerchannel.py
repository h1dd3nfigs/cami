import requests
from django.core.management.base import BaseCommand, CommandError
from guruquiz.models import Blogger as Blogger
from apiclient.discovery import build
from apiclient.errors import HttpError
from cami.settings import YOUTUBE_DEVELOPER_KEY as YOUTUBE_DEVELOPER_KEY


class Command(BaseCommand):
    help = "Queries the Youtube API to find a channel for the named username"

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+')

    def handle(self, *args, **options):
        for username in options['username']:
            try:
                blogger = Blogger.objects.get(yt_username=username)
            except Blogger.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    'Blogger with username "%s" does not exist' % username))
                channels = self.get_channels(username)

            self.stdout.write(self.style.SUCCESS(
                channels[0]))

    def get_channels(self, username):
        """
        Ask youtube for any channel names that match the supplied username
        """
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=YOUTUBE_DEVELOPER_KEY)
        results = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            forUsername=username).execute()
        return results["items"]

    def parse_response(self):
        """
        Extract the blogger's data from the response & store in our database
        """
        pass
