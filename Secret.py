from google.cloud import secretmanager

class Secret:
    secrets = {}
    instance = None

    @staticmethod
    def get_instance():
        if Secret.instance is None:
            Secret()
        return Secret.instance

    def __init__(self):
        if Secret.instance is not None:
            raise Exception("Singleton")
        Secret.instance = self
        self.fetch_secrets()

    def fetch_secrets(self):
        secret_ids = ["SLACK_BOT_TOKEN", "SLACK_SIGNING_SECRET", "WEATHER_API_KEY", "ZIPCODE_API_KEY"]
        project_id = "proj2-298620"
        version_id = "latest"

        client = secretmanager.SecretManagerServiceClient()

        for secret_id in secret_ids:
            name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
            response = client.access_secret_version(request={"name": name})
            self.secrets[secret_id] = response.payload.data.decode()



