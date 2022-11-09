from requests import post as requests_post
import logging
from models.urls import NEBULA_USERAPI_AUTHORIZATION
from models.nebula.UserAuthorization import NebulaUserAPIAuthorizationTokenResponseModel


class NebulaUserAuthorzation:
    def __init__(self, userToken: str, authorizationHeader: str | None) -> None:
        self.__USER_TOKEN = userToken
        self.__AUTHORIZATION_HEADER = authorizationHeader
        self.__fetch_authrizaton_token()
        self.__post_init__()

    def __fetch_authrizaton_token(self) -> None:
        logging.debug(
            "Fetching authorization token with user token %s...", self.__USER_TOKEN[:5]
        )
        if self.__AUTHORIZATION_HEADER:
            logging.debug(
                "Authorization header already set (`%s...`), not fetching authorization token",
                self.__AUTHORIZATION_HEADER[:10],
            )
            return
        response = requests_post(
            url=NEBULA_USERAPI_AUTHORIZATION,
            headers={"Authorization": f"Token {self.__USER_TOKEN}"},
        )
        if response.status_code == 200:
            self.__AUTHORIZATION_HEADER = NebulaUserAPIAuthorizationTokenResponseModel(
                **response.json()
            ).token
            logging.info(
                "Successfully fetched authorization token from Nebula API: `%s...`",
                self.__AUTHORIZATION_HEADER[:10],
            )
            return
        raise Exception(
            f"Failed to get authorization token for a given user token: `{response.content.__str__()}` with status code {response.status_code}"
        )

    def __post_init__(self) -> None:
        if not self.__USER_TOKEN:
            raise ValueError("User token for Nebula API must not be empty")
        if not self.__AUTHORIZATION_HEADER:
            raise ValueError("Authorization header must not be empty")
        logging.debug("Passed NebulaUserAuthorzation post initialization checks")

    def get_authorization_header(self, full: bool = False) -> str:
        if full:
            return f"Bearer {self.__AUTHORIZATION_HEADER}"
        return self.__AUTHORIZATION_HEADER or ""

    def get_user_token(self) -> str:
        return self.__USER_TOKEN

    def __repr__(self) -> str:
        return f"NebulaUserAuthorzation(userToken={self.__USER_TOKEN}, authorizationHeader={self.__AUTHORIZATION_HEADER})"

    def __str__(self) -> str:
        return self.__repr__()
